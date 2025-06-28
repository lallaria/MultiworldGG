from __future__ import annotations
from abc import ABC, abstractmethod
from gui import Gui
from enum import Enum
from CommonClient import *
from worlds.AutoWorld import MultiWorld
from typing import Optional, Any, Dict
import asyncio
import time
import weakref
from kivymd.app import MDApp
from NetUtils import Endpoint
from Utils import Version
from NetUtils import NetworkItem

class ClientState(Enum):
    INITIAL = "initial"
    GAME = "game"
    TRANSITIONING = "transitioning"

class ClientBuilder(ABC):
    _ctx: Optional[weakref.ReferenceType[CommonContext]] = None
    _mgr: Optional[weakref.ReferenceType[ClientManager]] = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == "ctx":
                self._ctx = weakref.ref(value)
            elif key == "mgr":
                self._mgr = weakref.ref(value)
            else:
                raise ValueError(f"Invalid keyword argument: {key}")
        self._is_running = False

    @property
    def ctx(self):
        if self._ctx:
            ctx = self._ctx()
            if ctx is None:
                raise RuntimeError("Context has been garbage collected")
            return ctx
        elif self._mgr:
            mgr = self._mgr()
            if mgr is None:
                raise RuntimeError("Manager has been garbage collected")
            return mgr
        else:
            raise RuntimeError("No context or manager available")
    
    @abstractmethod
    def build(self) -> Any:
        pass

    @abstractmethod
    def cleanup(self) -> None:
        pass

    @abstractmethod
    def can_transition_to(self, new_state: ClientState) -> bool:
        pass

    # @abstractmethod
    # def produce_client_cli(self) -> None:
    #     pass
    # @abstractmethod
    # def produce_client_gui(self) -> None:
    #     pass
    # @abstractmethod
    # def produce_client_ctx(self) -> None:
    #     pass
    # @abstractmethod
    # def produce_client_world_data(self) -> None:
    #     pass
    # @abstractmethod
    # def produce_client_connector(self) -> None:
    #     pass

class InitialClient(ClientBuilder):

    def __init__(self, ctx: InitContext):
        super().__init__(ctx)
        self._ui_task: Optional[asyncio.Task] = None
        self._kivy_ui: Optional[Gui.MultiMDApp] = None

    async def build(self) -> Dict[str, Any]:
        self._is_running = True
        
        try:
            self._kivy_ui = Gui.MultiMDApp(self.ctx)
            self._ui_task = asyncio.create_task(self._run_gui())

            return {
                "ui_task": self._ui_task
            }
        
        except Exception as e:
            self._is_running = False
            raise e
        
    async def _run_gui(self):
        pass
    
    async def cleanup(self) -> None:
        self._is_running = False
        await asyncio.sleep(0.1)
    
    def can_transition_to(self, new_state: ClientState) -> bool:
        return new_state == ClientState.GAME and self._is_running
    
    def produce_client_cli(self) -> None:
        self._client.add("CLI")
    
    def produce_client_gui(self) -> None:
        self._client.add("GUI")
    @property
    def client(self) -> Client:
        client = self._client
        self.reset()
        return client
    
    def produce_client_cli(self) -> None:
        self._client.add("CLI")

    def produce_client_gui(self) -> None:
        self._client.add("GUI")

class GameClient(ClientBuilder):
    def __init__(self, ctx: CommonContext, init_data: dict[str, Any] = None):
        super().__init__(ctx=ctx)
        # No need to store ui_task or kivy_ui - always available via global access

    async def build(self) -> Dict[str, Any]:
        """Build game client extending initial client"""
        self._is_running = True
        
        try:
            # Access ui, ui_task, and exit_event from global app reference when needed
            # MDApp.get_running_app().ctx.ui
            # MDApp.get_running_app().ctx.ui_task
            # MDApp.get_running_app().ctx.exit_event
            
            # Set up game-specific features
            await self._setup_game_features()
            
            return {}
            
        except Exception as e:
            self._is_running = False
            raise e
    
    async def _setup_game_features(self) -> None:
        """Initialize game-specific functionality"""
        # Override in subclasses for game-specific setup
        pass

class Client():
    def __init__(self):
        self.features = []
    def add(self, feature: str) -> None:
        self.features.append(feature)
    def __str__(self) -> str:
        return "Client with features: " + ", ".join(self.features)
    
class ClientDirector():

    def __init__(self) -> None:
        self._client_builder = None

    @property
    def client_builder(self) -> ClientBuilder:
        return self._client_builder

    @client_builder.setter
    def client_builder(self, client_builder: ClientBuilder) -> None:
        self._client_builder = client_builder

    def build_cli_client(self) -> None:
        self._client_builder.build()
    
    def build_gui_client(self) -> None:
        self._client_builder.build()

    def build_client(self) -> None:
        self._client_builder.produce_client_cli()
        self._client_builder.produce_client_gui()
        self._client_builder.produce_client_ctx()
        self._client_builder.produce_client_world_data()
        self._client_builder.produce_client_connector()


