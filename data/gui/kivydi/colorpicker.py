__all__ = ("MWColorPicker",)
from kivy.properties import ColorProperty, StringProperty, ObjectProperty
from PIL import ImageGrab
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.fitimage import FitImage
from kivy.lang import Builder
from kivymd.theming import ThemableBehavior
from kivy.utils import get_hex_from_color, get_color_from_hex
import re

color_info_kv = """
<ColorInfoLayout>:
    select_color_button: select_color_button
    color_text: color_text
    cols: 2
    rows: 2
    MDLabel:
        text: "Color:"
    MDTextField:
        id: color_text
        mode: "outlined"
        md_bg_color: app.theme_cls.surfaceContainerLowestColor
        theme_text_color: "Custom"
        text_color: root.color
        text: root.hex_color
        on_text: root.on_text_field_change(self.text)
        MDTextFieldLeadingIcon:
            icon: "palette"
        MDTextFieldHintText:
            text: "Hex Color"
        MDTextFieldHelperText:
            text: "Hex Color"
            mode: "persistent"
    Widget:
        canvas.before:
            Color:
                rgba: root.color
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [10, 10, 10, 10]
        size: 50, 50
    MDButton:
        id: select_color_button
        MDButtonText:
            theme_text_color: "Primary"
            text: "Select Color"
"""

# Load KV string once at module level
Builder.load_string(color_info_kv)

class ColorInfoLayout(MDGridLayout, ThemableBehavior):
    color = ColorProperty([0, 0, 0, 0])
    hex_color = StringProperty("#000000")
    select_color_button = ObjectProperty(None)
    color_text = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(color=self._on_color_change)
        self.bind(hex_color=self._on_hex_color_change)

    def on_parent(self, *args):
        if self.parent:
            self.color = self.parent.color
            self.hex_color = self.parent.hex_color

    def _on_color_change(self, instance, value):
        # Convert color to hex and strip alpha
        hex_color = get_hex_from_color(value).lstrip('#')[:6]
        if self.color_text:
            self.color_text.text_color = value
        # Update hex_color through the parent MWColorPicker
        if hasattr(self.parent, 'hex_color'):
            self.parent.hex_color = hex_color
            # Also update our own hex_color to keep KV in sync
            self.hex_color = hex_color

    def _on_hex_color_change(self, instance, value):
        if self.color_text:
            self.color_text.text = value

    def on_text_field_change(self, text):
        # Validate hex color format
        hex_pattern = r'^(?:#)?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$'
        if re.match(hex_pattern, text):
            try:
                # Update hex_color through the parent MWColorPicker
                if hasattr(self.parent, 'hex_color'):
                    self.parent.hex_color = text.lstrip('#')
                    # Also update our own hex_color to keep KV in sync
                    self.hex_color = text.lstrip('#')
            except Exception as e:
                print(f"Error converting hex color: {e}")


class MWColorPicker(MDBoxLayout):
    orientation = "horizontal"
    color = ColorProperty([0, 0, 0, 0])
    hex_color = StringProperty("#000000")
    image = ObjectProperty(None)

    def __init__(self, layout, **kwargs):
        super().__init__(**kwargs)
        self.parent_layout = layout
        self.size_hint = (1, None)
        self.height = 200  # Set a fixed height for the color picker
        
        # Create and configure the image
        self.image = FitImage(source="data/gui/data/palette.png", fit_mode='scale-down')
        self.image.bind(on_touch_down=self.on_touch_down)
        
        # Create and configure the info layout
        self.info_layout = ColorInfoLayout()
        
        self.add_widget(self.info_layout)
        self.add_widget(self.image)
        self.bind(color=self._on_color_change)
        self.bind(hex_color=self._on_hex_color_change)

    def _on_color_change(self, instance, value):
        self.info_layout.color = value

    def _on_hex_color_change(self, instance, value):
        # Update the color based on the new hex value
        try:
            if not value.startswith('#'):
                value = '#' + value
            color = get_color_from_hex(value)
            self.color = (color[0], color[1], color[2], 1)  # Force alpha to 1
            # Update the info layout's hex_color to keep KV in sync
            self.info_layout.hex_color = value.lstrip('#')
        except Exception as e:
            print(f"Error converting hex color: {e}")

    def on_touch_down(self, instance, touch):
        if self.image.collide_point(touch.x, touch.y):
            touch.grab(self.image)         
            # Get the color at the touched point
            try:
                pixel = ImageGrab.grab().load()[touch.x, touch.y]
                self.color = (pixel[0]/255, pixel[1]/255, pixel[2]/255, 1)
            except Exception as e:
                print(f"Error getting color: {e}, Color: {self.color}")
            return True
