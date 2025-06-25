"""
MultiworldGG World Plugin System

This module provides the entry point for discovering, validating, and loading
game worlds in MultiworldGG.
"""

import logging
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Any
import importlib.util
import tomllib
from dataclasses import dataclass

from worlds.AutoWorld import AutoWorldRegister
from worlds.LauncherComponents import components, Component, Type

logger = logging.getLogger(__name__)


@dataclass
class WorldValidationResult:
    """Result of world validation"""
    is_valid: bool
    metadata: Dict[str, Any]
    register_data: Dict[str, Any]
    errors: List[str]


@dataclass
class WorldData:
    """Data for a loaded world"""
    name: str
    world_class: Optional[Any] = None
    web_world_class: Optional[Any] = None
    client_function: Optional[Any] = None
    metadata: Dict[str, Any] = None
    register_data: Dict[str, Any] = None


class WorldLoadError(Exception):
    """Exception raised when world loading fails"""
    pass


class DuplicateWorldError(Exception):
    """Exception raised when attempting to register a duplicate world"""
    pass


class WorldValidator:
    """Validates world metadata and structure"""
    
    def __init__(self):
        self.required_pyproject_fields = ["name", "description", "authors", "requires-python"]
        self.required_register_fields = ["PLUGIN_NAME", "GAME_NAME", "IGDB_ID", "AUTHOR", "VERSION"]
    
    def validate_world(self, world_dir: Path) -> WorldValidationResult:
        """Validate a world directory"""
        errors = []
        metadata = {}
        register_data = {}
        
        # Check if pyproject.toml exists
        pyproject_path = world_dir / "pyproject.toml"
        if not pyproject_path.exists():
            errors.append("Missing pyproject.toml")
            return WorldValidationResult(False, metadata, register_data, errors)
        
        # Validate pyproject.toml
        try:
            with open(pyproject_path, 'rb') as f:
                pyproject_data = tomllib.load(f)
            
            project_data = pyproject_data.get("project", {})
            
            # Check required fields
            for field in self.required_pyproject_fields:
                if field not in project_data:
                    errors.append(f"Missing required field: {field}")
                else:
                    metadata[field] = project_data[field]
            
            # Validate Python version requirement
            if "requires-python" in project_data:
                python_req = project_data["requires-python"]
                if not self._validate_python_version(python_req):
                    errors.append(f"requires-python '{python_req}' is insufficient (need >=3.12)")
            
            # Validate plugin name matches directory
            if "name" in project_data and project_data["name"] != world_dir.name:
                errors.append(f"Plugin name '{project_data['name']}' doesn't match directory name '{world_dir.name}'")
                
        except Exception as e:
            errors.append(f"Error parsing pyproject.toml: {e}")
        
        # Validate Register.py
        register_result = self.validate_register_py(world_dir)
        if not register_result.is_valid:
            errors.extend(register_result.errors)
        else:
            register_data = register_result.register_data
        
        is_valid = len(errors) == 0
        return WorldValidationResult(is_valid, metadata, register_data, errors)
    
    def validate_register_py(self, world_dir: Path) -> WorldValidationResult:
        """Validate Register.py file"""
        errors = []
        register_data = {}
        
        register_path = world_dir / "Register.py"
        if not register_path.exists():
            errors.append("Missing Register.py")
            return WorldValidationResult(False, {}, register_data, errors)
        
        try:
            # Import Register.py to validate variables
            spec = importlib.util.spec_from_file_location("Register", register_path)
            register_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(register_module)
            
            # Check required variables
            for field in self.required_register_fields:
                if not hasattr(register_module, field):
                    errors.append(f"Missing required variable: {field}")
                else:
                    register_data[field] = getattr(register_module, field)
            
            # Check optional variables
            optional_fields = ["WORLD_CLASS", "WEB_WORLD_CLASS", "CLIENT_FUNCTION"]
            for field in optional_fields:
                if hasattr(register_module, field):
                    register_data[field] = getattr(register_module, field)
                else:
                    register_data[field] = None
                    
        except Exception as e:
            errors.append(f"Error loading Register.py: {e}")
        
        is_valid = len(errors) == 0
        return WorldValidationResult(is_valid, {}, register_data, errors)
    
    def _validate_python_version(self, version_spec: str) -> bool:
        """Validate Python version requirement"""
        # Simple validation - check if >=3.12
        if ">=" in version_spec:
            version_part = version_spec.split(">=")[1].strip()
            if version_part.startswith("3.12"):
                return True
        return False


