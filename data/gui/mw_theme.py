__all__ = ('MWColorFilter',)

import os
import re
from dataclasses import dataclass
from kivy.core.text import LabelBase
from kivy.metrics import sp
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.config import Config
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivy.lang import Builder
from PIL import Image
import numpy as np

# Overwriting default style.kv
Builder.load_string('''
<Selector>:
    color: app.theme_cls.inversePrimaryColor
''')
# The names of these colors are from Material Design
# and will be the input for primary_palette
# The colors in hex are actual color for the theme
THEME_OPTIONS = {
    "Dark": [("Purple","5f1414"), #default
             ("Brown","3f0071"),
             ("Cyan","004175"),
             ("OrangeRed","006b3c"),
             ("Pink","b5651d"), 
             ("Green","006b3c")],
    "Light": [("Gray","006064"), #default
              ("Goldenrod","004175"),
              ("Gold","5f1414"),
              ("Pink","006b3c"),
              ("Olivedrab","b5651d")]
}

@dataclass
class MarkupTagsTheme:
    location_color: list[str]
    player1_color: list[str]
    player2_color: list[str]
    entrance_color: list[str]
    trap_item_color: list[str]
    regular_item_color: list[str]
    useful_item_color: list[str]
    progression_item_color: list[str]
    command_echo_color: list[str]

    def __init__(self, **kwargs):
        self.location_color=["00c51b", "006f10"]
        self.player1_color=["ff87d7", "b42f88"]
        self.player2_color=["5fafff", "206cb8"]
        self.entrance_color=["60b7e8", "2985a0"]
        self.trap_item_color=["d75f5f", "8f1515"]
        self.regular_item_color=["b2b2b2", "3b3b3b"]
        self.useful_item_color=["bddd7e", "5f8e00"]
        self.progression_item_color=["FFC500", "9f8a00"]
        self.command_echo_color=["ff9334", "a75600"]

class DefaultTheme(ThemableBehavior):
    titlebar_bg_color: dict
    markup_tags_theme: MarkupTagsTheme
    theme_style: StringProperty
    primary_palette: StringProperty
    dynamic_scheme_name: StringProperty
    compact_mode: BooleanProperty


    def __init__(self):
        super().__init__()
        self.global_theme()
        self.titlebar_bg_color = {"Light": self.theme_cls.primaryContainerColor,
                                  "Dark": self.theme_cls.onPrimaryColor}
        self.recolor_atlas()
        self.markup_tags_theme = MarkupTagsTheme()

    def recolor_atlas(self):
        """Recolor the atlas image by replacing pixels close to target colors with their respective theme colors.
        """
        try:
            # Get the base directory for assets
            base_dir = os.path.dirname(os.path.abspath(__file__))
            atlas_path = os.path.join(base_dir, "data", "defaulttheme-0.png")
            output_path = os.path.join(os.environ["KIVY_HOME"], "images","defaulttheme-0.png")

            # Open and convert the image
            atlas = Image.open(atlas_path)
            atlas = atlas.convert("RGBA")
            data = np.array(atlas)

            # Define the target colors and their replacements
            color_pairs = [
                (np.array([50, 164, 206]), np.array(self.theme_cls.primaryColor[:3]) * 255, 100),      # cyanish -> primary
                (np.array([141, 178, 200]), np.array(self.theme_cls.secondaryColor[:3]) * 255, 40),    # blueish -> secondary
                (np.array([10, 72, 77]), np.array(self.theme_cls.onPrimaryColor[:3]) * 255, 21),       # tealish -> onPrimary
                (np.array([32, 72, 77]), np.array(self.theme_cls.onSecondaryColor[:3]) * 255, 15),       # alphatealish -> onPrimary
            ]
            
            # Process each color pair sequentially
            for old_color, new_color, tolerance in color_pairs:
                # Calculate color distances for this color
                rgb_data = data[:, :, :3]
                color_diff = np.sqrt(np.sum((rgb_data - old_color) ** 2, axis=2))
                
                # Create a mask for pixels within tolerance
                mask = color_diff < tolerance
                
                # First, replace exact matches
                exact_match = np.all(rgb_data == old_color, axis=2)
                data[exact_match, :3] = new_color
                
                # Then handle all other pixels within tolerance
                for i in range(data.shape[0]):
                    for j in range(data.shape[1]):
                        if mask[i, j] and not exact_match[i, j]:  # Skip exact matches
                            current_pixel = rgb_data[i, j]
                            direction = current_pixel - old_color
                            direction_norm = np.linalg.norm(direction)
                            if direction_norm > 0:  # Avoid division by zero
                                direction = direction / direction_norm
                                # Apply the same direction from the new color
                                replacement_color = new_color + direction * color_diff[i, j]
                                # Ensure values stay within valid range
                                replacement_color = np.clip(replacement_color, 0, 255)
                                data[i, j, :3] = replacement_color
            
            # Convert back to image and save
            new_atlas = Image.fromarray(data)
            new_atlas.save(output_path)
            
        except Exception as e:
            print(f"Error recoloring atlas: {str(e)}")
            # You might want to log this error or handle it differently

    def global_theme(self):
        #defaults
        self.theme_cls.theme_style = self.theme_style = "Dark"# Dark default
        self.theme_cls.primary_palette = self.primary_palette = THEME_OPTIONS[self.theme_cls.theme_style][0][0] # Purple default
        self.theme_cls.dynamic_scheme_name = self.dynamic_scheme_name = "RAINBOW" # Not changing this

