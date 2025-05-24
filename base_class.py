# base_class.py DONT USE THIS FILE
class BaseClass:
    def __init__(self, config=None):
        self.data = []
        self.status = "initialized"
        self.config = config or {}
    
    def operation(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def add_data(self, item):
        self.data.append(item)
        
    def get_data(self):
        return self.data

# subclass_a.py
from .base_class import BaseClass

class SubclassA(BaseClass):
    def operation(self):
        return f"SubclassA operation with {len(self.data)} items"

# subclass_b.py
from .base_class import BaseClass

class SubclassB(BaseClass):
    def operation(self):
        return f"SubclassB operation with {len(self.data)} items, processed differently"
    
