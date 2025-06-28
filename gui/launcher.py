from __future__ import annotations
__all__ = ['LauncherScreen', 'LauncherLayout']
import asynckivy
from textwrap import wrap
from kivy.uix.image import AsyncImage
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import StringProperty, DictProperty, ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RotateBehavior
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivymd.uix.sliverappbar import MDSliverAppbar, MDSliverAppbarHeader, MDSliverAppbarContent
from kivymd.uix.appbar import MDTopAppBar
from kivymd.theming import ThemableBehavior
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.chip import MDChip, MDChipLeadingIcon, MDChipText
from kivymd.uix.list import *
from kivymd.uix.expansionpanel import *
from kivymd.uix.textfield import MDTextField, MDTextFieldLeadingIcon, MDTextFieldHelperText
from kivymd.uix.tooltip import MDTooltip

import os
import json
import logging
from kivy.logger import Logger
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivymd.app import MDApp
from data.game_index import GameIndex
from .kivydi.expansionlist import *
from .bottomappbar import BottomAppBar

game_index = GameIndex()
logger = logging.getLogger(__name__)

Builder.load_string('''
<LauncherLayout>:
    id: launcher_layout
    size_hint: None,None
    pos: 0,82

<LauncherView>:
    id: launcher_view
    pos: 0,82
    game_name: "test"
    orientation: 'vertical'
    padding: 10
    spacing: 10
    theme_bg_color: "Custom"
    md_bg_color: app.theme_cls.surfaceVariantColor
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    MDBoxLayout:
        orientation: 'vertical'
        spacing: 10
        padding: 8
        pos_hint:{"x": 0, "y": 0}
        MDBoxLayout:
            orientation: 'horizontal'
            spacing: 10
            padding: 8
            MDButton:
                id: host_button
                on_release: app.root.current = 'host'
                MDButtonText:
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.onSurfaceVariantColor
                    text: 'Host or Generate'
                    halign: 'center'

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: 10
            padding: 8
            MDButton:
                id: game_yaml_button
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                MDButtonText:
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.onSurfaceVariantColor
                    text: 'Generate YAML'
                    halign: 'center'
            MDButton:
                id: game_patch_button
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                MDButtonText:
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.onSurfaceVariantColor
                    text: 'Patch ' + root.game_name
                    halign: 'center'
        MDBoxLayout:
            orientation: 'horizontal'
            spacing: 10
            padding: 8
            MDTextField:
                id: server
                size_hint_x: 0.7
                theme_text_color: "Custom"
                text_color_focus: app.theme_cls.onSurfaceVariantColor
                MDTextFieldLeadingIcon:
                    icon: 'router-network'
                MDTextFieldHintText:
                    text: app.app_config.get("client", "hostname", fallback="multiworld.gg")
            MDTextField:
                id: port
                size_hint_x: 0.3
                theme_text_color: "Custom"
                text_color_focus: app.theme_cls.onSurfaceVariantColor
                MDTextFieldHintText:
                    text: app.app_config.get("client", "port", fallback="38281")
        MDBoxLayout:
            orientation: 'horizontal'
            spacing: 10
            padding: 8
            MDTextField:
                id: slot_name
                size_hint_x: 0.5
                theme_text_color: "Custom"
                text_color_focus: app.theme_cls.onSurfaceVariantColor
                MDTextFieldLeadingIcon:
                    icon: 'ticket-account'
                MDTextFieldHelperText:
                    text: app.app_config.get("client", "slot", fallback="")
            MDTextField:
                id: slot_password
                size_hint_x: 0.5
                password: True
                theme_text_color: "Custom"
                text_color_focus: app.theme_cls.onSurfaceVariantColor
                MDTextFieldHelperText:
                    text: 'Password'
        MDBoxLayout:
            orientation: 'horizontal'
            spacing: 10
            padding: 8
            MDButton:
                id: connect_button
                on_release: app.root.connect()
                pos_hint: {'right': .9, 'center_y': 0.5}
                MDButtonText:
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.onSurfaceVariantColor
                    text: 'Connect & Play'
                    halign: 'center'

<TagChip>:
    type: "filter"
    MDChipText:
        text: root.text
        icon: root.icon
        
<LauncherSliverAppbar>:
    pos_hint: {"x": 0}
    width: 260
    size_hint_x: None
    adaptive_height: True
    hide_appbar: True
    background_color: app.theme_cls.secondaryContainerColor
    launcher_hero_from: launcher_hero_from

    SearchBar:
        type: "small"
        id: games_search_bar
        padding: dp(4)
        pos_hint: {"center_x": 0.5, "top": 1}

    MDSliverAppbarHeader:
        MDHeroFrom:   #### ok the herofrom size/loc is the transition size
            id: launcher_hero_from
            tag: "logo"
            size_hint: 1,1
            pos: root.x, root.y
            Image:
                source: "data/logo_bg.png"
                pos_hint: {"top": 1}
                fit_mode: "scale-down"

<LauncherTextField>:
    theme_font_name: "Custom"
    theme_font_style: "Custom"
    font_name: app.theme_cls.font_styles[self.font_style][self.role]["font-name"]
    font_size: app.theme_cls.font_styles[self.font_style][self.role]["font-size"]
    MDTextFieldHelperText:
        text: root.helper_text
        theme_font_name: "Custom"
        theme_font_style: "Custom"
        font_name: app.theme_cls.font_styles[self.font_style][self.role]["font-name"]
        font_size: app.theme_cls.font_styles[self.font_style][self.role]["font-size"]

''')
class LauncherLayout(MDRelativeLayout):
    pass

