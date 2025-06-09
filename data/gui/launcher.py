from __future__ import annotations
__all__ = ['LauncherScreen', 'LauncherLayout']
import asynckivy
from textwrap import wrap
from kivy.uix.image import AsyncImage
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import StringProperty, DictProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RotateBehavior
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.lang import Builder
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
from kivymd.uix.behaviors import HoverBehavior

import os
import json
import logging
from kivy.logger import Logger
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

logger = logging.getLogger(__name__)

LauncherKV = '''
<LauncherLayout>:
    id: launcher_layout
    width: 600
    height: 1000
    size_hint: None,None
    pos: 0,82
    game_name: "test"
    orientation: 'vertical'
    padding: 10
    spacing: 10
    theme_bg_color: "Custom"
    md_bg_color: app.theme_cls.primaryContainerColor
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    MDButton:
        id: host_button
        on_release: app.root.current = 'host'
        MDButtonText:
            text: 'Host or Generate'
            halign: 'center'
    MDDropDownItem:
        id: game_type
        on_release: root.open_menu(self)
        MDDropDownItemText:
            text: 'Generic Client'
    MDBoxLayout:
        orientation: 'horizontal'
        spacing: 10
        size_hint: 1, 0.5
        MDButton:
            id: game_yaml_button
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDButtonText:
                text: 'Generate YAML'
                halign: 'center'
        MDButton:
            id: game_patch_button
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDButtonText:
                text: 'Patch ' + root.game_name
                halign: 'center'
    MDBoxLayout:
        orientation: 'horizontal'
        spacing: 10
        padding: 16
        MDTextField:
            id: server
            size_hint_x: 0.7
            MDTextFieldLeadingIcon:
                icon: 'router-network'
            MDTextFieldHintText:
                text: "multiworld.gg" #app.app_config.get("client", "hostname", fallback="multiworld.gg")
        MDTextField:
            id: port
            size_hint_x: 0.3
            MDTextFieldHintText:
                text: "38281" #app.app_config.get("client", "port", fallback="38281")
    MDBoxLayout:
        orientation: 'horizontal'
        spacing: 10
        padding: 16
        MDTextField:
            id: slot_name
            size_hint_x: 0.5
            MDTextFieldLeadingIcon:
                icon: 'slot-machine'
            MDTextFieldHelperText:
                text: "hint text" #app.app_config.get("client", "slot", fallback="")
        MDTextField:
            id: slot_password
            size_hint_x: 0.5
            password: True
            MDTextFieldHelperText:
                text: 'Password'
    MDButton:
        id: connect_button
        #on_release: app.root.connect()
        pos_hint: {'right': .9, 'center_y': 0.5}
        MDButtonText:
            text: 'Connect & Play'
            halign: 'center'

<TagChip>:
    type: "filter"
    MDChipText:
        text: root.text
        icon: root.icon

<GameListPanel>:
    id: game_item
    MDExpansionPanelHeader:
        MDListItem:
            id: game_item_header
            MDListItemSupportingText:
                text: root.game_tag
                text_color: app.theme_cls.onSurfaceColor
                theme_text_color: "Custom"
                theme_font_style: "Label"
                role: "medium"
                shorten: False
            TrailingPressedIconButton:
                id: chevron
                icon: "gamepad-round-right"
                on_release: root.toggle_expansion(self)
    MDExpansionPanelContent:
        id: game_item_content
        orientation: 'vertical'
        padding: "12dp", 0, "12dp", "12dp"
        spacing: 4
        MDLabel:
            adaptive_height: True
            padding: 16, 0, 12, 0

<GameListItemTooltip>:
    tooltip_text: self.tooltip_text
    MDTooltipPlain:
        text: root.tooltip_text
        do_wrap: True
        adaptive_height: True
        theme_text_color: "Custom"
        theme_bg_color: "Custom"
        text_color: app.theme_cls.onSurfaceColor
            
<GameListItemText>:

<GameListItem>:
    tooltip_text: ""
    MDListItemLeadingIcon:
        icon: root.icon
    GameListItemText:
        text: root.text
        tooltip_text: root.tooltip_text
        shorten: False
        do_wrap: False
        adaptive_height: True
        role: "small"
        
<SliverAppbar>:
    pos_hint: {"x": 0, "y": 0}
    hide_appbar: True
    background_color: app.theme_cls.secondaryContainerColor

    SearchBar:
        type: "small"
        id: search_bar
        padding: 4

    MDSliverAppbarHeader:
        MDHeroFrom:   #### ok the herofrom size/loc is the transition size
            id: launcher_hero_from
            tag: "logo"
            size_hint: 1,1
            pos_hint: {"right": .9}
            Image:
                source: "data/logo_bg.png"
                pos_hint: {"top": 1}
                fit_mode: "scale-down"


'''

