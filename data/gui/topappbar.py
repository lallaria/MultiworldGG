from kivy.factory import Factory
from kivy.uix.layout import Layout
from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarLeadingButtonContainer, MDActionTopAppBarButton, \
                              MDTopAppBarTitle, MDTopAppBarTrailingButtonContainer
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
import time

__all__ = ["TopAppBarLayout", "TopAppBar"]

Builder.load_string('''
<TopAppBar>:
    type: "small"
    padding: 0,0,0,0
    md_bg_color: app.theme_cls.backgroundColor
    MDTopAppBarLeadingButtonContainer:
        MDActionTopAppBarButton:
            icon: "menu"
            id: menu_button
            on_release: app.open_top_appbar_menu(self)

    MDTopAppBarTitle:
        text: root.timer
        font_style: "Title"
        bold: True
        theme_font_style: "Custom"
        pos_hint: {"x": .05}
        size_hint_x: .1

    MDTopAppBarTrailingButtonContainer:

        MDActionTopAppBarButton:
            text: "Profile"
        MDActionTopAppBarButton:
            icon: "account-circle-outline"
''')

class TopAppBar(MDTopAppBar):
    timer: StringProperty

    def __init__(self, **kwargs):
        self.timer = "00:00:00"
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        self.timer = time.strftime("%H:%M:%S", time.gmtime(time.time()))

class TopAppBarLayout(AnchorLayout):
    top_appbar: ObjectProperty
    anchor_x = "left"
    anchor_y = "top"
    size_hint_x = 1
    padding = 0,39,0,0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.top_appbar = TopAppBar()
        self.top_appbar.id = "top_appbar"
        self.add_widget(self.top_appbar)


