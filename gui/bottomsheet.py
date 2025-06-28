from __future__ import annotations

__all__ = (
    "MainBottomSheet",
    "BottomChipLayout",
    "BottomChip",
    "UserInput",
)
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDButton
from kivymd.uix.chip.chip import MDChip
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.bottomsheet import MDBottomSheet
from kivymd.uix.tab.tab import MDTabsPrimary, MDTabsItem, MDTabsItemText, MDTabsCarousel
from kivymd.uix.textfield.textfield import MDTextField
from .kivydi import CONSOLE_ACTIONS, LAUNCHER_ACTIONS

Builder.load_string('''
<MainBottomSheet>:
    id: main_bottom_sheet
    size_hint_y: None
    height: "180dp"
    md_bg_color: app.theme_cls.surfaceContainerLowColor

    MDBoxLayout:
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .7}
        size_hint_x: 0.8

<BottomChip>:
    id: ObjectProperty()
    type: "assist"
    icon: ""
    text: ""
    MDChipLeadingIcon:
        icon: root.icon
    MDChipText:
        text: root.text

<BottomChipLayout>:
    rows: 2
    id: chip_box
    spacing: "12dp"
    width: app.bottom_sheet.width
    height: 80
    pos: app.bottom_sheet.x, 0
    size_hint: None, None
    padding: 10,0,10,10

''')

class UserInput(MDTextField):
    '''Text field for user input
    
    Console, hint, and admin will 
    all go here.'''
    input_type = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_font_name = "Custom"
        self.theme_font_size = "Custom"
        self.font_name = self.theme_cls.font_styles.monospace['medium']['font-name'] 
        self.font_size = self.theme_cls.font_styles.monospace['medium']['font-size']

    def on_enter(self, instance, value):
        if self.input_type == "hint":
            self.text += "!hint"
        elif self.input_type == "admin":
            self.text += "!admin"

    def on_input_select(self, instance, value):
        if value == "hint":
            self.input_type = "hint"
        elif value == "admin":
            self.input_type = "admin"

class BottomChip(MDChip):
    pass

class BottomChipLayout(MDGridLayout):
    pass

class MainBottomSheet(MDBottomSheet):
    '''
    Bottom Sheet class - this
    '''
    input_field = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_field = UserInput(mode="outlined")
        self.add_widget(self.input_field)

    # def on_bar_action(self, instance, screen_name: str):
    #     if not self.state == 'open': self.set_state("open")
    #     if screen_name == "console":
    #         actions = CONSOLE_ACTIONS
    #     elif screen_name == "launcher":
    #         actions = LAUNCHER_ACTIONS
    #     for action in actions:
    #         if action["id"] == "hint":
    #             pass
    #         elif action["id"] == "console":
    #             pass
    #         elif action["id"] == "admin":
    #             pass