class GameListItemTooltip(MDTooltip):
    ...

class GameListItemText(GameListItemTooltip,MDListItemSupportingText):
    tooltip_text = StringProperty(".")
    
    def on_press(self):
        self.display_tooltip()
    
    def on_release(self):
        self.remove_tooltip()

class GameListItem(MDListItem):
    '''
    This displays a single item from the game's
    dictionary (genre, theme, etc)'''
    text: StringProperty
    icon: StringProperty
    tooltip_text: StringProperty
    
    def __init__(self, text, icon, tooltip_text=".", **kwargs):
        self.text = text
        self.icon = icon
        self.tooltip_text = tooltip_text
        super().__init__(**kwargs)
        self.width = 256
        self.pos_hint = {"center_y": 0.5}
        Clock.schedule_once(lambda x: self.remove_trailing_icon())


    def remove_trailing_icon(self):
        for id in self.ids:
            if id == "trailing_container":
                self.remove_widget(self.ids[id])


class GameListPanel(MDExpansionPanel):
    '''
    This class is used to display a game item in the game list.
    It is a subclass of MDExpansionPanel.
    '''
    game_tag: StringProperty
    tag_type: DictProperty
    icon = StringProperty("game-controller")
    leading_avatar: MDListItemLeadingAvatar
    game_item_header: MDListItem
    game_item_content: MDExpansionPanelContent
    
    def __init__(self, game_tag, tag_type, **kwargs):
        self.game_tag = game_tag
        self.tag_type = tag_type
        super().__init__(**kwargs)
        self.leading_avatar = MDListItemLeadingAvatar()
        self.width = 256
        self.pos_hint = {"center_y": 0.5}
        Clock.schedule_once(lambda x: self.populate_game_item())

    def populate_game_item(self):
        self.game_item_header = self.ids.game_item_header
        self.game_item_content = self.ids.game_item_content
        self.game_item_header.add_widget(self.leading_avatar)
        self.leading_avatar.source = self.tag_type['cover_url']
        for item in self.tag_type:
            if item == "genres" and self.tag_type['genres']:
                list_tooltip = self.list_tooltip(self.tag_type['genres'])
                self.game_item_content.add_widget(GameListItem(text=list_tooltip['label'], icon="dice-multiple", tooltip_text=list_tooltip['tooltip']))
            elif item == "themes" and self.tag_type['themes']:
                list_tooltip = self.list_tooltip(self.tag_type['themes'])
                self.game_item_content.add_widget(GameListItem(text=list_tooltip['label'], icon="sword", tooltip_text=list_tooltip['tooltip']))
            elif item == "keywords" and self.tag_type['keywords']:
                list_tooltip = self.list_tooltip(self.tag_type['keywords'])
                self.game_item_content.add_widget(GameListItem(text=list_tooltip['label'], icon="tag-outline", tooltip_text=list_tooltip['tooltip']))
            elif item == "player_perspectives" and self.tag_type['player_perspectives']:
                list_tooltip = self.list_tooltip(self.tag_type['player_perspectives'])
                self.game_item_content.add_widget(GameListItem(text=list_tooltip['label'], icon="eye-outline", tooltip_text=list_tooltip['tooltip']))
            elif item == "rating" and self.tag_type['rating']:
                list_tooltip = self.list_tooltip(self.tag_type['rating'])
                self.game_item_content.add_widget(GameListItem(text=list_tooltip['label'], icon="alert-box-outline", tooltip_text=list_tooltip['tooltip']))
            elif item == "release_date" and self.tag_type['release_date']:
                self.game_item_content.add_widget(GameListItem(text=str(self.tag_type['release_date']), icon="calendar-month", tooltip_text=str(self.tag_type['release_date'])))

    def list_tooltip(self, item_list: list[str]) -> dict[str, str]:
        full_list = ", ".join(item_list).rstrip(", ")
        wrapped_list = wrap(full_list, width=17, break_on_hyphens=False, max_lines=3)
        item_dict = {
            "label": "\n".join(wrapped_list).rstrip("\n"),
            "tooltip": full_list
        }
        return item_dict

    def toggle_expansion(self, instance):
        Animation(
            padding=[0, dp(12), 0, dp(12)]
            if not self.is_open
            else [0,0,0,0],
            d=0.2,
        ).start(self)
        self.open() if not self.is_open else self.close()
        self.set_chevron_up(instance) if self.is_open else self.set_chevron_down(instance)

