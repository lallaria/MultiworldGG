from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import BooleanProperty, ListProperty, ObjectProperty, StringProperty, DictProperty
from kivy.uix.behaviors import DragBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.chip import MDChip
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.appbar import MDTopAppBar
from kivymd.theming import ThemableBehavior

from .testdict import testdict

# Load the KV string
Builder.load_string('''
<HintCard>:
    orientation: "vertical"
    padding: 16
    spacing: 8
    size_hint: None, None
    size: 350, 180
    radius: [8]
    elevation: 2
    md_bg_color: app.theme_cls.surfaceContainerHighColor
    
    BoxLayout:
        orientation: "vertical"
        spacing: 4
        
        BoxLayout:
            orientation: "horizontal"
            size_hint_y: None
            height: 30
            spacing: 8
            
            MDLabel:
                text: root.item
                theme_text_color: "Primary"
                font_style: "Title"
                bold: True
                size_hint_x: 0.7
                
            MDIconButton:
                icon: "flag" if not root.flagged else "flag-variant"
                theme_icon_color: "Primary" if not root.flagged else "Error"
                on_release: root.toggle_flag()
                size_hint_x: 0.15
                
            MDIconButton:
                icon: "dots-vertical"
                theme_icon_color: "Primary"
                on_release: root.show_importance_menu()
                size_hint_x: 0.15
        
        BoxLayout:
            orientation: "horizontal"
            size_hint_y: None
            height: 30
            spacing: 8
            
            MDLabel:
                text: "at"
                theme_text_color: "Secondary"
                font_style: "Body"
                size_hint_x: 0.1
                
            MDLabel:
                text: root.location
                theme_text_color: "Primary"
                font_style: "Body"
                size_hint_x: 0.9
        
        BoxLayout:
            orientation: "horizontal"
            size_hint_y: None
            height: 30
            spacing: 8
            opacity: 1 if root.entrance else 0
            disabled: not root.entrance
            
            MDLabel:
                text: "via"
                theme_text_color: "Secondary"
                font_style: "Body"
                size_hint_x: 0.1
                
            MDLabel:
                text: root.entrance
                theme_text_color: "Primary"
                font_style: "Body"
                size_hint_x: 0.9
        
        BoxLayout:
            orientation: "horizontal"
            size_hint_y: None
            height: 30
            spacing: 8
            
            MDLabel:
                text: root.player
                theme_text_color: "Primary"
                font_style: "Body"
                bold: True
                size_hint_x: 0.3
                
            MDLabel:
                text: root.importance
                theme_text_color: "Primary"
                font_style: "Body"
                size_hint_x: 0.7

<HintGridLayout>:
    cols: 2 if Window.width >= 600 else 1
    spacing: 10
    padding: 10
    size_hint_y: None
    height: self.minimum_height
    width: Window.width
    MDHeroTo:
        id: hint_hero_to
        tag: "logo"
        pos_hint: {'x': .1, 'y': .9}
        FitImage:
            source: "data/logo_bg.png"
            pos_hint: {"right": .9, "top": .9}
            fit_mode: "scale-down"

<HintScreen>:
    MDBoxLayout:
        size_hint_y: None
        height: Window.height-103
        orientation: "vertical"
        
        MDBoxLayout:
            orientation: "horizontal"
            size_hint_y: None
            height: 48
            spacing: 10
            id: filter_chips_container

            MDIconButton:
                icon: "menu"
                on_release: app.root.toggle_nav_drawer()

            MDIconButton:
                icon: "filter"
                on_release: root.show_filter_menu()
        
        MDBoxLayout:
            orientation: "vertical"
            padding: 10
            spacing: 10
            
            MDBoxLayout:
                orientation: "horizontal"
                size_hint_y: None
                height: 48
                spacing: 10
                id: filter_chips_container
                
            ScrollView:
                id: scroll_view
                do_scroll_x: False
                do_scroll_y: True
                
                HintGridLayout:
                    id: hint_grid

''')

