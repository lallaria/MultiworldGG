from kivy.factory import Factory
from kivy.properties import StringProperty, ObjectProperty, ColorProperty
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.config import Config as MWKVConfig
from kivy.uix import widget
from kivy.uix.recycleview import RecycleViewBehavior
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.card.card import MDCard, MDRelativeLayout
from kivymd.uix.chip.chip import MDChipLeadingAvatar
from kivy.uix.anchorlayout import AnchorLayout
#from console import ConsoleView, UIRecycleView
from textconsole import ConsoleView, TextConsole
from launcher import LauncherScreen, LauncherLayout

# from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen, MDHeroTo
from kivymd.uix.recyclegridlayout import MDRecycleGridLayout
from kivymd.uix.behaviors import RotateBehavior
from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarLeadingButtonContainer, MDActionTopAppBarButton, \
                              MDTopAppBarTitle, MDTopAppBarTrailingButtonContainer
from kivymd.uix.sliverappbar import MDSliverAppbar, MDSliverAppbarContent, MDSliverAppbarHeader
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelContent
from kivymd.uix.list import MDList, MDListItem
from testdict import testdict
from expansionpanel import OpacityExpansionPanel
from dataclasses import dataclass
from textwrap import wrap
from kivydi.expansionlist import *

Builder.load_string('''
<ConsoleLayout>:
    id: console_layout
    width: Window.width
    height: Window.height-185
    size_hint: None,None
    pos: 0,82

<ConsoleSliverAppbar>:
    pos_hint: {"x": 0}
    y: 82
    adaptive_height: True
    hide_appbar: True
    background_color: app.theme_cls.secondaryContainerColor

    MDTopAppBar:
        type: "small"
        pos_hint: {"center_x": 0.5, "top": .95}
        padding: dp(4)
        MDTopAppBarLeadingButtonContainer:
            MDActionTopAppBarButton:
                icon: "refresh"
                on_release: root.refresh()
        MDTopAppBarTitle:
            text: "Flags"
            halign: "center"
            font_style: "Body"
            role: "medium"
        MDTopAppBarTrailingButtonContainer:
            MDActionTopAppBarButton:
                icon: "food"
                on_release: root.set_bk()
            MDActionTopAppBarButton:
                icon: "headphones"
                on_release: root.set_deafen()

    MDSliverAppbarHeader:
        MDHeroFrom:   #### ok the herofrom size/loc is the transition size
            id: console_hero_from
            tag: "logo"
            size_hint: 1,1
            pos_hint: {"right": .9, "top": 1}
            Image:
                source: "data/logo_bg.png"
                pos_hint: {"top": 1}
                fit_mode: "scale-down"

''')

class ConsoleLayout(MDRelativeLayout):
    pass

class ConsoleSliverAppbar(MDSliverAppbar):
    content: MDSliverAppbarContent

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.content = MDSliverAppbarContent(orientation="vertical")
        self.content.id = "content"
        self.add_widget(self.content)

class SideBarContent(MDSliverAppbarContent):
    def __init__(self, **kwargs):
        super(SideBarContent, self).__init__(**kwargs)
        hint_items = testdict
        app = MDApp.get_running_app()
        theme_style = 0 if app.theme_cls.theme_style == "Dark" else 1
        for prog_level in hint_items:
            for i in range(len(hint_items[prog_level])):
                shadow_color = app.theme_mw.markup_tags_theme.progression_item_color[theme_style]
                if prog_level == "Useful": shadow_color = app.theme_mw.markup_tags_theme.useful_item_color[theme_style]
                if prog_level == "Trash": shadow_color = app.theme_mw.markup_tags_theme.regular_item_color[theme_style]
                if prog_level == "Trap": shadow_color = app.theme_mw.markup_tags_theme.trap_item_color[theme_style]
                self.add_widget(GameListPanel(
                    game_tag=f"{hint_items[prog_level][i]['item']}",
                    tag_type=hint_items[prog_level][i],
                    shadow_color=get_color_from_hex(shadow_color)))
        self.bind(minimum_height=self.setter('height'))

class ConsoleScreen(MDScreen):
    name = "console"
    console_hero_from: ObjectProperty
    consolegrid: MDBoxLayout
    important_appbar: MDSliverAppbar
    sidebar_content: SideBarContent
    ui_console: ConsoleView

    def init_console_grid(self):
        self.consolegrid = ConsoleLayout()#app grid
        self.add_widget(self.consolegrid, len(self.children))

    def init_important(self):
        self.important_appbar = ConsoleSliverAppbar()
        self.important_appbar.size_hint_x = 260/Window.width
        self.console_hero_from = self.important_appbar.ids.console_hero_from
        self.heroes_from = [self.console_hero_from]
        self.ui_console = ConsoleView(pos_hint={"center_y": .5, "center_x": .5+(130/Window.width)},
                                      size_hint_x=1-(264/Window.width), 
                                      size_hint_y=1-(8/Window.height))
        self.important_appbar.add_widget(SideBarContent(orientation="vertical", spacing="12dp", padding=(0,"16dp",0,0)))
        self.important_appbar.adaptive_height = True
        self.consolegrid.add_widget(self.important_appbar)
        self.consolegrid.add_widget(self.ui_console, len(self.consolegrid.children))

    def __init__(self, **kwargs):
        self.size_hint = (1,1)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        super().__init__(**kwargs)
        self.init_console_grid()
        self.init_important()
 