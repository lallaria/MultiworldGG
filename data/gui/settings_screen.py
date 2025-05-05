from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
from kivy.metrics import dp
import logging

from kivymd.uix.screen import MDScreen
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationDrawerMenu, MDNavigationDrawerDivider
from kivymd.uix.navigationdrawer.navigationdrawer import MDNavigationDrawerItem, MDNavigationDrawerLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.hero import MDHeroTo
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivymd.uix.button import MDButton, MDButtonText
# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Define custom widgets in kv language
settings_kv = '''
SettingsNavLayout:
    size_hint_y: None
    height: Window.height-103
    settings_hero_to: settings_hero_to
    settings_nav_menu: settings_nav_menu

    MDScreenManager:
        id: settings_screen_manager
    MDNavigationDrawer:
        id: settings_nav_drawer
        radius: 0, dp(16), dp(16), 0
        drawer_type: "standard"
        anchor: "left"
        elevation: 10
        
        MDBoxLayout:
            orientation: "vertical"
            spacing: dp(8)
            padding: [dp(4), dp(4), dp(4), dp(4)]
            
            MDHeroTo:
                id: settings_hero_to
                size_hint: None,None
                size: dp(256), dp(161)
                pos_hint: {"center_x": 0.5, "top": 1}
                FitImage:
                    source: "data/logo_bg.png"
                    size_hint: None,None
                    size: dp(256), dp(161)
                    pos_hint: {"center_x": 0.5, "top": 1}
            
            NavDrawerMenu:
                id: settings_nav_menu


<NavDrawerMenu>:
    orientation: "vertical"

<NavDrawerLabel>:
    font_style: "Title"
    bold: True
    padding: [0, dp(16), 0, 0]
    theme_text_color: "Custom"
    text_color: app.theme_cls.primaryColor

<NavDrawerItem>:
    MDNavigationDrawerItemLeadingIcon:
        icon: root.icon
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.onPrimaryContainerColor
    MDNavigationDrawerItemText:
        text: root.text
        theme_text_color: "Custom"
        text_color: app.theme_cls.onSecondaryContainerColor
    MDNavigationDrawerItemTrailingText:
        text: root.trailing_text
        theme_text_color: "Custom"
        text_color: app.theme_cls.onTertiaryContainerColor
'''

class SettingsNavLayout(MDNavigationLayout):
    settings_hero_to: ObjectProperty
    settings_nav_menu: ObjectProperty

class NavDrawerMenu(MDNavigationDrawerMenu):
    menu_label = StringProperty("")

    def on_start(self):
        self.ids.menu.size_hint_x = None
        self.ids.menu.width = self.width - dp(8)

class NavDrawerLabel(MDNavigationDrawerLabel):
    pass

class NavDrawerItem(MDNavigationDrawerItem):
    screen = ObjectProperty(None)
    icon = StringProperty("")
    text = StringProperty("")
    trailing_text = StringProperty("")


class SettingsScreen(MDScreen):
    '''
    Main settings screen to call from the application
    '''
    settings_hero_to: ObjectProperty
    heroes_to = []
    settings_nav_drawer: ObjectProperty
    settings_screen_manager: MDScreenManager
    nav_layout: SettingsNavLayout
    nav_menu: NavDrawerMenu

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.debug("Initializing SettingsScreen")
        self.name = "settings"
        self.nav_layout = Builder.load_string(settings_kv)
        logger.debug(f"Loaded nav_layout: {self.nav_layout}")
        
        self.settings_nav_drawer = self.nav_layout.ids.settings_nav_drawer
        self.settings_nav_drawer.type = "standard"
        logger.debug(f"Retrieved nav_drawer: {self.settings_nav_drawer}")
        
        self.settings_screen_manager = self.nav_layout.ids.settings_screen_manager
        self.settings_screen_manager.add_widget(SettingsScreenSection(name="NavBar", title="Navigation Bar", nav_drawer=self.settings_nav_drawer))
        self.settings_screen_manager.current = "NavBar"
        logger.debug(f"Retrieved screen_manager: {self.settings_screen_manager}")
        
        self.settings_hero_to = self.nav_layout.settings_hero_to
        self.add_widget(self.nav_layout)
        self.heroes_to.append(self.settings_hero_to)
        
        logger.debug("Added nav_layout to screen")
        
        # Set up the navigation menu after everything else is initialized
        Clock.schedule_once(self.setup_navigation_menu)
    
    def on_pre_enter(self, *args):
        logger.debug("SettingsScreen on_pre_enter called")
        logger.debug(f"Current screen manager screens: {self.settings_screen_manager.screens}")
        logger.debug(f"Current screen manager current: {self.settings_screen_manager.current}")
        super().on_pre_enter(*args)
    
    def setup_navigation_menu(self, *args):
        """Set up the navigation menu with all its items."""
        self.nav_menu = self.nav_layout.settings_nav_menu
        self.nav_menu.on_start()
        
        # Add Interface section
        self.nav_menu.add_widget(NavDrawerLabel(
            text="Interface"
        ))
        
        interface_items = [
            ("Display", "monitor", None),
            ("Animation", "animation", None),
            ("Transition", "transition", None),
            ("Menu", "menu", None)
        ]
        for text, icon, screen in interface_items:
            self.nav_menu.add_widget(NavDrawerItem(
                icon=icon,
                text=text,
                screen=screen
            ))
        
        # Add divider
        self.nav_menu.add_widget(MDNavigationDrawerDivider())
        
        # Add Theming section
        self.nav_menu.add_widget(NavDrawerLabel(
            text="Theming"
        ))
        
        theming_items = [
            ("Theme", "palette", None),
            ("Palette", "palette-swatch", None),
            ("Custom Colors", "color-helper", None),
            ("Font", "format-font", None)
        ]
        for text, icon, screen in theming_items:
            self.nav_menu.add_widget(NavDrawerItem(
                icon=icon,
                text=text,
                screen=screen
            ))
        
        # Add divider
        self.nav_menu.add_widget(MDNavigationDrawerDivider())
        
        # Add Connection section
        self.nav_menu.add_widget(NavDrawerLabel(
            text="Connection"
        ))
        
        connection_items = [
            ("Server", "server", None),
            ("Timeout", "clock", None),
            ("Authentication", "shield-account", None),
            ("Reconnection", "reload", None)
        ]
        for text, icon, screen in connection_items:
            self.nav_menu.add_widget(NavDrawerItem(
                icon=icon,
                text=text,
                screen=screen
            ))

class SettingsScreenSection(MDScreen):
    '''
    Generic settings section screen
    For use only on the settings screen, not as a standalone screen
    '''
    name = StringProperty("")
    title = StringProperty("")
    nav_drawer = ObjectProperty(None)
    def __init__(self, name, title, nav_drawer, **kwargs):
        super().__init__(**kwargs)
        logger.debug(f"Initializing SettingsScreenSection: {name}")
        self.nav_drawer = nav_drawer
        self.name = name
        self.title = title
        
        # Create a button to toggle the drawer
        toggle_button = MDButton(
            MDButtonText(text=self.title),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        toggle_button.bind(on_release=lambda x: self.nav_drawer.set_state("toggle"))
        self.add_widget(toggle_button)
        
    def on_pre_enter(self, *args):
        logger.debug(f"SettingsScreenSection {self.name} on_pre_enter called")
        logger.debug(f"Children: {self.children}")
        super().on_pre_enter(*args)