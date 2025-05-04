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

Builder.load_string('''
<HintItem>
    id: panel
    MDExpansionPanelHeader:
        size_hint_x: .9
        pos_hint: {"center_x": 0.5}
        ripple_effect: False
        MDCard:
            padding: "6dp"
            style: "elevated"
            size_hint_y: None
            height: "50dp"
            theme_shadow_softness: "Custom"
            shadow_softness: 1
            theme_elevation_level: "Custom"
            elevation_level: 2
            theme_shadow_color: "Custom"
            shadow_color: root.shadow_color
            theme_bg_color: "Custom"
            md_bg_color: self.theme_cls.secondaryContainerColor
            ripple_effect: False

            MDRelativeLayout:
                MDLabel:
                    markup: True
                    padding: 5,0,0,0
                    text: "[color=self.theme_mw.markup_tags_theme.location_color]" + root.location + "[/color] for [color=self.theme_mw.markup_tags_theme.receiving_player_color]" + root.receiving_player + "[/color]"
                    pos_hint: {"left": 0, "top": 1}
                TrailingPressedIconButton:
                    pos_hint: {"top":1, "right":1}
                    id: chevron
                    icon: "chevron-right"
                    on_release: root.tap_expansion_chevron(root, chevron)

                    
    MDExpansionPanelContent:
        md_bg_color: self.theme_cls.surfaceContainerLowColor
        MDLabel:
            text: "Hint"
            adaptive_height: True
            padding_x: "4dp"
            padding_y: "4dp"

        MDListItem:
            theme_bg_color: "Custom"
            md_bg_color: self.theme_cls.surfaceContainerLowColor
                    
            MDListItemLeadingIcon:
                icon: "earth-box"
                    
            MDListItemHeadlineText:
                text: root.location
                    
            MDListItemSupportingText:
                text: root.entrance
                    
        MDListItem:
            theme_bg_color: "Custom"
            md_bg_color: self.theme_cls.surfaceContainerLowColor
                    
            MDListItemLeadingIcon:
                icon: "account-search"
                    
            MDListItemHeadlineText:
                text: root.finding_player
                    
            MDListItemSupportingText:
                text: root.receiving_player
                                
''')
sliver_appbar = r'''
MDSliverAppbar:
    width: "260dp"
    pos_hint: {"x": 0, "y": 0}
    size_hint_x: None
    hide_appbar: True
    background_color: app.theme_cls.secondaryContainerColor

    MDTopAppBar:
        type: "small"
        MDTopAppBarLeadingButtonContainer:

            MDActionTopAppBarButton:
                icon: "refresh"
        MDTopAppBarTitle:
            text: "Flags"
            halign: "center"
            font_style: "Body"
            role: "medium"
        MDTopAppBarTrailingButtonContainer:

            MDActionTopAppBarButton:
                icon: "food"

            MDActionTopAppBarButton:
                icon: "headphones"

            MDActionTopAppBarButton:
                icon: "dots-vertical"

    MDSliverAppbarHeader:
        MDHeroFrom:   #### ok the herofrom size/loc is the transition size
            id: console_hero_from
            tag: "logo"
            size_hint: 1,1
            pos_hint: {"right": .9}
            Image:
                source: "data/logo_bg.png"
                pos_hint: {"top": 1}
                fit_mode: "scale-down"

'''
console_layout = f'''
MDRelativeLayout:
    id: console_layout
    width: Window.width
    height: Window.height-185
    size_hint: None,None
    pos: 0,82
'''

class TrailingPressedIconButton(RotateBehavior, MDIconButton):
    pass

class HintItem(OpacityExpansionPanel):
    location = StringProperty()
    entrance = StringProperty()
    item_flag = StringProperty()
    status = StringProperty()
    item = StringProperty()
    receiving_player = StringProperty()
    finding_player = StringProperty()
    shadow_color = ColorProperty()
    found = StringProperty()
    chevron = ObjectProperty(None)


    def __init__(self, receiving_player="", finding_player="", item="", location="", 
                 entrance="", shadow_color="", found="", **kwargs):
        # Initialize _bound_children before calling super().__init__
        self._bound_children = set()
        super(HintItem, self).__init__(**kwargs)
        self.found = found
        self.receiving_player = receiving_player
        self.finding_player = finding_player
        self.item = item
        self.location = location
        self.entrance = entrance
        self.shadow_color = shadow_color
        self.opening_transition = "out_expo"

    def tap_expansion_chevron(self, panel: MDExpansionPanel, chevron: TrailingPressedIconButton):
        # Store chevron reference for later use
        panel._chevron = chevron
        
        Animation(
            padding=[0, dp(12), 0, dp(12)]
            if not panel.is_open
            else [0, 0, 0, 0],
            d=0.2,
        ).start(panel)
        panel.open() if not panel.is_open else panel.close()
        panel.set_chevron_down(
            chevron
        ) if not panel.is_open else panel.set_chevron_up(chevron)

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
                self.add_widget(HintItem(
                    receiving_player=f"{hint_items[prog_level][i]['receiving_player']}",
                    finding_player=f"{hint_items[prog_level][i]['finding_player']}",
                    item=f"{hint_items[prog_level][i]['item']}", 
                    location=f"{hint_items[prog_level][i]['location']}",
                    entrance=f"{hint_items[prog_level][i]['entrance']}",
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
        self.consolegrid = Builder.load_string(console_layout)#app grid
        self.add_widget(self.consolegrid, len(self.children))

    def init_important(self):
        self.important_appbar = Builder.load_string(sliver_appbar) #hint bar
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
 