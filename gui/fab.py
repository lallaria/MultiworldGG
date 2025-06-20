from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.button.button import MDExtendedFabButton, MDExtendedFabButtonIcon, MDExtendedFabButtonText

ConsoleFABKV = '''
<ConsoleFABButton@MDExtendedFabButton+HoverBehavior>:
    on_enter: if self.hover_visible: self.fab_state = "expand"
    on_leave: self.fab_state = "collapse"
    MDExtendedFabButtonText:
        text: "Text\\nPrompt"
        halign: "center"
    MDExtendedFabButtonIcon:
        icon: "chat-outline"

MDRelativeLayout:
    ConsoleFABButton:
        id: console_fab_button
        pos: (Window.width - dp(156)), (dp(80)/2 - dp(56)/2)
        on_release: app.bottom_sheet.set_state("toggle")
'''
