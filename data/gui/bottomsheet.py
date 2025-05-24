__all__ = (
    "MainBottomSheet",
    "BottomChipLayout",
)
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDButton
from kivymd.uix.chip.chip import MDChip
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.bottomsheet import MDBottomSheet
from kivymd.uix.tab.tab import MDTabsPrimary, MDTabsItem, MDTabsItemText, MDTabsCarousel
from kivymd.uix.textfield.textfield import MDTextField
from bottomcontent import all_tab

def BottomSheetKV() -> str:
    '''
    Constructing Bottom Sheet
    Function is split out for readability
    '''

    carousel_items = carousel_items_loop()
    return f'''
#:import asynckivy asynckivy

MainBottomSheet
    id: main_bottom_sheet
    size_hint_y: None
    height: "180dp"
    bottom_carousel: bottom_carousel
    md_bg_color: app.theme_cls.surfaceContainerLowColor

    MDStackLayout:
        id: bs_tab_container
        adaptive_height: True
        pos_hint: {{"center_x": 0.5}}

        MDTabsCarousel:
            id: bottom_carousel
            size_hint_y: None
            {carousel_items}

'''
def carousel_items_loop() -> str:
    carousel_items = ""
    for item in all_tab:
        carousel_items = carousel_items + f'''
            MDBoxLayout
                orientation: "vertical"
                pos_hint: {{"center_x": .5, "center_y": .7}}
                size_hint_x: 0.8
                MDTextField:
                    id: {item["id"]}-content
                    mode: "outlined"
                    MDTextFieldLeadingIcon:
                        icon: '{item["icon"]}'
                    MDTextFieldHintText:
                        text: '{item["prefill"]}'
                    MDTextFieldHelperText:
                        text: '{item["label"]}'
                    MDTextFieldTrailingIcon:
                        icon: '{item["indicator"]}'
            '''
    return carousel_items

def ChipsOptionsKV() -> str:
    chips = ""
    for index,item in enumerate(all_tab):
        chips = chips + f'''
    BottomChip:
        id: {item["id"]}-chip
        type: '{item["type"]}'
        icon: '{item["icon"]}'
        text: '{item["label"]}' 
        on_release: app.bottom_sheet.on_bar_action(self, slide = app.bottom_sheet.bottom_carousel.slides[{index}])

'''

    return f'''
<BottomChip@MDChip>:
    id: ObjectProperty()
    type: "assist"
    icon: ""
    text: ""
    MDChipLeadingIcon:
        icon: root.icon
    MDChipText:
        text: root.text

BottomChipLayout:
    rows: 2
    id: chip_box
    spacing: "12dp"
    width: app.bottom_sheet.width
    height: 80
    pos: app.bottom_sheet.x, 0
    size_hint: None, None
    padding: 10,0,10,10

{chips}

    '''

class BottomChipLayout(MDGridLayout):
    pass

class MainBottomSheet(MDBottomSheet):
    bottom_carousel: ObjectProperty
    '''
    Bottom Sheet class
    '''
    def on_bar_action(self, instance, slide):
        if not self.state == 'open': self.set_state("open")
        self.bottom_carousel.load_slide(slide)