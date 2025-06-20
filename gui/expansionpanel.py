from kivy.animation import Animation
from kivy.properties import ObjectProperty, BooleanProperty, NumericProperty, StringProperty
from kivy.metrics import dp
from kivy.uix.widget import Widget

from kivymd.uix.behaviors import RotateBehavior
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelContent, MDExpansionPanelHeader

class OpacityExpansionPanel(MDExpansionPanel):
    """
    A custom expansion panel that makes content visible by changing opacity
    rather than adding/removing widgets.
    
    The content is always present but initially transparent and with height=0.
    """
    
    content_opacity = NumericProperty(0)
    content_height = NumericProperty(0)
    expanded_height = NumericProperty(dp(200))  # Default height when expanded
    is_open = BooleanProperty(False)
    content = ObjectProperty(None)  # Store content widget reference properly
    animation_duration = NumericProperty(0.2)  # Unified animation duration
    animation_transition = StringProperty("out_expo")  # Unified transition
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.opening_transition = self.animation_transition
        self.closing_transition = self.animation_transition
        self.opening_time = self.animation_duration
        self.closing_time = self.animation_duration
        # Ensure content is already added but invisible
        self._content_added = True
        self._bound_children = set()
    
    def add_widget(self, widget, *args, **kwargs):
        """Override to handle content widget differently"""
        if isinstance(widget, MDExpansionPanelContent):
            widget.opacity = self.content_opacity
            widget.size_hint_y = None
            widget.height = self.content_height
            super().add_widget(widget, *args, **kwargs)
            # Store reference to content for future animations
            self.content = widget
            
            # Bind to size changes of content's children to update expanded_height
            self._bind_children_height()
            # Bind to children changes to catch newly added widgets
            widget.bind(children=self._on_children_changed)
        else:
            super().add_widget(widget, *args, **kwargs)
    
    def _on_children_changed(self, instance, children):
        """Called when content's children change"""
        self._bind_children_height()
        
    def _bind_children_height(self):
        """Bind height of all content children"""
        if not self.content:
            return
            
        # Ensure _bound_children is initialized
        if not hasattr(self, '_bound_children'):
            self._bound_children = set()
            
        for child in self.content.children:
            # Only bind if not already bound
            if child not in self._bound_children:
                child.bind(height=self._update_expanded_height)
                self._bound_children.add(child)
        
        # Update height immediately
        self._update_expanded_height()
    
    def remove_widget(self, widget):
        """Override to handle unbinding"""
        if hasattr(self, '_bound_children') and widget in self._bound_children:
            widget.unbind(height=self._update_expanded_height)
            self._bound_children.remove(widget)
        
        if widget == self.content:
            self.content = None
            
        super().remove_widget(widget)
    
    def _update_expanded_height(self, *args):
        """Update expanded_height based on content's natural size"""
        if not hasattr(self, 'content') or not self.content:
            return
            
        if hasattr(self.content, 'minimum_height'):
            # Use minimum_height if available
            self.expanded_height = self.content.minimum_height
        else:
            # Otherwise calculate based on children
            try:
                total_height = sum(c.height for c in self.content.children if hasattr(c, 'height'))
                if total_height > 0:
                    self.expanded_height = total_height + dp(20)  # Add some padding
            except (AttributeError, TypeError):
                # Fallback if content.children is not iterable or has issues
                pass
    
    def open(self):
        """Animate the content to visible state"""
        if self.is_open:
            return
        
        # Update expanded_height before animating
        self._update_expanded_height()
            
        # First set chevron to indicate open state
        if hasattr(self, '_chevron'):
            self.set_chevron_down(self._chevron)
            
        # Then animate content visibility
        content_anim = Animation(
            content_opacity=1,
            content_height=self.expanded_height,
            d=self.opening_time,
            t=self.opening_transition
        )
        
        content_anim.start(self)
        self.is_open = True
    
    def close(self):
        """Animate the content to hidden state"""
        if not self.is_open:
            return
        
        # First set chevron to indicate closed state
        if hasattr(self, '_chevron'):
            self.set_chevron_up(self._chevron)
            
        # Then animate content visibility
        content_anim = Animation(
            content_opacity=0,
            content_height=0,
            d=self.closing_time,
            t=self.closing_transition
        )
        
        content_anim.start(self)
        self.is_open = False
    
    def on_content_opacity(self, instance, value):
        """Called when content_opacity property changes"""
        if hasattr(self, 'content') and self.content:
            self.content.opacity = value
    
    def on_content_height(self, instance, value):
        """Called when content_height property changes"""
        if hasattr(self, 'content') and self.content:
            self.content.height = value
    
    def tap_expansion_chevron(self, panel, chevron):
        """Handle tapping the chevron button"""
        # Store chevron reference for later use
        panel._chevron = chevron
        
        # Then open/close panel with padding animation
        if not panel.is_open:
            Animation(
                padding=[0, dp(12), 0, dp(12)],
                d=panel.opening_time,
                t=panel.opening_transition
            ).start(panel)
            panel.open()
        else:
            Animation(
                padding=[0, 0, 0, 0],
                d=panel.closing_time,
                t=panel.closing_transition
            ).start(panel)
            panel.close()
    
    def set_chevron_down(self, instance):
        """Rotate the chevron to pointing down"""
        Animation(rotate_value_angle=90, d=self.animation_duration).start(instance)
    
    def set_chevron_up(self, instance):
        """Rotate the chevron back to pointing right"""
        Animation(rotate_value_angle=0, d=self.animation_duration).start(instance)
