# MultiworldGG Plugin System Design Specification

## Overview

This document outlines the design for a plugin system that will allow MultiworldGG to dynamically load game worlds as packaged plugins, replacing the current hardcoded world registration system.

## Current System Analysis

The current system uses:
- Direct imports in `worlds/` directory
- `AutoWorldRegister` metaclass for automatic world registration
- `LauncherComponents` for client registration
- Hardcoded component registration in each world's `__init__.py`

## Plugin System Design

### 1. Root Entry Point (`Plugin.py`)

A new entry point file in the root directory that will:
- Discover and load plugins from configured plugin directories
- Register worlds, clients, and components dynamically
- Provide plugin management functionality

### 2. Plugin Package Structure

Each plugin will maintain its existing folder structure with minimal changes:

```
plugin_name/
├── pyproject.toml          # Package metadata and entry points
├── Register.py            # NEW: Plugin registration information
├── __init__.py            # Existing world initialization (unchanged)
├── Items.py               # Existing items (unchanged)
├── Locations.py           # Existing locations (unchanged)
├── Regions.py             # Existing regions (unchanged)
├── Rules.py               # Existing rules (unchanged)
├── Options.py             # Existing options (unchanged)
├── Client.py              # Existing client (unchanged)
├── Types.py               # Existing types (unchanged)
└── data/                  # Existing data files (unchanged)
```

**Key Changes:**
- Add `pyproject.toml` for plugin metadata
- Add `Register.py` for class registration information
- All existing files remain unchanged

### 3. Register.py Specification

The new `Register.py` file will contain the plugin registration information:

```python
# Register.py
from . import WorldClassName, WebWorldClassName, launch_client

# Plugin metadata
PLUGIN_NAME = "foldername"
GAME_NAME = "Game Name"  # From world class game= attribute
IGDB_ID = 12345         # From world class igdb_id= attribute
AUTHOR = "Author Name"   # From world class author= attribute
VERSION = "1.0.0"       # From existing version info if available

# Class references
WORLD_CLASS = WorldClassName
WEB_WORLD_CLASS = WebWorldClassName  # Optional
CLIENT_FUNCTION = launch_client      # Optional

# Entry point mappings
ENTRY_POINTS = {
    "foldername.WorldClass": "foldername.Register:WORLD_CLASS",
    "foldername.WebWorldClass": "foldername.Register:WEB_WORLD_CLASS",  # if exists
    "foldername.Client": "foldername.Register:CLIENT_FUNCTION",         # if exists
}
```

### 4. pyproject.toml Specification

Each plugin's `pyproject.toml` must contain:

```toml
[project]
name = "foldername"                    # Must match folder name
version = "1.0.0"  # version shouldn't be random - many of these have versions listed already
description = "Game Name"
authors = [
    {name = "author= in world class", email = "none right now"}
]
requires-python = ">=3.12"
dependencies = [
    # Plugin-specific dependencies <!-- each folder has its own requirements.txt, pull from there -->
]

[project.optional-dependencies]
# Optional dependency groups

[project.scripts]
# GUI script entry point (if applicable)
launch-client = "foldername:launch_client"

[project.entry-points."mwgg.plugins"]
# Core plugin entry points - these point to Register.py
"foldername.WorldClass" = "foldername.Register:WORLD_CLASS"
"foldername.WebWorldClass" = "foldername.Register:WEB_WORLD_CLASS"  # if exists
"foldername.Client" = "foldername.Register:CLIENT_FUNCTION"  # if exists <!-- some of the current Client.py files use main() rather than launch_client, or it's elsewhere. We can fix this later. -->

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"
```

### 5. Plugin Discovery and Loading

The `Plugin.py` entry point will:

1. **Scan Plugin Directories**: Look for plugins in configured directories
2. **Validate Plugins**: Check `pyproject.toml` for required metadata

<!-- The plugins need to be lazy-loaded, but I do need the metadata
There are too many folders/plugins to load every one at once. -->
3. **Load Plugins**: Import and register world classes, clients, and components
<!-- Should be done via metadata scanning, not loading the entirety of the plugin-->
4. **Register Components**: Add discovered components to the launcher system

### 6. Plugin Metadata Requirements

Each plugin must provide:

- **name**: Must match the folder name
- **game**: Must match `game=` attribute in world class
- **igdb**: Must match `igdb_id=` attribute in world class  
- **authors**: Must match `author=` attribute in world class
- **requires-python**: Must be >=3.12

