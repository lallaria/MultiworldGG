# Design Specification: GUI Client Takeover System

## Overview
This specification outlines the design for a system that allows world modules to take over an existing GUI client instance, transitioning from an initial context to a game-specific context while preserving the running GUI and connection state.

## Current Architecture Analysis

### Existing Components
1. **CommonClient.py**: Contains `CommonContext` with `run_gui()` method that creates new GUI instances
2. **ClientBuilder.py**: Implements Builder pattern with `ClientBuilder`, `InitialClient`, and `GameClient` classes
3. **Gui.MultiMDApp**: Main GUI application class accessible via `MDApp.get_running_app()`
4. **World Modules**: Each module has entrypoints defined in `pyproject.toml` for `launch()`, `main()`, `make_gui()`, etc.

### Current Flow
1. Initial client starts with `InitialClient` builder
2. World modules are discovered via entrypoints and called through their defined entrypoints
3. `run_gui()` creates new GUI instances, losing existing state

## Design Requirements

### Functional Requirements
1. **State Preservation**: Preserve `ui`, `ui_task`, and `exit_event` from existing GUI instance
2. **Context Transition**: Seamlessly transition from `InitContext` to game-specific `CommonContext`
3. **Builder Integration**: Utilize existing `ClientBuilder` pattern for state management
4. **Global Access**: Access running GUI via `Gui.MultiMDApp.get_running_app()`
5. **Entrypoint Integration**: Use module entrypoints instead of direct function calls

### Non-Functional Requirements
1. **Minimal Disruption**: Zero downtime during transition
2. **Error Handling**: Graceful fallback to new GUI creation if takeover fails
3. **Thread Safety**: Safe context switching in async environment
4. **Memory Efficiency**: Avoid duplicate GUI instances
5. **Performance**: Complete takeover within 5 minutes

## Proposed Architecture

### 1. Context Hierarchy

```python
class InitContext:
    """Base context for initial GUI state with minimal properties"""
    def __init__(self):
        self.exit_event = asyncio.Event()
        self._state = ClientState.INITIAL
        self._is_transitioning = False

class CommonContext(InitContext):
    """Extended context for game clients with full functionality"""
    # All existing CommonContext properties and methods
    # command_processor will only exist in game clients
    command_processor: typing.Type[CommandProcessor] = None
```

### 2. Enhanced CommonContext

```python
class CommonContext(InitContext):
    def run_gui(self):
        """Modified to support takeover of existing GUI"""
        if self._can_takeover_existing_gui():
            return self._takeover_existing_gui()
        else:
            return self._create_new_gui()
    
    def _can_takeover_existing_gui(self) -> bool:
        """Check if existing GUI can be taken over"""
        try:
            app = MDApp.get_running_app()
            return (app is not None and 
                   hasattr(app, 'ctx') and 
                   isinstance(app.ctx, InitContext) and
                   app.ctx._state == ClientState.INITIAL and
                   not app.ctx._is_transitioning)
        except:
            return False
    
    async def _takeover_existing_gui(self) -> None:
        """Take over existing GUI instance"""
        app = MDApp.get_running_app()
        existing_ctx = app.ctx
        
        # Mark transition state
        existing_ctx._is_transitioning = True
        self._is_transitioning = True
        
        try:
            # Preserve exit_event from existing context
            self.exit_event = existing_ctx.exit_event
            
            # Access ui and ui_task from global app reference
            # No need to store locally - always available via MDApp.get_running_app()
            
            # Update app reference to new context
            app.ctx = self
            
            # Update state
            self._state = ClientState.GAME
            
        finally:
            existing_ctx._is_transitioning = False
            self._is_transitioning = False
    
    def _create_new_gui(self) -> None:
        """Create new GUI instance (existing behavior)"""
        # Original run_gui implementation
        pass
```

### 3. Enhanced ClientBuilder Classes

```python
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
```

### 4. Module Entrypoint Integration