class WorldLoader:
    """Loads worlds from validated directories"""
    
    def __init__(self):
        self.validator = WorldValidator()
    
    def load_world(self, world_dir: Path) -> WorldData:
        """Load a single world"""
        # Validate world first
        validation_result = self.validator.validate_world(world_dir)
        if not validation_result.is_valid:
            raise WorldLoadError(f"World validation failed: {validation_result.errors}")
        
        try:
            # Import Register.py
            register_path = world_dir / "Register.py"
            spec = importlib.util.spec_from_file_location("Register", register_path)
            register_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(register_module)
            
            # Extract plugin data
            world_data = WorldData(
                name=register_module.PLUGIN_NAME,
                world_class=getattr(register_module, 'WORLD_CLASS', None),
                web_world_class=getattr(register_module, 'WEB_WORLD_CLASS', None),
                client_function=getattr(register_module, 'CLIENT_FUNCTION', None),
                metadata=validation_result.metadata,
                register_data=validation_result.register_data
            )
            
            return world_data
            
        except Exception as e:
            raise WorldLoadError(f"Failed to load world {world_dir.name}: {e}")


class WorldManager:
    """Manages world discovery, loading, and registration"""
    
    def __init__(self, world_dirs: List[str]):
        self.world_dirs = [Path(d) for d in world_dirs]
        self.loader = WorldLoader()
        self.validator = WorldValidator()
        self.loaded_worlds: Dict[str, WorldData] = {}
    
    def discover_worlds(self) -> Set[str]:
        """Discover worlds in configured directories"""
        discovered_worlds = set()
        
        for world_dir in self.world_dirs:
            if not world_dir.exists():
                continue
                
            for item in world_dir.iterdir():
                if not item.is_dir():
                    continue
                
                # Check if this directory is a plugin
                pyproject_path = item / "pyproject.toml"
                register_path = item / "Register.py"
                
                if pyproject_path.exists() and register_path.exists():
                    discovered_worlds.add(item.name)
        
        return discovered_worlds
    
    def load_all_worlds(self) -> None:
        """Load all discovered worlds"""
        discovered_worlds = self.discover_worlds()
        
        for world_name in discovered_worlds:
            try:
                # Find world directory
                world_dir = None
                for base_dir in self.world_dirs:
                    candidate = base_dir / world_name
                    if candidate.exists() and (candidate / "pyproject.toml").exists():
                        plugin_dir = candidate
                        break
                
                if plugin_dir is None:
                    logger.warning(f"Could not find world directory for {world_name}")
                    continue
                
                # Load world
                world_data = self.loader.load_world(world_dir)
                self.loaded_worlds[world_name] = world_data
                
                # Register world components
                self._register_world(world_data)
                
                logger.info(f"Successfully loaded world: {world_name}")
                
            except Exception as e:
                logger.error(f"Failed to load world {world_name}: {e}")
    
    def _register_world(self, world_data: WorldData) -> None:
        """Register world components with MultiworldGG systems"""
        # Register world class
        if world_data.world_class:
            self.register_world(world_data.world_class)
        
        # Register web world class
        if world_data.web_world_class:
            self.register_web_world(world_data.web_world_class)
        
        # Register client function
        if world_data.client_function:
            self.register_client(world_data.name, world_data.client_function)
    
    def register_world(self, world_class: Any) -> None:
        """Register world class with AutoWorld system"""
        if hasattr(world_class, 'game') and world_class.game:
            if world_class.game in AutoWorldRegister.world_types:
                raise DuplicateWorldError(f"World '{world_class.game}' is already registered")
            
            # The AutoWorldRegister metaclass should handle registration automatically
            # when the class is defined, but we can verify it's there
            if world_class.game not in AutoWorldRegister.world_types:
                logger.warning(f"World class {world_class.game} not automatically registered")
    
    def register_web_world(self, web_world_class: Any) -> None:
        """Register web world class"""
        # WebWorld registration is handled by metaclass
        if not hasattr(web_world_class, 'display_name'):
            logger.warning("WebWorld class missing display_name attribute")
    
    def register_client(self, plugin_name: str, client_function: Any) -> None:
        """Register client function with LauncherComponents"""
        # Check if component already exists
        component_name = f"{plugin_name.title()} Client"
        
        # Remove existing component if it exists
        components[:] = [c for c in components if c.display_name != component_name]
        
        # Add new component
        component = Component(
            display_name=component_name,
            func=client_function,
            component_type=Type.CLIENT
        )
        components.append(component)


def initialize_world_system(world_dirs: Optional[List[str]] = None) -> WorldManager:
    """Initialize the world system"""
    if world_dirs is None:
        # Default plugin directories
        plugin_dirs = [
            "worlds",  # Existing worlds directory
            "custom_worlds"  # Custom worlds directory
        ]
    
    world_manager = WorldManager(world_dirs)
    
    # Load all worlds
    world_manager.load_all_worlds()
    
    return world_manager


# Initialize world system when module is imported
if __name__ != "__main__":
    # Only initialize if not running as main script
    try:
        world_manager = initialize_world_system()
        logger.info(f"World system initialized with {len(world_manager.loaded_worlds)} worlds")
    except Exception as e:
        logger.error(f"Failed to initialize world system: {e}") 