class LauncherView(MDBoxLayout):
    pass

class LauncherSliverAppbar(MDSliverAppbar):
    content: MDSliverAppbarContent

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.content = MDSliverAppbarContent(orientation="vertical")
        self.content.id = "content"
        self.add_widget(self.content)

class LauncherTextField(MDTextField):
    helper_text = StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper_text = kwargs.get("helper_text", "")

class SearchBar(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_box = LauncherTextField(
            id="game_tag_filter",
            padding=dp(16),
            font_style = "Body",
            helper_text = "Game Search",
            pos_hint = {"center_x": 0.5, "top": 1}
        )
        self.add_widget(self.search_box)
        Clock.schedule_once(lambda x: self.remove_widgets())
        self.search_box.bind(on_text_validate=self.on_enter)
    
    def remove_widgets(self):
        for child in self.children:
            if not isinstance(child, MDTextField):
                self.remove_widget(child)

    def add_widget(self, widget):
        if isinstance(widget, MDTextField):
            widget._appbar = self
            self.appbar_title = widget
            widget.theme_font_style = "Body"
            Clock.schedule_once(lambda x: self._add_title(widget))
        else:
            super().add_widget(widget)

    def _add_title(self, widget):
        super()._add_title(widget)

    def on_enter(self, instance):
        # Get the parent screen to access the game list
        screen = MDApp.get_running_app().screen_manager.current_screen
        if isinstance(screen, LauncherScreen):
            # Clear existing game list
            screen.games_mdlist.clear_widgets()
            # Update the filter and trigger new search
            screen.game_tag_filter = instance.text
            asynckivy.start(screen.set_game_list())


class LauncherScreen(MDScreen, ThemableBehavior):
    '''
    This is the main screen for the launcher.
    Left side has the game list/sorter
    Right contains the previously selected game
    with options to connect to the MW server
    '''
    name = "launcher"
    launcher_hero_from: ObjectProperty
    layoutgrid: MDBoxLayout
    important_appbar: MDSliverAppbar
    launcher_layout: LauncherView
    game_filter: list
    game_tag_filter: StringProperty
    bottom_appbar: BottomAppBar
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 1)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.game_filter = []
        self.games_mdlist = MDList(width=260)
        self.game_tag_filter = "popular"

        self.bottom_appbar = BottomAppBar(screen_name="launcher")
        self.important_appbar = LauncherSliverAppbar()

        Clock.schedule_once(lambda x: self.init_important())

        asynckivy.start(self.set_game_list())

    def init_important(self):
        self.launchergrid = LauncherLayout(width=Window.width, height=Window.height-185)
        self.add_widget(self.launchergrid)
        self.add_widget(self.bottom_appbar)

        self.launcher_hero_from = self.important_appbar.launcher_hero_from
        self.heroes_from = [self.launcher_hero_from]

        self.important_appbar.size_hint_x = 260/Window.width
        self.important_appbar.size_hint_y=1-(8/Window.height)

        self.launcher_view = LauncherView(pos_hint={"center_y": .5, "center_x": .5+(130/Window.width)},
                                      size_hint_x=1-(264/Window.width), 
                                      size_hint_y=1-(8/Window.height))
        
        self.important_appbar.ids.scroll.scroll_wheel_distance = 40
        #self.important_appbar.ids.scroll.y = 82

        self.important_appbar.content.add_widget(self.games_mdlist)

        self.launchergrid.add_widget(self.important_appbar)  
        self.launchergrid.add_widget(self.launcher_view)

    async def set_game_list(self):
        game_index = GameIndex()
        matching_games = game_index.search(self.game_tag_filter)
        self.games_mdlist.clear_widgets()
        for game_name, game_data in matching_games.items():
            await asynckivy.sleep(0)
            game = GameListPanel(game_tag=game_name, game_data=game_data)
            self.games_mdlist.add_widget(game)

    def set_filter(self, active, tag):
        if active:
            self.game_filter.append((self.game_tag_filter.text, tag))
        else:
            self.game_filter.remove((self.game_tag_filter.text, tag))

    def on_game_tag_filter_text(self, instance):
        self.game_filter = [(self.game_tag_filter.text, tag) for tag in GameIndex.search(self.game_tag_filter.text)]
    
    def connect(self):
        pass
