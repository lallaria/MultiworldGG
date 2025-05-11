from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, ColorProperty, BooleanProperty, NumericProperty
from kivy.metrics import dp
from kivy.utils import get_color_from_hex, get_hex_from_color
import logging
import os
import sys
import io
from dataclasses import fields
from kivy.clock import Clock

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.slider import MDSlider
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.textfield import MDTextField
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogSupportingText, MDDialogContentContainer, MDDialogButtonContainer 

from mw_theme import THEME_OPTIONS, MarkupTagsTheme
from textconsole import TextConsole
from kivydi.colorpicker import MWColorPicker
# Set up logging
log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "logs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "settings_components.log")

# Remove any existing handlers
root_logger = logging.getLogger()
for handler in root_logger.handlers[:]:
    root_logger.removeHandler(handler)
    handler.close()

# Create a custom stream handler that won't cause recursion
class CustomStreamHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            msg = self.format(record)
            stream = self.stream
            stream.write(msg + self.terminator)
            self.flush()
        except Exception:
            self.handleError(record)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, mode='w'),
        CustomStreamHandler(sys.stdout)  # Use stdout instead of stderr
    ]
)
logger = logging.getLogger(__name__)

# Test log message
logger.debug("Settings components logging initialized")
logger.info("Settings components logging initialized")
logger.warning("Settings components logging initialized")
logger.error("Settings components logging initialized")

# KV string for settings components
settings_components_kv = '''
<SettingsSection>:
    orientation: "vertical"
    padding: [dp(16), dp(8)]
    spacing: dp(8)
    size_hint_y: None
    height: self.minimum_height

<LabeledSwitch>:
    orientation: "horizontal"
    size_hint_y: None
    height: dp(48)
    MDLabel:
        theme_text_color: "Secondary"
        text: root.text
        size_hint_x: 0.7
    MDSwitch:
        id: switch
        on_active: root.on_switch(root, self.active) if root.on_switch else None

<LabeledDropdown>:
    orientation: "horizontal"
    size_hint_y: None
    height: dp(48)
    MDLabel:
        theme_text_color: "Secondary"
        text: root.text
        size_hint_x: 0.7
    MDButton:
        id: dropdown_button
        text: root.current_item
        on_release: root.show_menu()

<ColorBox>:
    orientation: "horizontal"
    size_hint_y: None
    height: dp(48)
    MDLabel:
        theme_text_color: "Custom"
        text_color: root.color
        text: root.text
        size_hint_x: 0.7
    
    ColorPreviewBox:
        id: color_preview_box
        index: root.index
        color_attr: root.color_attr
        color: root.color

<ColorPreviewBox>:
    orientation: "horizontal"
    size_hint_y: None
    height: dp(48)
    MDButton:
        style: "filled"
        size: dp(32), dp(32)
        theme_bg_color: "Custom"
        md_bg_color: root.color
        on_release: root.open_color_picker(root.color, root.index, root.color_attr, self.pos)

<SettingsScrollBox>:
    MDBoxLayout:
        id: layout
        orientation: "vertical"
        padding: [dp(16), dp(8)]
        spacing: dp(8)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"top": 1}
'''

Builder.load_string(settings_components_kv)

class SettingsSection(MDBoxLayout):
    """Base class for settings sections"""
    name = StringProperty("")
    title = StringProperty("")

class LabeledSwitch(MDBoxLayout):
    """Switch with a label"""
    text = StringProperty("")
    on_switch = ObjectProperty(None)

class LabeledDropdown(MDBoxLayout):
    """Dropdown with a label"""
    text = StringProperty("")
    items = ObjectProperty([])
    current_item = StringProperty("")
    on_select = ObjectProperty(None)

    def show_menu(self):
        menu_items = [
            {
                "text": item, 
                "theme_text_color": "Secondary",
                "on_release": lambda x=item: self.select_item(x),
            } for item in self.items
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.dropdown_button,
            items=menu_items,
            width_mult=4,
        )
        self.menu.open()

    def select_item(self, item):
        self.current_item = item
        if self.on_select:
            self.on_select(item)
        self.menu.dismiss()