class TrailingPressedIconButton(
    ButtonBehavior, RotateBehavior, MDListItemTrailingIcon
):
    ...

class SliverAppbar(MDSliverAppbar):
    content: MDSliverAppbarContent

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.content = MDSliverAppbarContent(orientation="vertical")
        self.content.id = "content"
        self.add_widget(self.content)

class SearchBar(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_box = MDTextField(MDTextFieldHelperText(text="Game Search"),
            id="game_tag_filter",
            padding=16,
        )
        self.add_widget(self.search_box)
        Clock.schedule_once(lambda x: self.remove_widgets())
    
    def remove_widgets(self):
        for child in self.children:
            if not isinstance(child, MDTextField):
                self.remove_widget(child)

    def add_widget(self, widget):
        if isinstance(widget, MDTextField):
            widget._appbar = self
            self.appbar_title = widget
            Clock.schedule_once(lambda x: self._add_title(widget))
        else:
            super().add_widget(widget)

    def _add_title(self, widget):
        super()._add_title(widget)

class LauncherLayout(MDRelativeLayout):
    def __init__(self, **kwargs):
        logger.debug("Initializing LauncherLayout")
        super().__init__(**kwargs)
        logger.debug(f"LauncherLayout initialized with size_hint: {self.size_hint}, pos_hint: {self.pos_hint}")

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
    launcher_layout: LauncherLayout
    game_filter: list

    def __init__(self,**kwargs):
        logger.debug("Initializing LauncherScreen")
        super().__init__(**kwargs)
        self.game_filter = []
        self.games_mdlist = MDList(width=260)

        async def set_game_list():
            game_list = self.load_game_list()
            for game_tag, tag_type in game_list.items():
                await asynckivy.sleep(0)
                game = GameListPanel(game_tag=game_tag, tag_type=tag_type)
                self.games_mdlist.add_widget(game)

        self.layoutgrid = MDBoxLayout()
        self.important_appbar = SliverAppbar()
        self.launcher_layout = LauncherLayout()
        self.important_appbar.ids.scroll.scroll_wheel_distance = 40
        logger.debug("Loading game list")
        self.important_appbar.width = 260
        self.important_appbar.content.add_widget(self.games_mdlist)

        self.layoutgrid.add_widget(self.important_appbar)
        self.layoutgrid.add_widget(self.launcher_layout)
        self.add_widget(self.layoutgrid)

        asynckivy.start(set_game_list())


    def _update_appbar_rect(self, instance, value):
        self.appbar_rect.pos = instance.pos
        self.appbar_rect.size = instance.size

    def set_filter(self, active, tag):
        if active:
            self.game_filter.append((self.game_tag_filter.text, tag))
        else:
            self.game_filter.remove((self.game_tag_filter.text, tag))

    def on_game_tag_filter_text(self, instance):
        self.game_filter = [(self.game_tag_filter.text, tag) for tag in self.load_game_list().keys()]

    def load_game_list(self) -> list[dict]:
        with open("game_details.json", "r", encoding="utf-8") as file:
            game_list = json.load(file)
        return game_list
    
    def connect(self):
        pass

Builder.load_string(LauncherKV)