from __future__ import annotations
__all__ = ['LaunchFactory', 'Launch']
from typing import Dict, Type, TypeVar, Optional, Any
import importlib
import inspect
import pkgutil

T = TypeVar('T')

class LaunchFactory:
    """
    A singleton factory that manages creation and switching of bonds (Contexts) 
    from a base class while the application is running
    """
    _instance = None
    _registry: Dict[str, Type] = {}
    _active_instance = None
    _base_instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LaunchFactory, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self._initialized = True
    
    @classmethod
    def register(cls, name: str, class_type: Type[T]) -> None:
        """Register a class with the factory"""
        cls._registry[name] = class_type
    
    @classmethod
    def get_class(cls, name: str) -> Optional[Type[T]]:
        """Get a class by name"""
        return cls._registry.get(name)
    
    @classmethod
    def create(cls, name: str, *args, **kwargs) -> Optional[T]:
        """Create an instance of a registered class"""
        class_type = cls.get_class(name)
        if class_type:
            return class_type(*args, **kwargs)
        return None
    
    @classmethod
    def get_registered_classes(cls) -> Dict[str, Type]:
        """Get all registered classes"""
        return cls._registry.copy()
    
    @classmethod
    def register_all_subclasses(cls, base_class: Type[T], package_name: str = None) -> None:
        """
        Automatically register all subclasses of a given base class
        Optionally provide a package name to search for modules
        """
        # Register direct subclasses
        for subclass in base_class.__subclasses__():
            cls.register(subclass.__name__, subclass)
            
            # Also register indirect subclasses
            for indirect_subclass in subclass.__subclasses__():
                cls.register(indirect_subclass.__name__, indirect_subclass)
        
        # If package name is provided, we can search for other modules
        if package_name:
            try:
                package = importlib.import_module(package_name)
                package_path = package.__path__
                
                # Find all modules in package
                for _, module_name, _ in pkgutil.iter_modules(package_path):
                    full_module_name = f"{package_name}.{module_name}"
                    try:
                        module = importlib.import_module(full_module_name)
                        
                        # Find all classes in module that are subclasses of base_class
                        for name, obj in inspect.getmembers(module):
                            if (inspect.isclass(obj) and 
                                issubclass(obj, base_class) and 
                                obj != base_class):
                                cls.register(obj.__name__, obj)
                    except ImportError:
                        pass
            except ImportError:
                pass
    
    @classmethod
    def set_base_instance(cls, instance) -> None:
        """
        Set the base instance that is already running
        This will be used as a reference for state transfer
        """
        cls._base_instance = instance
        if cls._active_instance is None:
            cls._active_instance = instance
    
    @classmethod
    def get_active_instance(cls):
        """Get the currently active instance"""
        return cls._active_instance
    
    @classmethod
    def switch_implementation(cls, name: str, *args, **kwargs):
        """
        Switch to a different implementation while preserving state from the current instance
        Returns the new active instance
        """
        if cls._base_instance is None:
            raise RuntimeError("Base instance must be set before switching implementations")
        
        class_type = cls.get_class(name)
        if not class_type:
            raise ValueError(f"Implementation '{name}' not found")
        
        # Create new instance
        new_instance = class_type(*args, **kwargs)
        
        # Transfer state from current active instance to new instance
        cls._transfer_state(cls._active_instance, new_instance)
        
        # Update active instance
        cls._active_instance = new_instance
        
        return new_instance
    
    @classmethod
    def _transfer_state(cls, source, target):
        """
        Transfer state from source instance to target instance
        Override this method for custom state transfer logic
        """
        # Default implementation: copy all public attributes
        for attr_name in dir(source):
            # Skip private attributes, methods, and callables
            if (not attr_name.startswith('_') and
                not callable(getattr(source, attr_name)) and
                not attr_name in ['__class__', '__dict__', '__weakref__']):
                try:
                    setattr(target, attr_name, getattr(source, attr_name))
                except (AttributeError, TypeError):
                    # Skip attributes that can't be set
                    pass

class Launch:
    '''MWGG Launch class'''
    def __init__(self):
        self.status = "initialized"
        self.config = {}

    def launch(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement this method")

