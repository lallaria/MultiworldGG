from kivy.factory import Factory
from kivy.uix.layout import Layout
from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarLeadingButtonContainer, MDActionTopAppBarButton, \
                              MDTopAppBarTitle, MDTopAppBarTrailingButtonContainer
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty

__all__ = ["TopAppBarLayout", "TopAppBar"]

client_appbar = '''
TopAppBar:
    type: "small"
    padding: 0,0,0,0
    md_bg_color: app.theme_cls.backgroundColor
    MDTopAppBarLeadingButtonContainer:
        MDActionTopAppBarButton:
            icon: "menu"
            id: menu_button
            on_release: app.open_top_appbar_menu(self)

    MDTopAppBarTitle:
        text: app.title
        font_style: "Title"
        bold: True
        theme_font_style: "Custom"
        pos_hint: {"center_x": .5}

    MDTopAppBarTrailingButtonContainer:

        MDActionTopAppBarButton:
            text: "Profile"
        MDActionTopAppBarButton:
            icon: "account-circle-outline"
'''

class TopAppBar(MDTopAppBar):
    pass
        

class TopAppBarLayout(AnchorLayout):
    top_appbar: ObjectProperty
    anchor_x = "left"
    anchor_y = "top"
    size_hint_x = 1
    padding = 0,39,0,0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.top_appbar = Builder.load_string(client_appbar)
        self.top_appbar.id = "top_appbar"
        self.add_widget(self.top_appbar)


