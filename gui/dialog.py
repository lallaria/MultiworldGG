from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivymd.app import MDApp

class MessageBox:
    """
    A simple KivyMD dialog class that can be used throughout the codebase.
    
    Args:
        title (str): The dialog title
        message (str): The dialog message content
        is_error (bool): If True, shows error styling
    """
    app = ObjectProperty(None)
    
    def __init__(self, title="", message="", is_error=False):
        self.title = title
        self.message = message
        self.is_error = is_error
        self.dialog = None
        self.app = MDApp.get_running_app()
        
    def open(self):
        """Opens the dialog and displays it to the user."""
        # Create the dialog content

        content = MDLabel(
            text=self.message,
            theme_text_color="Custom" if self.is_error else "Primary",
            text_color=self.app.theme_cls.errorColor if self.is_error else self.app.theme_cls.onSurfaceColor,  # Red for errors, black for normal
            size_hint_y=None,
            height="48dp"
        )
        
        # Create the dialog
        self.dialog = MDDialog(
            title=self.title,
            type="simple",
            content=content,
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    text_color=self.app.theme_cls.errorColor if self.is_error else self.app.theme_cls.onSurfaceColor,
                    on_release=self._close_dialog
                )
            ]
        )
        
        # Open the dialog
        self.dialog.open()
        
    def _close_dialog(self, instance):
        """Closes the dialog."""
        if self.dialog:
            self.dialog.dismiss()
            self.dialog = None


# Convenience functions for common use cases
def show_info_dialog(title, message):
    """Show an information dialog."""
    dialog = MessageBox(title=title, message=message, is_error=False)
    dialog.open()
    return dialog


def show_error_dialog(title, message):
    """Show an error dialog."""
    dialog = MessageBox(title=title, message=message, is_error=True)
    dialog.open()
    return dialog