class ColorPreviewBox(MDBoxLayout):
    """Box showing a color preview"""
    color = ColorProperty([0,0,0,0])
    color_attr = ObjectProperty(None)
    color_attr_old = ObjectProperty(None)
    index = NumericProperty(0)
    text = StringProperty("")

    def reset(self):
        self.color_attr = self.color_attr_old
        self.color_picker.dismiss()
    
    def apply(self):
        self.color_picker.dismiss()

    def open_color_picker(self, color, index, color_attr, pos):
        # Create a new color picker each time to avoid binding issues
        self.color_attr = color_attr
        self.color_attr_old = color_attr
        self.index = index
        self.text = self.parent.text
        self.color_picker = MWColorPicker(self)
        
        def on_color(instance, value):
            try:
                hex_color = instance.hex_color#.lstrip('#')[:-2]
                # Update the appropriate color in the list based on theme style
                self.color_attr[self.index] = hex_color
                #Clock.schedule_once(lambda dt: self.app.theme_cls.refresh(), 0.5)
            except Exception as e:
                logger.error(f"Error updating color: {e}", exc_info=True)
        
        # Bind to the color property
        self.color_picker.bind(color=on_color)
        
        # Create popup with color picker
        dialog = MDDialog(
            MDDialogHeadlineText(
                text="Choose Color"
            ),
            MDDialogSupportingText(
                text=self.text
            ),
            MDDialogContentContainer(
                self.color_picker
            )
        )

        
        # Get current color and set it
        try:
            current_color = self.color
            self.color_picker.color = current_color
        except Exception as e:
            logger.error(f"Error setting initial color: {e}", exc_info=True)
            self.color_picker.color = (1, 1, 1, 1)  # Default to white if there's an error
        
        # Show the popup
        dialog.open()

