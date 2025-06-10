from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.metrics import sp
import os

# Register all fonts
FONT_DIR = os.path.join('data', 'gui', 'fonts')
for font_file in os.listdir(FONT_DIR):
    if font_file.endswith(('.ttf', '.otf')):  # Check for both TTF and OTF files
        font_name = os.path.splitext(font_file)[0]
        font_path = os.path.join(FONT_DIR, font_file)
        LabelBase.register(name=font_name, fn_regular=font_path)

class FontTestApp(App):
    def build(self):
        # Create main layout
        main_layout = BoxLayout(orientation='vertical')
        
        # Create scrollable area
        scroll = ScrollView()
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        
        # Text to display
        text = '[color=5fafff]CubeKnight[/color] sent [color=FFC500]☆Power Star☆[/color] to [color=5fafff]Lenamphy_sm64[/color] [color=00c51b](Grub-Crossroads_Stag)[/color]'
        
        # Create a label for each font
        for font_file in os.listdir(FONT_DIR):
            if font_file.endswith(('.ttf', '.otf')):  # Check for both TTF and OTF files
                font_name = os.path.splitext(font_file)[0]
                label = Label(
                    text=f"{font_name}:\n{text}",
                    markup=True,
                    font_size=sp(14),
                    font_name=font_name,
                    size_hint_y=None,
                    height=50,
                    halign='left',
                    valign='middle',
                    text_size=(Window.width - 40, None)
                )
                layout.add_widget(label)
        
        scroll.add_widget(layout)
        main_layout.add_widget(scroll)
        return main_layout

if __name__ == '__main__':
    FontTestApp().run() 