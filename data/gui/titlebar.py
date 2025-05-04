###############################################################################
###
###     Titlebar class - creates the root widget that will be added to
###     the titlebar.  Additionally creates helper functions to bind
###     to the mouse and window events to display the appropriate icon
###     WINDOWS ONLY
###
###############################################################################
__all__ = (
    "Titlebar",
    "TitleBarButton",
)
import sys
from kivy.core.window import Window

from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.effectwidget import EffectWidget
from kivy.uix.effectwidget import HorizontalBlurEffect, VerticalBlurEffect
from kivymd.uix.button import MDIconButton 

archipelago_name = "multiworld.gg"    ## need to fix in the future

TitlebarKV = f'''
<TitleBarButton>:
    style: "standard"
    adaptive_size: True
    pos_hint: {{"y": 0, "x": 0}}
    draggable: False
    theme_bg_color: "Custom"
    md_bg_color: app.theme_mw.titlebar_bg_color[app.theme_cls.theme_style]
    theme_text_color: "Custom"
    text_color: app.theme_cls.onPrimaryContainerColor


Titlebar:
    adaptive_height: True
    width: root.width
    orientation: 'horizontal'
    padding: [0,0,0,0]
    spacing: 0
    theme_bg_color: "Custom"
    md_bg_color: app.theme_mw.titlebar_bg_color[app.theme_cls.theme_style]

    tbmin: tbmin
    tbrestore: tbrestore
    tbmax: tbmax
    tbclose: tbclose
    tblabel: tblabel
    
    Image:
        halign: "left"
        valign: "top"
        source: "data/titlebards.png"
        size: self.texture_size
        size_hint: None,None

    MDFloatLayout:
        id: tblabel
        size_hint: 1, 1
        pos_hint: {{"center_x": .5, "center_y": .5}}

        TitleBlur:
            id: titleblur
            x: 258
            y: 696
            size_hint_x: 1
            height: 40
            opacity: .5
            MDLabel:
                pos_hint: {{"center_x": .5, "center_y": .5}}
                id: tblabel_title
                text: app.title
                font_style: "TitleBar"
                role: "small"
                text_size: self.width, None
                outline_width: 2
                outline_color: app.theme_cls.shadowColor
                shorten: True
                shorten_from: "center"
                theme_text_color: "Custom"
                text_color: app.theme_cls.shadowColor
                opacity: .5

        MDLabel:
            x: 256
            y: 697
            id: tblabeltext
            text: app.title
            font_style: "TitleBar"
            text_size: self.width, None
            role: "small"
            shorten: True
            shorten_from: "center"
            outline_width: 1
            outline_color: app.theme_cls.inverseOnSurfaceColor


    TitleBarButton:
        id: tbmin
        icon: "window-minimize"
        on_release: root.tb_min()
    
    TitleBarButton:
        id: tbrestore
        icon: "window-restore"
        on_release: root.tb_res()

    TitleBarButton:
        id: tbmax
        icon: "window-maximize"
        on_release: root.tb_max()

    TitleBarButton:
        id: tbclose
        icon: "close"
        on_release: root.tb_close()

'''
class TitleBlur(EffectWidget):
    effects = [VerticalBlurEffect(size=3), HorizontalBlurEffect(size=3)]

class TitleBarButton(MDIconButton):
    pass

class Titlebar(MDBoxLayout):
    ''' 
    Titlebar class, creates functions to bind to window events
    Windows only
    '''
    titleblur = ObjectProperty(None)
    tbmin = ObjectProperty(None)
    tbmax = ObjectProperty(None)
    tbrestore = ObjectProperty(None)
    tbclose = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Titlebar, self).__init__(**kwargs)

    def tb_close(self):
        MDApp.get_running_app().stop()
        Window.close()

    def tb_max(self):
        Window.maximize()

    def tb_onmax(self, instance):
        try:
            assert self.tbmax in self.children
            self.remove_widget(self.tbmax)
            self.add_widget(self.tbrestore)
            self.remove_widget(self.tbclose)
            self.add_widget(self.tbclose)
        except:
            return

    def tb_res(self):
        Window.restore()

    def tb_onres(self, instance):
        try:
            assert self.tbrestore in self.children
            self.remove_widget(self.tbrestore)
            self.add_widget(self.tbmax)
            self.remove_widget(self.tbclose)
            self.add_widget(self.tbclose)
        except:
            return
        
    def tb_min(self):
        Window.minimize()
