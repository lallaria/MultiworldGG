from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import ObjectProperty, ColorProperty, NumericProperty, BooleanProperty
from kivymd.app import MDApp
from kivy.uix.textinput import TextInput
from kivy.utils import escape_markup
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import MDExtendedFabButton, MDExtendedFabButtonText
from kivydi.markuptextfield import MarkupTextField
from kivy.clock import Clock
#from mw_theme import theme_font_styles

__all__ = ('TextConsole', 'ConsoleView',)

# Builder.load_string('''
# #:import MDApp kivymd.app
# <TextConsole>:
#     multiline: True
#     cursor_color: self.theme_cls.primaryColor
#     background_normal: ""
#     background_active: ""
#     use_menu: True
#     readonly: True
#     do_wrap: True
#     auto_indent: True
#     use_handles: True
#     #scroll_from_swipe: True
# ''')

class TextConsole(MarkupTextField, ThemableBehavior):
    #text_color: ColorProperty

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = self.theme_cls.font_styles.monospace['medium']['font-name'] 
        self.font_size = self.theme_cls.font_styles.monospace['medium']['font-size']
        self.line_spacing = self.theme_cls.font_styles.monospace['medium']['line-height']
        self.selection_color = self.theme_cls.secondaryColor
        self.selection_color[3] = 0.3
        self.text_default_color = self.theme_cls.onSurfaceColor
        self.multiline = True
        self.do_wrap = True
        self.auto_indent = True
        self.use_handles = True
        self.use_menu = True
        self.readonly = True
        self.cursor_color = self.theme_cls.primaryColor
        
    def scroll_to_bottom(self, *args):
        """Scroll the text console to the bottom"""
        self.focus = True
        self.cursor = self.end_cursor

    def on_scroll_y(self, *args):
        pass
    #         return True

class ConsoleView(MDFloatLayout):
    text_console = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.text_console = TextConsole(pos_hint={"x": 0, "y": 0}, 
                                        size_hint=(1-(4/Window.width),1-(185/Window.height)))
        self.add_widget(self.text_console)
        with open(r"C:\Users\Lindsay\source\repos\MultiworldGG\data\gui\textclientlog.txt", encoding='utf-8') as oldlog:
            lines = oldlog.readlines()
            for i in lines:
                self.text_console.text = self.text_console.text + i # TODO: add escape_markup
            self.text_console.text = self.text_console.text + "[color=5fafff]CubeKnight[/color] sent [color=FFC500]☆Power Star☆[/color] to [color=5fafff]Lenamphy_sm64[/color] [color=00c51b](Grub-Crossroads_Stag)[/color]"
        # Create the "To Bottom" button
        self.to_bottom_button = MDExtendedFabButton(MDExtendedFabButtonText(text="Current"),
            pos_hint={"center_x": 0.5, "y": 0},
            on_release=self.scroll_to_bottom
        )
        self.add_widget(self.to_bottom_button)
        self.to_bottom_button.opacity = 0
        self.to_bottom_button.disabled = True
        self.text_console.bind(on_scroll_y=self._show_to_bottom_button)

    def _show_to_bottom_button(self, instance, value):
        if value > self.text_console.cursor[1]:
            print(value)
            print(self.text_console.cursor[1])
            print(instance)
            self.to_bottom_button.opacity = 1
            self.to_bottom_button.disabled = False

    def scroll_to_bottom(self, *args):
        """Callback for the To Bottom button"""
        self.to_bottom_button.opacity = 0
        self.to_bottom_button.disabled = True
        self.text_console.scroll_to_bottom(self.to_bottom_button.x, self.to_bottom_button.y)