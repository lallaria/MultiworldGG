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
import asynckivy

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
from kivymd.theming import ThemableBehavior
from bottomappbar import BottomAppBar

Builder.load_string('''
<ConsoleLayout>:
    id: console_layout
    size_hint: None,None
    pos: 0,82

<ConsoleSliverAppbar>:
    pos_hint: {"x": 0}
    width: 260
    size_hint_x: None
    adaptive_height: True
    hide_appbar: True
    background_color: app.theme_cls.secondaryContainerColor

    MDTopAppBar:
        type: "small"
        pos_hint: {"center_x": 0.5, "top": 1}
        padding: dp(4),0,dp(4),dp(4)
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
        MDHeroTo:   #### ok the herofrom size/loc is the transition size
            id: console_hero_to
            tag: "logo"
            size_hint: 1,1
            pos: root.x, root.y

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

class ConsoleScreen(MDScreen, ThemableBehavior):
    '''
    This is the main screen for the console.
    Left side has the players, with expansion for hints
    Right contains the console
    '''
    name = "console"
    console_hero_to: ObjectProperty
    consolegrid: MDBoxLayout
    important_appbar: MDSliverAppbar
    ui_console: ConsoleView
    bottom_appbar: BottomAppBar


    def __init__(self, **kwargs):
        self.size_hint = (1,1)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        super().__init__(**kwargs)
        self.slots_mdlist = MDList(width=260)

        self.bottom_appbar = BottomAppBar(screen_name="console")

        self.important_appbar = ConsoleSliverAppbar()
        
        self.console_hero_to = self.important_appbar.ids.console_hero_to
        self.heroes_to = [self.console_hero_to]

        Clock.schedule_once(lambda x: self.init_important())

        asynckivy.start(self.set_slots_list())


    def init_important(self):

        self.consolegrid = ConsoleLayout(width=Window.width, height=Window.height-185)
        self.add_widget(self.consolegrid)
        self.add_widget(self.bottom_appbar)


        self.important_appbar.size_hint_x = 260/Window.width
        self.important_appbar.size_hint_y=1-(8/Window.height)

        self.ui_console = ConsoleView(pos_hint={"center_y": .5, "center_x": .5+(130/Window.width)},
                                      size_hint_x=1-(264/Window.width), 
                                      size_hint_y=1-(8/Window.height))
        self.important_appbar.ids.scroll.scroll_wheel_distance = 40
        #self.important_appbar.ids.scroll.y = 82

        self.important_appbar.content.add_widget(self.slots_mdlist)

        self.consolegrid.add_widget(self.important_appbar)
        self.consolegrid.add_widget(self.ui_console)

    async def set_slots_list(self):

        self.slots_mdlist.clear_widgets()
        for slot_name, slot_data in testdict.items():
            await asynckivy.sleep(0)
            slot = GameListPanel(game_tag=slot_name, game_data=slot_data)
            self.slots_mdlist.add_widget(slot)