class HintCard(MDCard, DragBehavior, HoverBehavior):
    """A card widget that displays hint information."""
    
    item = StringProperty("")
    location = StringProperty("")
    entrance = StringProperty("")
    player = StringProperty("")
    importance = StringProperty("")
    flagged = BooleanProperty(False)
    hint_data = ObjectProperty(None)

    def __init__(self, **kwargs):
        self.app = MDApp.get_running_app()
        self.theme_style = 0 if self.app.theme_cls.theme_style == "Dark" else 1
        super().__init__(**kwargs)
        self.drag_threshold = dp(20)
        self.drag_timeout = 0.5  # 0.5 seconds for long press
        
    def _update_colors(self):
        """Update colors based on current theme"""
        if not self.hint_data:
            return
            
        if self.hint_data.get("is_player1", True):
            self.theme_bg_color = "Custom"
            self.md_bg_color = self.app.theme_mw.markup_tags_theme.player1_color[self.theme_style]
        else:
            self.theme_bg_color = "Custom"
            self.md_bg_color = self.app.theme_mw.markup_tags_theme.player2_color[self.theme_style]
        
    def on_hint_data(self, instance, value):
        if value:
            self.item = value.get("item", "")
            self.location = value.get("location", "")
            self.entrance = value.get("entrance", "")
            self.player = value.get("player1", "") if value.get("is_player1", True) else value.get("player2", "")
            self.importance = value.get("importance", "")
            self.flagged = value.get("flagged", False)
            
            # Update colors
            self._update_colors()
            
            # Set card shadow color based on importance
            self.elevation = 2
            self.theme_shadow_color = "Custom"
            if self.importance == "Progression":    
                self.shadow_color = self.app.theme_mw.markup_tags_theme.progression_item_color[self.theme_style]
            elif self.importance == "Helpful":
                self.shadow_color = self.app.theme_mw.markup_tags_theme.useful_item_color[self.theme_style]
            elif self.importance == "Junk":
                self.shadow_color = self.app.theme_mw.markup_tags_theme.regular_item_color[self.theme_style]
            elif self.importance == "Trap":
                self.shadow_color = self.app.theme_mw.markup_tags_theme.trap_item_color[self.theme_style]
            
    def toggle_flag(self):
        """Toggle the flagged state of the hint."""
        if self.hint_data:
            self.flagged = not self.flagged
            self.hint_data["flagged"] = self.flagged
            
    def show_importance_menu(self):
        """Show a menu to change the importance level."""
        # This would be implemented with a dropdown menu
        pass

