# MultiworldGG Plugin System

This document describes the plugin system implementation for MultiworldGG, which allows game worlds to be loaded as plugins.

## Overview

The plugin system provides a way to dynamically load game worlds without modifying the core MultiworldGG codebase. Each plugin is a self-contained package that includes:

- Plugin metadata (`pyproject.toml`)
- Registration information (`Register.py`)
- Game world files (Items.py, Locations.py, etc.)

## Plugin Structure

### Required Files

1. **`pyproject.toml`** - Plugin metadata and configuration
2. **`Register.py`** - Plugin registration and class references

### Optional Files

- `Items.py` - Game items definition
- `Locations.py` - Game locations definition
- `Regions.py` - Game regions definition
- `Rules.py` - Game logic rules
- `Options.py` - Game options
- `Client.py` - Game client implementation
- `WebWorld.py` - Web interface implementation

## Plugin Configuration

### pyproject.toml

```toml
[project]
name = "your_plugin_name"
version = "1.0.0"
description = "Your Game Description"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
requires-python = ">=3.12"

[project.entry-points."mwgg.plugins"]
"your_plugin.WorldClass" = "your_plugin.Register:WORLD_CLASS"
"your_plugin.WebWorldClass" = "your_plugin.Register:WEB_WORLD_CLASS"
"your_plugin.Client" = "your_plugin.Register:CLIENT_FUNCTION"
```

### Register.py

```python
# Required metadata
PLUGIN_NAME = "your_plugin_name"
GAME_NAME = "Your Game Name"
IGDB_ID = 12345
AUTHOR = "Your Name"
VERSION = "1.0.0"

# Import your world classes
from .Items import YourWorldClass
from .WebWorld import YourWebWorldClass
from .Client import launch_client

# Plugin entry points
WORLD_CLASS = YourWorldClass
WEB_WORLD_CLASS = YourWebWorldClass
CLIENT_FUNCTION = launch_client
```

## Plugin Discovery

The plugin system automatically discovers plugins in the following directories:

1. `worlds/` - Built-in worlds (existing structure)
2. `custom_worlds/` - Custom user worlds

A directory is considered a plugin if it contains both:
- `pyproject.toml`
- `Register.py`

## Plugin Validation

The system validates plugins by checking:

1. **pyproject.toml validation:**
   - Required fields: `name`, `description`, `authors`, `requires-python`
   - Python version requirement (must be >=3.12)
   - Plugin name matches directory name

2. **Register.py validation:**
   - Required variables: `PLUGIN_NAME`, `GAME_NAME`, `IGDB_ID`, `AUTHOR`, `VERSION`
   - Optional variables: `WORLD_CLASS`, `WEB_WORLD_CLASS`, `CLIENT_FUNCTION`

## Plugin Loading

When a plugin is loaded:

1. The system validates the plugin structure
2. Imports the `Register.py` file
3. Extracts class references and metadata
4. Registers components with MultiworldGG systems:
   - World classes with AutoWorld system
   - Web world classes with WebWorld system
   - Client functions with LauncherComponents

## Backward Compatibility

The plugin system is designed to be backward compatible:

- Existing worlds without plugin files continue to work
- Plugin and legacy worlds can coexist
- No changes required to existing world implementations

## Example Plugin

See the `example_plugin/` directory for a complete example of a plugin structure.

## Testing

The plugin system includes comprehensive unit tests in `test/test_plugin_system.py` that cover:

- Plugin discovery
- Plugin validation
- Plugin loading
- Component registration
- Error handling
- Backward compatibility

Run the tests with:
```bash
python -m pytest test/test_plugin_system.py -v
```

## Implementation Details

### Core Classes

- **`PluginManager`** - Manages plugin discovery, loading, and registration
- **`PluginValidator`** - Validates plugin metadata and structure
- **`PluginLoader`** - Loads plugins from validated directories
- **`PluginData`** - Data structure for loaded plugin information

### Integration Points

- **AutoWorld System** - World class registration
- **LauncherComponents** - Client component registration
- **WebWorld System** - Web interface registration

## Error Handling

The plugin system includes robust error handling:

- Invalid plugins are logged but don't crash the system
- Missing required files are reported
- Import errors are caught and logged
- Duplicate registrations are prevented

## Future Enhancements

Potential future improvements:

1. Plugin versioning and updates
2. Plugin dependencies
3. Plugin configuration UI
4. Plugin marketplace
5. Plugin signing and verification 