# Design Specification: GUI Client Takeover System

## Overview
This specification outlines the design for a system that allows world modules to take over an existing GUI client instance, transitioning from an initial context to a game-specific context while preserving the running GUI and connection state.

## Current Architecture Analysis

### Existing Components
1. **CommonClient.py**: Contains `CommonContext` with `run_gui()` method that creates new GUI instances
2. **ClientBuilder.py**: Implements Builder pattern with `ClientBuilder`, `InitialClient`, and `GameClient` classes
3. **Gui.MultiMDApp**: Main GUI application class accessible via `MDApp.get_running_app()`
4. **World Modules**: Each module has a `launch()` or `main()` function that calls `run_gui()`

### Current Flow
1. Initial client starts with `InitialClient` builder
2. World modules create new contexts and call `run_gui()` 
3. `run_gui()` creates new GUI instances, losing existing state

## Design Requirements

### Functional Requirements
1. **State Preservation**: Preserve only `ui` and `ui_task` from existing GUI instance
2. **Context Transition**: Seamlessly transition from `InitContext` to game-specific `CommonContext`
3. **Builder Integration**: Utilize existing `ClientBuilder` pattern for state management
4. **Global Access**: Access running GUI via `Gui.MultiMDApp.get_running_app()`
5. **Backward Compatibility**: Maintain existing `launch()` and `main()` function signatures

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
        self.ui: Optional[Gui.MultiMDApp] = None
        self.ui_task: Optional[asyncio.Task] = None
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
            app = Gui.MultiMDApp.get_running_app()
            return (app is not None and 
                   hasattr(app, 'ctx') and 
                   isinstance(app.ctx, InitContext) and
                   app.ctx._state == ClientState.INITIAL and
                   not app.ctx._is_transitioning)
        except:
            return False
    
    async def _takeover_existing_gui(self) -> None:
        """Take over existing GUI instance"""
        app = Gui.MultiMDApp.get_running_app()
        existing_ctx = app.ctx
        
        # Mark transition state
        existing_ctx._is_transitioning = True
        self._is_transitioning = True
        
        try:
            # Preserve only ui and ui_task
            self.ui = existing_ctx.ui
            self.ui_task = existing_ctx.ui_task
            
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
        self._ui_task: Optional[asyncio.Task] = init_data.get("ui_task") if init_data else None
        self._kivy_ui: Optional[Gui.MultiMDApp] = init_data.get("ui") if init_data else None

    async def build(self) -> Dict[str, Any]:
        """Build game client extending initial client"""
        self._is_running = True
        
        try:
            # Inherit existing GUI task if available
            if self._ui_task:
                self.ctx.ui_task = self._ui_task
            if self._kivy_ui:
                self.ctx.ui = self._kivy_ui
            
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

### 4. World Module Integration

```python
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
```

### 5. State Management

```python
class ClientState(Enum):
    INITIAL = "initial"
    GAME = "game"
    TRANSITIONING = "transitioning"
```

## Implementation Strategy

### Phase 1: Core Infrastructure
1. Create `InitContext` base class with minimal properties
2. Modify `CommonContext` to inherit from `InitContext`
3. Implement `_can_takeover_existing_gui()` and `_takeover_existing_gui()` methods
4. Add state management properties

### Phase 2: Builder Integration
1. Update `GameClient` builder to handle existing GUI instances
2. Implement context preservation logic for `ui` and `ui_task` only
3. Add error handling and fallback mechanisms

### Phase 3: World Module Updates
1. Update world modules to use takeover system
2. Maintain backward compatibility with existing `launch()` functions
3. Add game-specific setup hooks

### Phase 4: Testing and Validation
1. Test takeover scenarios with existing world modules
2. Validate that `ui` and `ui_task` are preserved
3. Verify Window event loop remains the same
4. Performance testing to ensure <5 minute transition time

## Testing Strategy

### Primary Test Case
1. Start initial client with `InitContext` (only `ui` and `ui_task`)
2. Launch world module that performs takeover
3. Verify same Kivy app instance with full `CommonContext`
4. Confirm Window event loop is identical

### Validation Points
- `Gui.MultiMDApp.get_running_app()` returns same instance
- `ui_task` reference is preserved
- Window event loop remains unchanged
- All game-specific functionality works after takeover

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
- Existing `run_gui()` calls continue to work
- World modules can opt-in to takeover functionality
- Gradual migration without breaking existing functionality

### World Module Updates
- Minimal changes required to existing modules
- Optional override of `run_gui()` for takeover support
- Clear documentation for migration process

## Performance Considerations

### Memory Usage
- Avoid duplicate GUI instances during transition
- Clean up old context references after successful takeover
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

This design specification provides a streamlined framework for implementing GUI client takeover functionality while maintaining the existing architecture and ensuring backward compatibility. The focus on preserving only `ui` and `ui_task` simplifies the implementation and reduces potential conflicts. 