class HintGridLayout(GridLayout):
    """A grid layout that displays hint cards."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(width=self.on_window_width)
        
    def on_window_width(self, instance, value):
        """Update the number of columns based on window width."""
        self.cols = 2 if value >= dp(600) else 1

class HintScreen(MDScreen):
    """A screen that displays hint items in a grid layout."""
    name = "hint"
    hint_hero_to: ObjectProperty
    hints = ListProperty([])
    filtered_hints = ListProperty([])
    flagged_hints = ListProperty([])
    deleted_hints = ListProperty([])
    show_flagged_only = BooleanProperty(False)
    current_filter = StringProperty("all")
    current_sort = StringProperty("default")
    sort_ascending = BooleanProperty(True)
    filter_chip_dict = DictProperty({})  # Dictionary to store filter chips 
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loading = False
        self.dragging = False
        self.drag_card = None
        self.drag_start_pos = None
        self.filter_chip_dict = {}  # Dictionary to store filter chips
        self.load_hints()  # Load test data
        
    def on_kv_post(self, widget):
        """Called after the kv file is loaded."""
        self.hint_hero_to = self.ids.hint_grid.ids.hint_hero_to
        self.heroes_to = [self.hint_hero_to]
        # Create filter chips
        self.create_filter_chips()
        
        # Bind to window size changes
        Window.bind(width=self.on_window_width)
        
    def create_filter_chips(self):
        """Create filter chips for importance levels."""
        filter_chips_container = self.ids.filter_chips_container
        filter_chips_container.clear_widgets()
        
        # Add "All" chip
        all_chip = MDChip()
        all_chip.label = "All"  # Use label instead of text
        all_chip.bind(on_release=lambda x: self.filter_hints("all"))
        all_chip.theme_bg_color = "Custom"
        all_chip.md_bg_color = self.theme_cls.primaryColor
        all_chip.theme_text_color = "Custom"
        all_chip.text_color = self.theme_cls.onPrimaryColor
        self.filter_chip_dict["all"] = all_chip
        filter_chips_container.add_widget(all_chip)
        
        # Add importance level chips
        for importance in ["Progression", "Helpful", "Junk", "Trap"]:
            chip = MDChip()
            chip.label = importance  # Use label instead of text
            chip.bind(on_release=lambda x, imp=importance: self.filter_hints(imp))
            self.filter_chip_dict[importance] = chip
            filter_chips_container.add_widget(chip)
            
        # Add player chips
        player1_chip = MDChip()
        player1_chip.label = "Player 1"  # Use label instead of text
        player1_chip.bind(on_release=lambda x: self.filter_hints("player1"))
        self.filter_chip_dict["player1"] = player1_chip
        filter_chips_container.add_widget(player1_chip)
        
        player2_chip = MDChip()
        player2_chip.label = "Player 2"  # Use label instead of text
        player2_chip.bind(on_release=lambda x: self.filter_hints("player2"))
        self.filter_chip_dict["player2"] = player2_chip
        filter_chips_container.add_widget(player2_chip)
        
    def on_window_width(self, instance, value):
        """Update the grid layout when the window width changes."""
        self.ids.hint_grid.cols = 2 if value >= dp(600) else 1
        
    def add_hint(self, hint_data):
        """Add a hint to the list."""
        # Generate a unique ID if not provided
        if "id" not in hint_data:
            hint_data["id"] = str(len(self.hints) + 1)
            
        # Add order if not provided
        if "order" not in hint_data:
            hint_data["order"] = len(self.hints)
            
        self.hints.append(hint_data)
        self.filter_hints(self.current_filter)
        
    def update_hint(self, hint_id, hint_data):
        """Update a hint in the list."""
        for i, hint in enumerate(self.hints):
            if hint.get("id") == hint_id:
                # Preserve the order
                order = hint.get("order", i)
                hint_data["order"] = order
                self.hints[i] = hint_data
                break
                
        self.filter_hints(self.current_filter)
        
    def remove_hint(self, hint_data):
        """Remove a hint from the list."""
        hint_id = hint_data.get("id")
        if hint_id:
            for i, hint in enumerate(self.hints):
                if hint.get("id") == hint_id:
                    # Mark as deleted instead of removing
                    hint["deleted"] = True
                    self.deleted_hints.append(hint)
                    break
                    
        self.filter_hints(self.current_filter)
        
    def filter_hints(self, filter_type):
        """Filter hints based on the selected filter."""
        self.current_filter = filter_type
        
        # Update chip appearance
        for key, chip in self.filter_chip_dict.items():
            if key == filter_type:
                chip.theme_bg_color = "Custom"
                chip.md_bg_color = self.theme_cls.primaryColor
                chip.theme_text_color = "Custom"
                chip.text_color = self.theme_cls.onPrimaryColor
            else:
                chip.theme_bg_color = "Custom"
                chip.md_bg_color = self.theme_cls.cardColor
                chip.theme_text_color = "Custom"
                chip.text_color = self.theme_cls.onSurfaceColor
        
        # Filter hints
        if filter_type == "all":
            self.filtered_hints = [h for h in self.hints if not h.get("deleted", False)]
        elif filter_type in ["Progression", "Helpful", "Junk", "Trap"]:
            self.filtered_hints = [h for h in self.hints if h.get("importance") == filter_type and not h.get("deleted", False)]
        elif filter_type == "player1":
            self.filtered_hints = [h for h in self.hints if h.get("is_player1", True) and not h.get("deleted", False)]
        elif filter_type == "player2":
            self.filtered_hints = [h for h in self.hints if not h.get("is_player1", True) and not h.get("deleted", False)]
        elif filter_type == "flagged":
            self.filtered_hints = [h for h in self.hints if h.get("flagged", False) and not h.get("deleted", False)]
            
        # Apply sorting
        self.sort_hints(self.current_sort)
        
        # Update the grid
        self.update_hint_grid()
        
    def sort_hints(self, sort_type):
        """Sort hints based on the selected sort type."""
        self.current_sort = sort_type
        
        if sort_type == "default":
            # Sort by order
            self.filtered_hints.sort(key=lambda x: x.get("order", 0))
        elif sort_type == "player":
            # Sort by player
            self.filtered_hints.sort(key=lambda x: x.get("player1", ""))
        elif sort_type == "item":
            # Sort by item
            self.filtered_hints.sort(key=lambda x: x.get("item", ""))
        elif sort_type == "location":
            # Sort by location
            self.filtered_hints.sort(key=lambda x: x.get("location", ""))
        elif sort_type == "importance":
            # Sort by importance
            importance_order = {"Progression": 0, "Helpful": 1, "Junk": 2, "Trap": 3}
            self.filtered_hints.sort(key=lambda x: importance_order.get(x.get("importance", ""), 4))
            
        # Reverse if descending
        if not self.sort_ascending:
            self.filtered_hints.reverse()
            
        # Update the grid
        self.update_hint_grid()
        
    def update_hint_grid(self):
        """Update the grid with the current filtered hints."""
        grid = self.ids.hint_grid
        grid.clear_widgets()
        
        for hint_data in self.filtered_hints:
            card = HintCard(hint_data=hint_data)
            grid.add_widget(card)
            
    def show_filter_menu(self):
        """Show a menu for additional filtering options."""
        # This would be implemented with a dropdown menu
        pass
        
    def show_sort_menu(self):
        """Show a menu for sorting options."""
        # This would be implemented with a dropdown menu
        pass
        
    def toggle_flagged_view(self):
        """Toggle between all hints and flagged hints."""
        self.show_flagged_only = not self.show_flagged_only
        if self.show_flagged_only:
            self.filter_hints("flagged")
        else:
            self.filter_hints("all")
            
    def on_long_press(self, card, touch):
        """Handle long press on a card."""
        if not self.dragging:
            self.dragging = True
            self.drag_card = card
            self.drag_start_pos = touch.pos
            touch.grab(card)
            
    def on_touch_up(self, touch):
        """Handle touch up event."""
        if self.dragging and self.drag_card:
            self.dragging = False
            touch.ungrab(self.drag_card)
            
            # Find the closest card and swap positions
            grid = self.ids.hint_grid
            closest_card = None
            min_distance = float('inf')
            
            for child in grid.children:
                if child != self.drag_card:
                    distance = abs(child.center_y - touch.pos[1])
                    if distance < min_distance:
                        min_distance = distance
                        closest_card = child
                        
            if closest_card and min_distance < dp(20):
                # Swap positions
                self.swap_hints(self.drag_card, closest_card)
                
            self.drag_card = None
            self.drag_start_pos = None
            
    def swap_hints(self, card1, card2):
        """Swap the positions of two hints."""
        hint1 = card1.hint_data
        hint2 = card2.hint_data
        
        if hint1 and hint2:
            # Swap order
            order1 = hint1.get("order", 0)
            order2 = hint2.get("order", 0)
            
            hint1["order"] = order2
            hint2["order"] = order1
            
            # Update the grid
            self.update_hint_grid()
            
    def load_hints(self):
        """Load hints from the data source."""
        # Clear existing hints
        self.hints = []
        
        # Get current user from app
        current_user = "Delilah"
        
        # Transform and load test data
        importance_mapping = {
            "Important": "Progression",
            "Useful": "Helpful",
            "Trash": "Junk"
        }
        
        for importance, hints in testdict.items():
            for hint in hints:
                # Determine if current user is involved in this hint
                is_finding_player = current_user == hint["finding_player"]
                is_receiving_player = current_user == hint["receiving_player"]
                
                transformed_hint = {
                    "id": f"{hint['finding_player']}_{hint['item']}",  # Create unique ID
                    "item": hint["item"],
                    "location": hint["location"],
                    "entrance": hint["entrance"],
                    "player1": hint["finding_player"] if is_finding_player else hint["receiving_player"],
                    "player2": hint["receiving_player"] if is_finding_player else hint["finding_player"],
                    "is_player1": is_finding_player or is_receiving_player,  # True if current user is involved
                    "importance": importance_mapping.get(importance, "Junk"),
                    "flagged": False,
                    "order": len(self.hints)  # Maintain order
                }
                self.hints.append(transformed_hint)
        
        # Simulate loading
        Clock.schedule_once(lambda dt: self.finish_loading(), 1)
        
    def finish_loading(self):
        """Finish loading hints."""

        self.filter_hints(self.current_filter)
        
    def recover_hint(self, hint_data):
        """Recover a deleted hint."""
        hint_id = hint_data.get("id")
        if hint_id:
            for i, hint in enumerate(self.deleted_hints):
                if hint.get("id") == hint_id:
                    # Remove deleted flag
                    hint["deleted"] = False
                    # Add back to hints
                    self.hints.append(hint)
                    # Remove from deleted hints
                    self.deleted_hints.pop(i)
                    break
                    
        self.filter_hints(self.current_filter)

# Register the KV string