class ColorBox(MDBoxLayout):
    """Box showing a color preview"""
    text = StringProperty("")
    color = ColorProperty([0,0,0,0])
    color_attr = ObjectProperty(None)
    index = NumericProperty(0)

    def __init__(self, text, color, color_attr, index, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.color = color
        self.color_attr = color_attr
        self.index = index

class SettingsScrollBox(MDScrollView):
    """Scrollable box for settings"""
    layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.debug("Initializing SettingsScrollBox")
        self.layout = self.ids.layout
        logger.debug(f"Retrieved layout: {self.layout}")

class ConnectionSettings(SettingsScrollBox):
    """Connection settings section"""
    def __init__(self, **kwargs):
        logger.debug("Initializing ConnectionSettings")
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        logger.debug("Got running app")
        
        # Profile section
        logger.debug("Creating profile section")
        profile_section = SettingsSection(name="profile_settings", title="Profile")
        
        # Alias
        logger.debug("Adding alias field")
        alias_box = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(48))
        alias_box.add_widget(MDLabel(text="Alias", theme_text_color="Primary", size_hint_x=0.7))
        alias_input = MDTextField(
            text=self.app.app_config.get('client', 'alias', fallback=''),
        )
        alias_box.add_widget(alias_input)
        profile_section.add_widget(alias_box)
        
        # Pronouns
        logger.debug("Adding pronouns field")
        pronouns_box = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(48))
        pronouns_box.add_widget(MDLabel(text="Pronouns", theme_text_color="Primary", size_hint_x=0.7))
        pronouns_input = MDTextField(
            text=self.app.app_config.get('client', 'pronouns', fallback=''),
        )
        pronouns_box.add_widget(pronouns_input)
        profile_section.add_widget(pronouns_box)
        
        # Status toggles
        logger.debug("Creating status section")
        status_section = SettingsSection(name="status_settings", title="Status")
        status_section.add_widget(LabeledSwitch(
            text="In Call",
            on_switch=self.toggle_in_call
        ))
        status_section.add_widget(LabeledSwitch(
            text="In BK",
            on_switch=self.toggle_in_bk
        ))
        
        # Host settings
        logger.debug("Creating host settings section")
        host_section = SettingsSection(name="multiworld_settings", title="Multiworld Settings")
        
        # Hostname & Port
        logger.debug("Adding hostname field")
        hostname_box = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(48))
        hostname_box.add_widget(MDLabel(text="Hostname", theme_text_color="Primary"))
        hostname_input = MDTextField(
            text=self.app.app_config.get('client', 'hostname', fallback='multiworld.gg'),
        )
        hostname_box.add_widget(hostname_input)
        hostname_box = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(48))
        hostname_box.add_widget(MDLabel(text="Port", theme_text_color="Primary", size_hint_x=0.7))
        port_input = MDTextField(
            text=self.app.app_config.get('client', 'port', fallback='38281'),
        )
        hostname_box.add_widget(port_input)
        host_section.add_widget(hostname_box)
 
        # Player Slot
        logger.debug("Adding player slot field")
        slot_box = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(48))
        slot_box.add_widget(MDLabel(text="Player Slot", theme_text_color="Primary", size_hint_x=0.7))
        slot_input = MDTextField(
            text=self.app.app_config.get('client', 'slot', fallback=''),
        )
        slot_box.add_widget(slot_input)
        slot_box.add_widget(MDLabel(text="Password", theme_text_color="Primary", size_hint_x=0.7))
        slot_input = MDTextField(
            text='',
            password=True,
        )
        slot_box.add_widget(slot_input)
        host_section.add_widget(slot_box)
        
        # Admin Password
        logger.debug("Adding admin password field")
        admin_box = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(48))
        admin_box.add_widget(MDLabel(text="Admin Password", theme_text_color="Primary", size_hint_x=0.7))
        admin_input = MDTextField(
            text="********" if self.app.app_config.get('client', 'admin_password', fallback='') else '',
            hint_text="Login for the multiworld server to run admin commands",
            password=True
        )
        admin_box.add_widget(admin_input)
        host_section.add_widget(admin_box)
        
        # Add all sections to the layout
        logger.debug("Adding all sections to layout")
        self.layout.add_widget(profile_section)
        self.layout.add_widget(status_section)
        self.layout.add_widget(host_section)
        logger.debug("Finished initializing ConnectionSettings")
    
    def toggle_in_call(self, instance, value):
        try:
            logger.debug(f"Toggling in_call to {value}")
            self.app.app_config.set('client', 'in_call', str(value))
            self.app.app_config.write()
            logger.debug("In call toggle complete")
        except Exception as e:
            logger.error(f"Error in toggle_in_call: {e}", exc_info=True)
    
    def toggle_in_bk(self, instance, value):
        try:
            logger.debug(f"Toggling in_bk to {value}")
            self.app.app_config.set('client', 'in_bk', str(value))
            self.app.app_config.write()
            logger.debug("In BK toggle complete")
        except Exception as e:
            logger.error(f"Error in toggle_in_bk: {e}", exc_info=True)