class ClientManager:
    """Manager that can work with existing InitContext or create new one"""
    
    def __init__(self, existing_context: Optional['InitContext'] = None):
        self._existing_context = existing_context
        self._current_producer: Optional[ClientBuilder] = None
        self._state = ClientState.INITIAL
        self._is_transitioning = False
        self._client_data: Dict[str, Any] = {}
        self._context_adapter: Optional['ContextAdapter'] = None
        
        if existing_context:
            self._context_adapter = ContextAdapter(existing_context, self)


class ContextAdapter:
    """Adapter to bridge existing InitContext with our client producers"""
    
    def __init__(self, existing_context: 'InitContext', manager: 'ClientManager'):
        self._existing_context = existing_context
        self._manager = weakref.ref(manager)
        self._inherited_tasks: Dict[str, asyncio.Task] = {}
    
    @property
    def manager(self) -> 'ClientManager':
        mgr = self._manager()
        if mgr is None:
            raise RuntimeError("Manager has been garbage collected")
        return mgr
    
    def inherit_existing_tasks(self) -> Dict[str, Any]:
        """Extract and inherit tasks from existing context"""
        inherited_data = {}
        
        # Try to extract common attributes from existing context
        if hasattr(self._existing_context, '_client_data'):
            inherited_data.update(self._existing_context._client_data)
        
        if hasattr(self._existing_context, 'get_running_tasks'):
            self._inherited_tasks = self._existing_context.get_running_tasks()
            inherited_data['inherited_tasks'] = self._inherited_tasks
        
        return inherited_data
    
    async def register_new_tasks(self, new_tasks: Dict[str, asyncio.Task]):
        """Register new tasks with existing context if it supports it"""
        if hasattr(self._existing_context, 'register_tasks'):
            await self._existing_context.register_tasks(new_tasks)


class InitContext:
    """Context that manages the asyncio lifecycle and state transitions"""
    
    def __init__(self):
        self._current_producer: Optional[ClientBuilder] = None
        self._state = ClientState.INITIAL
        self._is_transitioning = False
        self._client_data: Dict[str, Any] = {}
        self._main_task: Optional[asyncio.Task] = None
        self._registered_tasks: Dict[str, asyncio.Task] = {}
    
    @property
    def state(self) -> ClientState:
        return self._state
    
    @property
    def is_transitioning(self) -> bool:
        return self._is_transitioning
    
    def get_running_tasks(self) -> Dict[str, asyncio.Task]:
        """Get currently running tasks"""
        running_tasks = {}
        running_tasks.update(self._registered_tasks)
        
        if "connection_task" in self._client_data and self._client_data["connection_task"]:
            running_tasks["connection_task"] = self._client_data["connection_task"]
        if "game_task" in self._client_data and self._client_data["game_task"]:
            running_tasks["game_task"] = self._client_data["game_task"]
            
        return running_tasks
    
    async def register_tasks(self, tasks: Dict[str, asyncio.Task]):
        """Register new tasks with the context"""
        self._registered_tasks.update(tasks)
    
    async def start_initial_client(self) -> Dict[str, Any]:
        """Start with initial client producer"""
        if self._current_producer is not None:
            raise RuntimeError("Client already started")
        
        self._current_producer = InitialClient(self)
        self._state = ClientState.INITIAL
        
        self._client_data = await self._current_producer.build()
        return self._client_data
    
    async def transition_to_game_client(self) -> Dict[str, Any]:
        """Transition from initial to game client while preserving asyncio context"""
        if self._state != ClientState.INITIAL:
            raise RuntimeError(f"Cannot transition to game from state: {self._state}")
        
        if not self._current_producer or not self._current_producer.can_transition_to(ClientState.GAME):
            raise RuntimeError("Current producer cannot transition to game state")
        
        self._is_transitioning = True
        self._state = ClientState.TRANSITIONING
        
        try:
            # Prepare current producer for transition
            await self._current_producer.cleanup()
            
            # Create new game client producer with inherited data
            old_producer = self._current_producer
            self._current_producer = GameClient(self, self._client_data)
            
            # Build new client
            self._client_data = await self._current_producer.build()
            
            self._state = ClientState.GAME
            self._is_transitioning = False
            
            print("Transition to game client completed successfully")
            return self._client_data
            
        except Exception as e:
            self._is_transitioning = False
            self._state = ClientState.INITIAL  # Rollback
            raise e
    
    async def shutdown(self):
        """Shutdown the client context and cleanup all resources"""
        if self._current_producer:
            await self._current_producer.cleanup()
        
        # Clean up any remaining tasks in client data
        if "connection_task" in self._client_data:
            task = self._client_data["connection_task"]
            if task and not task.done():
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
        
        if "game_task" in self._client_data:
            task = self._client_data["game_task"]
            if task and not task.done():
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
        
        print("Client context shutdown complete")

