from __future__ import annotations
__all__ = ['LauncherScreen', 'LauncherLayout']
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.sliverappbar import MDSliverAppbar, MDSliverAppbarHeader, MDSliverAppbarContent
from kivymd.theming import ThemableBehavior
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.chip import MDChip, MDChipLeadingIcon, MDChipText
from kivymd.uix.textfield import MDTextField, MDTextFieldLeadingIcon, MDTextFieldHelperText

LauncherKV = '''
<LauncherLayout>:
    orientation: 'vertical'
    padding: 10
    spacing: 10
    size_hint: 1, 1
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
                text: app.app_config.get("client", "hostname", fallback="multiworld.gg")
        MDTextField:
            id: port
            size_hint_x: 0.3
            MDTextFieldHintText:
                text: app.app_config.get("client", "port", fallback="38281")
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
                text: app.app_config.get("client", "slot", fallback="")
        MDTextField:
            id: slot_password
            size_hint_x: 0.5
            password: True
            MDTextFieldHelperText:
                text: 'Password'
    MDButton:
        id: connect_button
        on_release: app.root.connect()
        pos_hint: {'right': .9, 'center_y': 0.5}
        MDButtonText:
            text: 'Connect & Play'
            halign: 'center'
'''


class LauncherLayout(MDBoxLayout):
    pass

class LauncherScreen(MDScreen, ThemableBehavior):
    #TODO if portrait/landscape, change layout
    name = "launcher"
    console_hero_from: ObjectProperty
    consolegrid: MDBoxLayout
    important_appbar: MDSliverAppbar
    sidebar_content: MDBoxLayout
    launcher_layout: LauncherLayout
    game_filter: list

    def __init__(self, game_tags,**kwargs):
        super().__init__(**kwargs)
        self.game_filter = []
        self.important_appbar = MDSliverAppbar(
            MDSliverAppbarHeader(
                MDLabel(text="Game Filter"),
                FitImage(source="data/logo_bg.png"),
            ), 
            background_color = self.theme_cls.secondaryContainerColor,
        )
        self.sidebar_content = MDBoxLayout(MDTextField(
            MDTextFieldLeadingIcon(icon="game-controller"),
            MDTextFieldHelperText(text="Game Search"),
            id = "game_tag_filter",
            orientation = "vertical",
            size_hint = (1, None),
            height = "48dp",
        ))
        for game_tag, tag_type in game_tags:
            chip = MDChip(MDChipLeadingIcon(icon=tag_type),
                            MDChipText(text=game_tag, 
                                        icon=tag_type, 
                                        type="filter"))
            chip.bind(active=lambda x, y, z=tag_type: self.set_filter(y,z))
            self.sidebar_content.add_widget(chip)

        self.sidebar_content.orientation = "vertical"
        self.sidebar_content.size_hint = (1, None)
        self.launcher_layout = LauncherLayout()

    def set_filter(self, active, tag):
        if active:
            self.game_filter.append((self.game_tag.text, tag))
        else:
            self.game_filter.remove((self.game_tag.text, tag))

    def on_game_tag_filter_text(self, instance):
        self.game_filter = [(self.game_tag_filter.text, tag) for tag in ["Outline", "Off", "On"]]

Builder.load_string(LauncherKV)