class ThemingSettings(SettingsScrollBox):
    """Theming settings section"""
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.theme_mw = self.app.theme_mw

        # Theme style section
        theme_style_section = SettingsSection(name="theme_style_settings", title="Theme Style")
        theme_styles = ["Light", "Dark"]
        current_style = self.app.theme_cls.theme_style
        theme_style_section.add_widget(LabeledDropdown(
            text="Theme Style",
            items=theme_styles,
            current_item=current_style,
            on_select=self.set_theme_style
        ))
        
        # Palette section
        palette_section = SettingsSection(name="palette_settings", title="Primary Palette")
        current_style = self.app.theme_cls.theme_style
        palettes = [color[0] for color in THEME_OPTIONS[current_style]]
        current_palette = self.app.theme_cls.primary_palette
        palette_section.add_widget(LabeledDropdown(
            text="Primary Color",
            items=palettes,
            current_item=current_palette,
            on_select=self.set_primary_palette
        ))
        
        # Custom colors section
        custom_colors_section = SettingsSection(name="custom_colors_settings", title="Custom Color Settings")
        app_style = {"Light": 0, "Dark": 1}
        for f in fields(self.theme_mw.markup_tags_theme):
            color_attr = getattr(self.theme_mw.markup_tags_theme, f.name)
            color_box = ColorBox(text=f.name, 
                                 color=get_color_from_hex(color_attr[app_style[current_style]]), 
                                 color_attr=color_attr, 
                                 index=app_style[current_style])
            custom_colors_section.add_widget(color_box)

        # Font size section
        font_section = SettingsSection(name="font_settings", title="Font Settings")
        font_sizes = ["Small", "Medium", "Large", "Extra Large"]
        font_section.add_widget(LabeledDropdown(
            text="Font Size",
            items=font_sizes,
            current_item="Medium",
            on_select=self.set_font_size
        ))
        
        # Add all sections to the layout
        self.layout.add_widget(theme_style_section)
        self.layout.add_widget(palette_section)
        self.layout.add_widget(custom_colors_section)
        self.layout.add_widget(font_section)
    
    def set_theme_style(self, style):
        self.app.theme_cls.theme_style = style
        self.app.app_config.set('client', 'theme_style', style)
        self.app.app_config.write()
        # Schedule a refresh after the change
        Clock.schedule_once(lambda dt: self.app.theme_cls.refresh(), 0.5)
    
    def set_primary_palette(self, palette):
        self.app.theme_cls.primary_palette = palette
        self.app.app_config.set('client', 'primary_palette', palette)
        self.app.app_config.write()
        # Schedule a refresh after the change
        Clock.schedule_once(lambda dt: self.app.theme_cls.refresh(), 0.5)
    
    def set_font_size(self, size):
        sizes = {"Small": 0.8, "Medium": 1.0, "Large": 1.2, "Extra Large": 1.5}
        scale_factor = sizes.get(size, 1.0)
        self.app.app_config.set('client', 'font_scale', str(scale_factor))
        self.app.app_config.write()

class InterfaceSettings(SettingsScrollBox):
    """Interface settings section"""
    def __init__(self, **kwargs):
        logger.debug("Initializing InterfaceSettings")
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        logger.debug("Got running app")
        
        # Display section
        logger.debug("Creating display section")
        display_section = SettingsSection(name="display_settings", title="Display")
        display_section.add_widget(LabeledSwitch(
            text="Fullscreen",
            theme_text_color="Secondary",
            on_switch=self.toggle_fullscreen
        ))
        logger.debug("Added fullscreen switch")
        
        # Layout section
        logger.debug("Creating layout section")
        layout_section = SettingsSection(name="layout_settings", title="Layout")
        layout_section.add_widget(LabeledSwitch(
            text="Compact Mode",
            theme_text_color="Secondary",
            on_switch=self.toggle_compact_mode
        ))
        logger.debug("Added compact mode switch")
        
        # Add all sections to the layout
        logger.debug("Adding sections to layout")
        self.layout.add_widget(display_section)
        self.layout.add_widget(layout_section)
        logger.debug("Finished initializing InterfaceSettings")
    
    def toggle_fullscreen(self, instance, value):
        try:
            logger.debug(f"Toggling fullscreen to {value}")
            self.app.config.set('graphics', 'fullscreen', str(value))
            self.app.config.write()
            logger.debug("Fullscreen toggle complete")
        except Exception as e:
            logger.error(f"Error in toggle_fullscreen: {e}", exc_info=True)
    
    def toggle_compact_mode(self, instance, value):
        try:
            logger.debug(f"Toggling compact mode to {value}")
            self.app.app_config.set('client', 'compact_mode', str(value))
            self.app.app_config.write()
            logger.debug("Compact mode toggle complete")
        except Exception as e:
            logger.error(f"Error in toggle_compact_mode: {e}", exc_info=True) 