### Full unicode fonts, finally
def RegisterFonts(app: MDApp):
    LabelBase.register('Inter',
                        os.path.join("fonts","Inter-Regular.ttf"),
                        os.path.join("fonts","Inter-Italic.ttf"),
                        os.path.join("fonts","Inter-Bold.ttf"),
                        os.path.join("fonts","Inter-BoldItalic.ttf"))
    LabelBase.register('NanumGothicCoding',
                        os.path.join("fonts","NanumGothicCoding-Regular.ttf"),
                        None,
                        os.path.join("fonts","NanumGothicCoding-Bold.ttf"),
                        None)
    LabelBase.register('GothicA1',
                        os.path.join("fonts","GothicA1-Regular.ttf"),
                        None,
                        os.path.join("fonts","GothicA1-Bold.ttf"),
                        None)
    LabelBase.register('Texturina',
                       os.path.join("fonts","Texturina_14pt-Regular.ttf"),
                       )
    LabelBase.register('LibreFranklin',
                       os.path.join("fonts","LibreFranklin-ExtraBold.ttf"),
                       )
    app.theme_cls.font_styles = {
        "Icon": {
            "large": {
                "line-height": 1,
                "font-name": "Icons",
                "font-size": sp(24),
            },
        },
        "Display": {
            "large": {
                "line-height": 1.64,
                "font-name": "GothicA1",
                "font-size": sp(57),
            },
            "medium": {
                "line-height": 1.52,
                "font-name": "GothicA1",
                "font-size": sp(45),
            },
            "small": {
                "line-height": 1.40,
                "font-name": "GothicA1",
                "font-size": sp(36),
            },
        },
        "Headline": {
            "large": {
                "line-height": 1.40,
                "font-name": "GothicA1",
                "font-size": sp(32),
            },
            "medium": {
                "line-height": 1.36,
                "font-name": "GothicA1",
                "font-size": sp(28),
            },
            "small": {
                "line-height": 1.32,
                "font-name": "GothicA1",
                "font-size": sp(24),
            },
        },
        "Title": {
            "large": {
                "line-height": 1.28,
                "font-name": "Inter",
                "font-size": sp(22),
            },
            "medium": {
                "line-height": 1.24,
                "font-name": "Inter",
                "font-size": sp(16),
            },
            "small": {
                "line-height": 1.20,
                "font-name": "Inter",
                "font-size": sp(14),
            },
        },
        "Body": {
            "large": {
                "line-height": 1.24,
                "font-name": "Inter",
                "font-size": sp(16),
            },
            "medium": {
                "line-height": 1.20,
                "font-name": "Inter",
                "font-size": sp(14),
            },
            "small": {
                "line-height": 1.16,
                "font-name": "Inter",
                "font-size": sp(12),
            },
        },
        "Label": {
            "large": {
                "line-height": 1.20,
                "font-name": "Inter",
                "font-size": sp(14),
            },
            "medium": {
                "line-height": 1.16,
                "font-name": "Inter",
                "font-size": sp(12),
            },
            "small": {
                "line-height": 1.16,
                "font-name": "Inter",
                "font-size": sp(11),
            },
        },
        "TitleBar": {
            "large": {
                "line-height": 1.20,
                "font-name": "LibreFranklin",
                "font-size": sp(20),
            },
            "medium": {
                "line-height": 1.20,
                "font-name": "LibreFranklin",
                "font-size": sp(19),
            },
            "small": {
                "line-height": 1.20,
                "font-name": "LibreFranklin",
                "font-size": sp(18),
            },
        },
        "monospace": {
            "large": {
                "line-height": 3,
                "font-name": "NanumGothicCoding",
                "font-size": sp(16),
            },
            "medium": {
                "line-height": 2.5,
                "font-name": "NanumGothicCoding",
                "font-size": sp(14),
            },
            "small": {
                "line-height": 2,
                "font-name": "NanumGothicCoding",
                "font-size": sp(12),
            },
        },
    }
