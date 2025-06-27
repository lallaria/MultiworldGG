import asyncio
from abc import ABC, abstractmethod
from typing import Optional, Any, Dict
from enum import Enum
import weakref


class ClientState(Enum):
    INITIAL = "initial"
    GAME = "game"
    TRANSITIONING = "transitioning"


class ClientProduceBase(ABC):
    """Base class for all client producers"""
    
    def __init__(self, context_or_manager):
        # Handle both AsyncClientContext and ClientManager
        if isinstance(context_or_manager, ClientManager):
            self._manager = weakref.ref(context_or_manager)
            self._context = None
        else:
            self._context = weakref.ref(context_or_manager)
            self._manager = None
        self._is_running = False
    
    @property
    def context(self):
        """Get the context - either direct or through manager"""
        if self._context:
            ctx = self._context()
            if ctx is None:
                raise RuntimeError("Context has been garbage collected")
            return ctx
        elif self._manager:
            mgr = self._manager()
            if mgr is None:
                raise RuntimeError("Manager has been garbage collected")
            return mgr
        else:
            raise RuntimeError("No context or manager available")
    
    @abstractmethod
    async def build(self) -> Any:
        """Build the client component"""
        pass
    
    @abstractmethod
    async def cleanup(self):
        """Cleanup resources before transition"""
        pass
    
    @abstractmethod
    def can_transition_to(self, new_state: ClientState) -> bool:
        """Check if transition to new state is allowed"""
        pass


class InitialClientProduce(ClientProduceBase):
    """Initial client builder that sets up basic connection and auth"""
    
    def __init__(self, context: 'AsyncClientContext'):
        super().__init__(context)
        self._connection_task: Optional[asyncio.Task] = None
        self._auth_data: Dict[str, Any] = {}
    
    async def build(self) -> Dict[str, Any]:
        """Build initial client with connection and authentication"""
        self._is_running = True
        
        try:
            # Simulate initial connection setup
            print("Initial client: Establishing connection...")
            await asyncio.sleep(1)  # Simulate connection time
            
            # Simulate authentication
            print("Initial client: Authenticating...")
            await asyncio.sleep(0.5)
            self._auth_data = {"token": "initial_auth_token", "user_id": "user123"}
            
            # Start background connection monitoring
            self._connection_task = asyncio.create_task(self._monitor_connection())
            
            print("Initial client: Ready for game transition")
            
            return {
                "status": "connected",
                "auth": self._auth_data,
                "connection_task": self._connection_task
            }
            
        except Exception as e:
            self._is_running = False
            raise e
    
    async def _monitor_connection(self):
        """Background task to monitor connection"""
        try:
            while self._is_running and not self.context.is_transitioning:
                await asyncio.sleep(2)
                print("Initial client: Connection heartbeat")
        except asyncio.CancelledError:
            print("Initial client: Connection monitoring cancelled")
            raise
    
    async def cleanup(self):
        """Prepare for transition to game client"""
        print("Initial client: Preparing for transition...")
        # Don't cancel the connection task - let it be inherited
        self._is_running = False
        await asyncio.sleep(0.1)  # Allow graceful cleanup
    
    def can_transition_to(self, new_state: ClientState) -> bool:
        return new_state == ClientState.GAME and self._is_running
    
    @property
    def auth_data(self) -> Dict[str, Any]:
        return self._auth_data.copy()
    
    @property
    def connection_task(self) -> Optional[asyncio.Task]:
        return self._connection_task


class GameClientProduce(ClientProduceBase):
    """Game client builder that extends initial client with game-specific features"""
    
    def __init__(self, context: 'AsyncClientContext', initial_data: Optional[Dict] = None):
        super().__init__(context)
        self._initial_data = initial_data or {}
        self._game_task: Optional[asyncio.Task] = None
        self._inherited_connection_task: Optional[asyncio.Task] = None
    
    async def build(self) -> Dict[str, Any]:
        """Build game client extending initial client"""
        self._is_running = True
        
        try:
            # Inherit connection from initial client
            if "connection_task" in self._initial_data:
                self._inherited_connection_task = self._initial_data["connection_task"]
                print("Game client: Inherited connection from initial client")
            
            # Set up game-specific features
            print("Game client: Setting up game features...")
            await asyncio.sleep(0.5)  # Simulate game setup
            
            # Start game-specific background tasks
            self._game_task = asyncio.create_task(self._game_loop())
            
            print("Game client: Ready for gameplay")
            
            return {
                "status": "game_ready",
                "auth": self._initial_data.get("auth", {}),
                "connection_task": self._inherited_connection_task,
                "game_task": self._game_task
            }
            
        except Exception as e:
            self._is_running = False
            raise e
    
    async def _game_loop(self):
        """Background game loop"""
        try:
            game_tick = 0
            while self._is_running:
                await asyncio.sleep(1)
                game_tick += 1
                print(f"Game client: Game tick {game_tick}")
        except asyncio.CancelledError:
            print("Game client: Game loop cancelled")
            raise
    
    async def cleanup(self):
        """Cleanup game client resources"""
        print("Game client: Cleaning up...")
        self._is_running = False
        
        if self._game_task and not self._game_task.done():
            self._game_task.cancel()
            try:
                await self._game_task
            except asyncio.CancelledError:
                pass
        
        # Note: We don't clean up inherited connection task here
        # as it might be used by other components
    
    def can_transition_to(self, new_state: ClientState) -> bool:
        # Game client could potentially transition to other states
        return False  # For now, game is terminal state


class ClientManager:
    """Manager that can work with existing AsyncClientContext or create new one"""
    
    def __init__(self, existing_context: Optional['AsyncClientContext'] = None):
        self._existing_context = existing_context
        self._current_producer: Optional[ClientProduceBase] = None
        self._state = ClientState.INITIAL
        self._is_transitioning = False
        self._client_data: Dict[str, Any] = {}
        self._context_adapter: Optional['ContextAdapter'] = None
        
        if existing_context:
            self._context_adapter = ContextAdapter(existing_context, self)


class ContextAdapter:
    """Adapter to bridge existing AsyncClientContext with our client producers"""
    
    def __init__(self, existing_context: 'AsyncClientContext', manager: 'ClientManager'):
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


class AsyncClientContext:
    """Context that manages the asyncio lifecycle and state transitions"""
    
    def __init__(self):
        self._current_producer: Optional[ClientProduceBase] = None
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
        
        self._current_producer = InitialClientProduce(self)
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
            self._current_producer = GameClientProduce(self, self._client_data)
            
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


# Example usage and demonstration
async def main():
    """Demonstrate the pattern in action"""
    context = AsyncClientContext()
    
    try:
        # Start initial client
        print("=== Starting Initial Client ===")
        initial_result = await context.start_initial_client()
        print(f"Initial client result: {initial_result}")
        
        # Let it run for a bit
        print("\n=== Initial Client Running ===")
        await asyncio.sleep(3)
        
        # Transition to game client while keeping asyncio context
        print("\n=== Transitioning to Game Client ===")
        game_result = await context.transition_to_game_client()
        print(f"Game client result: {game_result}")
        
        # Let game run for a bit
        print("\n=== Game Client Running ===")
        await asyncio.sleep(5)
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Clean shutdown
        print("\n=== Shutting Down ===")
        await context.shutdown()


if __name__ == "__main__":
    asyncio.run(main())