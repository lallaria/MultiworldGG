from __future__ import annotations
__all__ = ['GameListPanel', 
           'GameListItem', 
           'GameListItemLongText', 
           'GameListItemShortText', 
           'GameTrailingPressedIconButton'
           ]
import asynckivy
from textwrap import wrap

from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import StringProperty, DictProperty, ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RotateBehavior

from kivymd.uix.list import *
from kivymd.uix.expansionpanel import *

from kivymd.uix.tooltip import MDTooltip

import logging
from kivy.logger import Logger
from kivy.lang import Builder
import os
from kivy.clock import Clock
from kivymd.app import MDApp

logger = logging.getLogger(__name__)

with open(
    os.path.join("data", "gui", "kivydi", "expansionlist.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())

class GameListItemTooltip(MDTooltip):
    '''Base class for tooltip behavior.'''
    pass

class GameListItemLongText(GameListItemTooltip, MDListItemSupportingText):
    '''Implements a list item with tooltip behavior.'''
    text = StringProperty("")
    tooltip_text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = kwargs.get('text', '')
        self.tooltip_text = kwargs.get('tooltip_text', '')

class GameListItemShortText(MDListItemSupportingText):
    '''Implements a list item with no tooltip behavior.'''
    text = StringProperty("")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = kwargs.get('text', '')

class GameListItem(MDListItem):
    '''
    This displays a single item from a dictionary
    dictionary (genre, theme, etc)'''
    text = StringProperty("")
    icon = StringProperty("")
    tooltip_text = StringProperty("")
    user_dict = DictProperty()
    
    def __init__(self, text="", icon="blank", tooltip_text="", user_dict={}, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.icon = icon
        self.tooltip_text = tooltip_text
        self.user_dict = user_dict
        self.width = 256
        self.pos_hint = {"center_y": 0.5}
        
        # Create and add the text widget
        if "..." in text:
            text_widget = GameListItemLongText()
            text_widget.tooltip_text = tooltip_text
        else:
            text_widget = GameListItemShortText()
        text_widget.text = text
        self.add_widget(text_widget)
        
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
        if self.game_tag == "hint":
            Clock.schedule_once(lambda x: self.populate_hint_item())
        else:
            Clock.schedule_once(lambda x: self.populate_game_item())

    def populate_hint_item(self):
        self.game_item_header = self.ids.game_item_header
        self.game_item_content = self.ids.game_item_content
        self.game_item_header.add_widget(self.leading_avatar)
        self.leading_avatar.source = self.tag_type['player2']['avatar']
        for item in self.tag_type["hints"]:
            self.game_item_content.add_widget(GameListItem(user_dict=item))

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
            "tooltip": "\n".join(wrap(full_list, width=40, break_on_hyphens=False)).rstrip("\n")
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

class GameTrailingPressedIconButton(
    ButtonBehavior, RotateBehavior, MDListItemTrailingIcon
):
    ...