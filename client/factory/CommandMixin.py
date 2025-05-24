from __future__ import annotations
from typing import Dict, Type, TypeVar, Optional, Any
import importlib
import inspect
import pkgutil


class CommandMixin:
    '''Mixin for CommandProcessor'''
    def add_command(self, *args, **kwargs):
        '''Add a command to the CommandProcessor'''
        pass

    def override_command(self, *args, **kwargs):
        '''Override a command in the CommandProcessor'''
        if hasattr(super(), 'base_method'):
            return super().base_method(*args, **kwargs)
