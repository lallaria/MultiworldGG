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
                "kivy_ui": self._kivy_ui,
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
    def __init__(self, ctx: CommonContext, init_data: dict[Gui.MultiMDApp, asyncio.Task] = None):
        super().__init__(ctx)
        self._ui_task: Optional[asyncio.Task] = init_data["ui_task"]
        self._kivy_ui: Optional[Gui.MultiMDApp] = init_data["kivy_ui"]

    async def build(self) -> None:
        """Build game client extending initial client"""
        self._is_running = True
        
        try:
            # Inherit connection from initial client
            if "ui_task" in self.ctx.ui_context:
                self._ui_task = self.ctx.ui_context["ui_task"]
                self._kivy_ui = self.ctx.ui_context["kivy_ui"]
                #Inherit connection from initial client
            
            # Set up game-specific features
            return {}
            
        except Exception as e:
            self._is_running = False
            raise e

    async def _console_loop(self) -> None:
        self.ctx.console_task = asyncio.create_task(console_loop(self.ctx), name="console loop")
    
    async def _keep_alive_loop(self) -> None:
        self.ctx.keep_alive_task = asyncio.create_task(keep_alive(self.ctx), name="keep alive loop")
    
    async def _server_loop(self) -> None:
        self.ctx.server_task = asyncio.create_task(server_loop(self.ctx), name="server loop")
    
    async def _autoreconnect_loop(self) -> None:
        self.ctx.autoreconnect_task = asyncio.create_task(server_autoreconnect(self.ctx), name="server auto reconnect")
    
    async def cleanup(self) -> None:
        self._is_running = False
        await asyncio.sleep(0.1)
    
    def can_transition_to(self, new_state: ClientState) -> bool:
        return False #For now, not going to transition to other games
    
    def produce_client_cli(self) -> None:
        self._client.add("CLI")
    
    def produce_client_gui(self) -> None:
        self._client.add("GUI")
    
    def produce_client_ctx(self) -> None:
        self._client.add("Context")
    
    def produce_client_cli(self) -> None:
        self._client.add("CLI")

    def produce_kivy_client(self) -> "type[Gui.KivyMDGUI]":
        self._client.add("asyncio.Task[None]")

    def produce_client_gui(self) -> None:
        self._client.add("asyncio.Task[None]")

    def produce_client_ctx(self, ctx: CommonContext) -> None:
        self._client.add("Context")
    
    def produce_ctx_server_task(self) -> None:
        self._client.add("asyncio.Task[None]")

    def produce_ctx_keep_alive_task(self) -> None:
        self._client.add("asyncio.Task[None]")

    def produce_client_autoreconnect(self) -> None:
        self._client.add("asyncio.Task[None]")

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
        self._client_builder.produce_client_cli()
        self._client_builder.produce_client_ctx()
        self._client_builder.produce_client_world_data()
        self._client_builder.produce_client_connector()
    
    def build_gui_client(self) -> None:
        self._client_builder.produce_client_gui()
        self._client_builder.produce_client_ctx()
        self._client_builder.produce_client_world_data()
        self._client_builder.produce_client_connector()

    def build_client(self) -> None:
        self._client_builder.produce_client_cli()
        self._client_builder.produce_client_gui()
        self._client_builder.produce_client_ctx()
        self._client_builder.produce_client_world_data()
        self._client_builder.produce_client_connector()


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