### 7. Entry Point Specifications

#### World Registration
```toml
"foldername.WorldClass" = "foldername.Register:WORLD_CLASS"
```
- Points to the WORLD_CLASS variable in Register.py
- WORLD_CLASS must reference the main World class that inherits from `worlds.AutoWorld.World`
- Must have `game`, `author`, and `igdb_id` class attributes

#### WebWorld Registration (Optional)
```toml
"foldername.WebWorldClass" = "foldername.Register:WEB_WORLD_CLASS"
```
- Points to WEB_WORLD_CLASS variable in Register.py
- Optional - only needed if web interface features are required

#### Client Registration (Optional)
```toml
"foldername.Client" = "foldername.Register:CLIENT_FUNCTION"
```
- Points to CLIENT_FUNCTION variable in Register.py
- Optional - only needed if the game has a custom client

### 8. Migration Strategy

#### Phase 1: Plugin System Implementation
- Implement `Plugin.py` entry point
- Create plugin discovery and loading mechanism
- Add `Register.py` files to existing worlds
- Maintain backward compatibility with existing worlds

#### Phase 2: World Migration
- Add `pyproject.toml` files to existing worlds
- Update build system to package worlds as plugins
- Test plugin loading and registration

#### Phase 3: Legacy Removal
- Remove hardcoded world imports
- Deprecate old registration system
- Update documentation and tooling

### 9. Plugin Management Features

The plugin system should support:

- **Plugin Installation**: Install plugins from local files or remote sources
- **Plugin Updates**: Check for and install plugin updates
- **Plugin Validation**: Validate plugin compatibility and requirements
- **Plugin Disabling**: Temporarily disable plugins without uninstalling
- **Plugin Dependencies**: Handle plugin-to-plugin dependencies

### 10. Configuration

Plugin system configuration should include:

- **Plugin Directories**: List of directories to scan for plugins
- **Plugin Sources**: Remote sources for plugin discovery and updates
- **Plugin Filters**: Rules for which plugins to load/ignore
- **Plugin Settings**: Per-plugin configuration options

### 11. Error Handling

The plugin system must handle:

- **Invalid Plugins**: Gracefully handle malformed or incompatible plugins
- **Missing Dependencies**: Report and handle missing plugin dependencies
- **Version Conflicts**: Resolve version conflicts between plugins
- **Loading Failures**: Provide clear error messages for plugin loading issues

### 12. Security Considerations

- **Plugin Validation**: Validate plugin integrity and authenticity
- **Sandboxing**: Consider sandboxing plugins to prevent malicious code execution
- **Permission Model**: Define what plugins can and cannot access
- **Update Security**: Secure plugin update mechanism

### 13. Performance Considerations

- **Lazy Loading**: Load plugins only when needed
- **Caching**: Cache plugin metadata and discovery results
- **Parallel Loading**: Load multiple plugins in parallel when possible
- **Memory Management**: Properly clean up unused plugin resources

## Implementation Notes

### Required Changes to Existing Code

1. **AutoWorld.py**: Modify `AutoWorldRegister` to support plugin-based registration
2. **LauncherComponents.py**: Add plugin-based component discovery
3. **World Loading**: Update world loading mechanism to use plugins
4. **Build System**: Update build system to package worlds as plugins

### Backward Compatibility

<!-- The only amount of Backward Compatibility that is necessary
is that the world structure should remain similar -->
- Maintain support for existing world structure
- Provide migration tools for converting existing worlds to plugins
- Gradual deprecation of old registration system

### Author Considerations

**Important**: The existing world authors will not be updating their worlds to match the new plugin system for years. Therefore:

- The plugin system must work with existing world structures
- Only minimal changes should be required (adding `Register.py` and `pyproject.toml`)
- All existing imports, class names, and file structures must remain functional
- The system should gracefully handle worlds that haven't been converted yet

### Testing Strategy

- Unit tests for plugin discovery and loading
- Integration tests for plugin registration and functionality
- Migration tests for converting existing worlds
- Performance tests for plugin system overhead

## Conclusion

This plugin system will provide a more modular, maintainable, and extensible architecture for MultiworldGG, allowing for easier development, distribution, and management of game worlds while maintaining backward compatibility during the transition period. The use of `Register.py` files minimizes changes to existing worlds while enabling the plugin system to work with the current author base. 