class UIContext:
    """Context that manages the asyncio lifecycle and state transitions"""

    def __init__(self):
        self._current_client_build: Optional[ClientBuilder] = None
        self._state = ClientState.INITIAL
        self._is_transitioning = False
        self._initial_ctx: dict[Gui.MultiMDApp, asyncio.Task] = {}
        self._main_task: Optional[asyncio.Task] = None
    
    @property
    def state(self) -> ClientState:
        return self._state
    
    @property
    def is_transitioning(self) -> bool:
        return self._is_transitioning
    
    async def start_initial_client(self) -> dict[Gui.MultiMDApp, asyncio.Task]:
        """Start with initial client producer"""
        if self._current_client is not None:
            raise RuntimeError("Client already started")
        
        self._current_client = InitialClient(self)
        self._state = ClientState.INITIAL
        
        self._initial_ctx = await self._current_client.build()
        return self._initial_ctx
    
    async def transition_to_game_client(self) -> Dict[str, Any]:
        """Transition from initial to game client while preserving asyncio ctx"""
        if self._state != ClientState.INITIAL:
            raise RuntimeError(f"Cannot transition to game from state: {self._state}")
        
        if not self._current_client or not self._current_client.can_transition_to(ClientState.GAME):
            raise RuntimeError("Current client build cannot transition to game state")
        
        self._is_transitioning = True
        self._state = ClientState.TRANSITIONING
        
        try:
            # Prepare current producer for transition
            await self._current_client.cleanup()
            
            # Create new game client producer with inherited data
            old_client = self._current_client
            self._current_client = GameClient(self, self._initial_ctx)
            
            # Build new client
            self._initial_ctx = await self._current_client.build()
            
            self._state = ClientState.GAME
            self._is_transitioning = False
            
            print("Transition to game client completed successfully")
            return self._initial_ctx
            
        except Exception as e:
            self._is_transitioning = False
            self._state = ClientState.INITIAL  # Rollback
            raise e
    
    @property
    def state(self) -> ClientState:
        return self._state
    
    @property
    def is_transitioning(self) -> bool:
        return self._is_transitioning
    
    async def start_initial_client(self) -> dict[Gui.MultiMDApp, asyncio.Task]:
        """Start with initial client producer"""
        if self._current_client is not None:
            raise RuntimeError("Client already started")
        
        self._current_client = InitialClient(self)
        self._state = ClientState.INITIAL
        
        self._initial_ctx = await self._current_producer.build()
        return self._initial_ctx
    
    async def transition_to_game_client(self) -> dict[Gui.MultiMDApp, asyncio.Task]:
        """Transition from initial to game client while preserving asyncio ctx"""
        if self._state != ClientState.INITIAL:
            raise RuntimeError(f"Cannot transition to game from state: {self._state}")
        
        if not self._current_producer or not self._current_producer.can_transition_to(ClientState.GAME):
            raise RuntimeError("Current producer cannot transition to game state")
        
        self._is_transitioning = True
        self._state = ClientState.TRANSITIONING
        
        try:
            # Prepare current producer for transition
            await self._current_producer.cleanup()
            
            # Create new game client producer with inherited data
            old_client = self._current_client
            self._current_client = GameClient(self, self._initial_ctx)
            
            # Build new client
            self._initial_ctx = await self._current_producer.build()
            
            self._state = ClientState.GAME
            self._is_transitioning = False
            
            print("Transition to game client completed successfully")
            return self._initial_ctx
            
        except Exception as e:
            self._is_transitioning = False
            self._state = ClientState.INITIAL  # Rollback
            raise e
    
    async def shutdown(self):
        """Shutdown the client ctx and cleanup all resources"""
        if self._current_producer:
            await self._current_producer.cleanup()
        
        # Clean up any remaining tasks in client data
        if "connection_task" in self._initial_ctx:
            task = self._initial_ctx["connection_task"]
            if task and not task.done():
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
        
        if "game_task" in self._initial_ctx:
            task = self._initial_ctx["game_task"]
            if task and not task.done():
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
        
        print("Client ctx shutdown complete")





if __name__ == "__main__":
    director = ClientDirector()
    director.client_builder = InitialClient()
    director.build_cli_client() #if args.cli
    director.client_builder = GameClient(director.client_builder.ctx)
    director.build_client() #all other scenarios
    print(director.client_builder.client)
