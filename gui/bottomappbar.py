from __future__ import annotations
__all__ = (
    "BottomAppBar"
)
from kivy.uix.widget import Widget
from kivymd.uix.appbar import MDBottomAppBar, MDActionBottomAppBarButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDButton
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.bottomsheet import MDBottomSheet
from kivymd.uix.textfield.textfield import MDTextField
from kivy.clock import Clock
from kivydi import CONSOLE_ACTIONS, LAUNCHER_ACTIONS

Builder.load_string('''
<BottomAppBar>:
    theme_bg_color: "Custom"
    md_bg_color: app.theme_cls.primaryContainerColor \
                    if app.theme_cls.theme_style == "Light" \
                    else app.theme_cls.onPrimaryColor
    MDFabBottomAppBarButton:
        id: bottomsheet_fab
        icon: "chat-outline"
        on_release: app.bottom_sheet.set_state("toggle")
''')

class BottomAppBar(MDBottomAppBar):

    def __init__(self, screen_name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if screen_name == "console":
            actions = CONSOLE_ACTIONS   
        elif screen_name == "launcher":
            actions = LAUNCHER_ACTIONS
        action_items = []
        for item in actions:
            button = MDActionBottomAppBarButton(id=item["id"], 
                                                icon=item["icon"])
            button.bind(on_release=lambda instance: self.on_bar_action(instance))
            action_items.append(button)
        Clock.schedule_once(lambda dt: self.set_actions(action_items), 0)

    def set_actions(self, action_items: list[MDActionBottomAppBarButton]):
        self.action_items = action_items

    def on_bar_action(self, instance):
        print(instance)
        pass