```python
# Example: worlds/kh2/pyproject.toml
[project.entry-points."mwgg.plugins"]
"kh2.WorldClass" = "kh2.Register:WORLD_CLASS"
"kh2.WebWorldClass" = "kh2.Register:WEB_WORLD_CLASS"
"kh2.Client" = "kh2.Register:CLIENT_FUNCTION"

# Example: worlds/kh2/Register.py
CLIENT_FUNCTION = launch  # This will be the function that supports takeover

# Example: worlds/kh2/Client.py
class KH2Context(CommonContext):
    command_processor = KH2CommandProcessor
    game = "Kingdom Hearts 2"
    # ... other game-specific properties ...

def launch():
    async def main(args):
        ctx = KH2Context(args.connect, args.password)
        
        # Check if we can take over existing GUI
        if ctx._can_takeover_existing_gui():
            await ctx._takeover_existing_gui()
        else:
            # Original launch logic
            ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
            if gui_enabled:
                ctx.run_gui()
            ctx.run_cli()
        
        # ... rest of launch logic ...

# Entrypoint discovery and execution
def discover_and_launch_module(module_name: str, args):
    """Discover and launch module via entrypoints"""
    import importlib.metadata
    
    try:
        # Discover entrypoints for mwgg.plugins
        entry_points = importlib.metadata.entry_points()
        plugin_entry_points = entry_points.get("mwgg.plugins", {})
        
        client_entry_key = f"{module_name}.Client"
        if client_entry_key in plugin_entry_points:
            # Load and execute the CLIENT_FUNCTION entrypoint
            entry_point = plugin_entry_points[client_entry_key]
            launch_function = entry_point.load()
            launch_function(args)
        else:
            raise ValueError(f"Client entrypoint for module {module_name} not found")
            
    except Exception as e:
        logger.error(f"Failed to launch module {module_name}: {e}")
        raise
```

### 5. State Management

```python
class ClientState(Enum):
    INITIAL = "initial"
    GAME = "game"
    TRANSITIONING = "transitioning"
```

## Global Access Pattern

### Accessing GUI Components
```python
from kivymd.app import MDApp

# Access current GUI components
app = MDApp.get_running_app()
kivy_ui = app.ctx.ui
ui_task = app.ctx.ui_task
exit_event = app.ctx.exit_event
event_loop = app.ctx.loop

# These are always available when a GUI is running
# No need to store references locally
```

## Implementation Strategy

### Phase 1: Core Infrastructure
1. Create `InitContext` base class with minimal properties
2. Modify `CommonContext` to inherit from `InitContext`
3. Implement `_can_takeover_existing_gui()` and `_takeover_existing_gui()` methods
4. Add state management properties

### Phase 2: Builder Integration
1. Update `GameClient` builder to use global access for GUI components
2. Implement context preservation logic (preserve exit_event, no local storage needed for others)
3. Add error handling and fallback mechanisms

### Phase 3: Module Entrypoint Updates
1. Update existing `CLIENT_FUNCTION` entrypoints to support takeover
2. Implement entrypoint discovery and execution system using `mwgg.plugins`
3. Add game-specific setup hooks via existing entrypoints

### Phase 4: Testing and Validation
1. Test takeover scenarios with existing world modules via `mwgg.plugins` entrypoints
2. Validate that global access works correctly after takeover
3. Verify Window event loop remains the same
4. Performance testing to ensure <5 minute transition time

## Testing Strategy

### Primary Test Case
1. Start initial client with `InitContext` (only basic properties)
2. Launch world module via `mwgg.plugins` entrypoint that performs takeover
3. Verify same Kivy app instance with full `CommonContext` or subclass of `CommonContext`
4. Confirm Window event loop is identical
5. Verify global access to `ui`, `ui_task`, `exit_event`, and `loop` works

### Validation Points
- `MDApp.get_running_app()` returns same instance
- `app.ctx.ui_task` reference is preserved
- `app.ctx.exit_event` reference is preserved
- `app.ctx.loop` remains unchanged
- All game-specific functionality works after takeover
- Global access pattern works correctly
- Entrypoint discovery and execution works via `mwgg.plugins`

## Error Handling

### Takeover Failures
- Fallback to new GUI creation if takeover detection fails
- Log takeover attempts and failures for debugging
- Graceful degradation when existing GUI is incompatible

### State Corruption
- Validate context state before and after transitions
- Clear error messages for debugging

## Migration Path

### Backward Compatibility
- None - the existing gui is being removed

### World Module Updates
- Minimal changes required to existing modules
- Modify existing `CLIENT_FUNCTION` entrypoints to support takeover
- Optional override of `run_gui()`, `launch()`, `make_gui()`, `main()` for takeover support
- Clear documentation for migration process
- No changes needed to `pyproject.toml` entrypoint definitions

## Performance Considerations

### Memory Usage
- Avoid duplicate GUI instances during transition
- No local storage of GUI references (use global access)
- Monitor memory usage during state transitions

### Transition Speed
- Minimize blocking operations during takeover
- Use async patterns for state preservation
- Target <5 minute completion time

## Security Considerations

### Context Validation
- Validate existing GUI ownership before takeover
- Prevent unauthorized context modifications
- Sanitize state data during transitions

### Error Isolation
- Isolate takeover failures from main application
- Prevent state corruption across contexts
- Secure error reporting without exposing internal state

## Conclusion

This design specification provides a streamlined framework for implementing GUI client takeover functionality while maintaining the existing architecture and ensuring backward compatibility. The focus on global access patterns eliminates the need for local storage of GUI references and simplifies the implementation. The integration with existing `mwgg.plugins` entrypoints provides a clean plugin architecture for world modules. 