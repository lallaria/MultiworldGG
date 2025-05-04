__all__ = (
    "BottomAppBar",
    "BottomBarKV"
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
from kivymd.uix.tab.tab import MDTabsPrimary, MDTabsItem, MDTabsItemText, MDTabsCarousel
from kivymd.uix.textfield.textfield import MDTextField

all_tab = [
{
    "id":           "console",
    "buttonicon":   "chat-outline",
    "icon":         "chat-outline",
    "prefill":      "!countdown",
    "label":        "Console",
    "indicator":    "blank",
    "type":         "assist",
},
{
    "id":           "hint",
    "buttonicon":   "map-search",
    "icon":         "map-search",
    "prefill":      "!hint",
    "label":        "Hint",
    "indicator":    "widgets",
    "type":         "assist",
},
{
    "id":           "admin",
    "buttonicon":   "account-lock-outline",
    "icon":         "wrench",
    "prefill":      "password",
    "label":        "Host Administration",
    "indicator":    "server-network",
    "type":         "assist",
}]

def BottomBarKV() -> str:
    '''
    On the fly generate a KV to load
    Sorry this is hard to read!
    Root element is BottomAppBar
    Buttons are created in a for loop according to the dictionary below
    '''
    action_items = ""
    for index,item in enumerate(all_tab):
        action_items = f'''{action_items}
        MDActionBottomAppBarButton(id='{item["id"]}_bar', icon='{item["icon"]}',on_release=lambda instance: app.bottom_sheet.on_bar_action(instance, app.bottom_sheet.ids.bottom_carousel.slides[{index}])),'''
    ### I hate this.
    ### Anyone want some strings in their strings string?
    return f'''
#:import MDActionBottomAppBarButton kivymd.uix.appbar.MDActionBottomAppBarButton

<BottomAppBar>:
    action_items:
        [{action_items}
        ]

    MDFabBottomAppBarButton:
        id: bottomsheet_fab
        icon: "chat-outline"
        on_release: app.bottom_sheet.set_state("toggle")
'''