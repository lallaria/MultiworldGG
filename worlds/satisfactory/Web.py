from BaseClasses import Tutorial
from ..AutoWorld import WebWorld


class SatisfactoryWebWorld(WebWorld):
    theme = "dirt"
    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Satisfactory MultiworldGG mod and connect it to an MultiworldGG world",
        "English",
        "setup_en.md",
        "setup/en",
        ["Robb", "Jarno"]
    )
    tutorials = [setup]
    rich_text_options_doc = True
