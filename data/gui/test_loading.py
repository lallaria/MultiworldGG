import pytest
from kivy.tests.common import GraphicUnitTest
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.uix.label import Label
from kivydi.loadinglayout import LoadingAnimation
from kivy.uix.effectwidget import EffectWidget
import os
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

class TestLoadingApp(MDApp):
    interval = NumericProperty(0.040)
    def build(self):
        
        # Create main layout
        main_layout = FloatLayout()
        self.pixelate_effect = EffectWidget()
        layout = BoxLayout(orientation='vertical', padding=[0,400,0,0], spacing=10)
        
        # Add canvas instructions for background
        with layout.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(
                pos=layout.pos,
                size=layout.size,
                source=os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "background.png")
            )
        
        # Bind size and pos to update background
        layout.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        self.loading = LoadingAnimation()  
        self.loading.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        

        # Create toggle button
        self.toggle_button = Button(
            text="Toggle Loading",
            pos_hint={'center_x': 0.5},
            on_release=self.toggle_loading
        )
        layout.add_widget(self.toggle_button)
        
        # Create speed control buttons
        speed_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        self.speed_slow = Button(
            text="Slower",
            on_release=lambda x: self.adjust_speed(0.001)  # Increase by 0.05
        )
        self.speed_fast = Button(
            text="Faster",
            on_release=lambda x: self.adjust_speed(-0.001)  # Decrease by 0.05
        )
        self.speed_reset = Button(
            text="Reset Speed",
            on_release=lambda x: self.set_speed(self.loading.DEFAULT_SPEED)
        )
        
        # Create interval label
        self.interval_label = Label(
            text=f"Interval: {self.interval}s",
            size_hint_x=None,
            width=150
        )
        self.bind(interval=self.update_interval_label)
        
        speed_layout.add_widget(self.speed_slow)
        speed_layout.add_widget(self.interval_label)
        speed_layout.add_widget(self.speed_reset)
        speed_layout.add_widget(self.speed_fast)
        
        layout.add_widget(speed_layout)
        self.pixelate_effect.add_widget(layout)
        main_layout.add_widget(self.pixelate_effect)
        main_layout.add_widget(self.loading)
        return main_layout
    
    def update_interval_label(self, *args):
        """Update the interval label text when interval changes"""
        self.interval_label.text = f"Interval: {self.interval:.3f}s"
    
    def toggle_loading(self, *args):
        if self.loading.loading:
            self.loading.hide_loading()
            self.toggle_button.text = "Show Loading"
        else:
            self.loading.show_loading()
            self.toggle_button.text = "Hide Loading"
    
    def set_speed(self, speed):
        """Set the animation speed"""
        self.interval = speed
        self.loading.set_speed(speed)
    
    def adjust_speed(self, delta):
        """Adjust the animation speed by the given delta"""
        if not self.loading.loading:
            return
            
        # Get current speed from clock event
        current_speed = self.interval
        new_speed = current_speed + delta
        
        if new_speed < self.loading.MIN_SPEED:
            new_speed = self.loading.MIN_SPEED #Fastest speed
        else:
            if new_speed > self.loading.MAX_SPEED:
                new_speed = self.loading.MAX_SPEED  # Jump to fastest speed
        
        self.interval = new_speed
        
        # Set the new speed
        self.loading.set_speed(new_speed)

    def _update_bg_rect(self, *args):
        """Update background rectangle size and position"""
        self.bg_rect.pos = self.root.pos
        self.bg_rect.size = self.root.size

class TestLoadingAnimation(GraphicUnitTest):
    def setUp(self):
        super().setUp()
        self.app = TestLoadingApp()
        self.loading = LoadingAnimation()
    
    def test_initial_state(self):
        """Test initial state of LoadingAnimation"""
        assert not self.loading.loading
        assert self.loading.current_frame == 0
        assert self.loading.current_image is None
        assert len(self.loading.frames) > 0
    
    def test_show_loading(self):
        """Test showing loading animation"""
        self.loading.show_loading()
        assert self.loading.loading
        assert self.loading.current_image is not None
    
    def test_hide_loading(self):
        """Test hiding loading animation"""
        #self.loading.show_loading()
        self.loading.hide_loading()
        assert not self.loading.loading
        assert self.loading.current_image is None
    
    def test_frame_update(self):
        """Test frame update functionality"""
        self.loading.show_loading()
        initial_frame = self.loading.current_frame
        
        # Simulate frame update
        Clock.tick()
        self.loading.update_frame(0)
        
        assert self.loading.current_frame == (initial_frame + 1) % len(self.loading.frames)

    def test_speed_control(self):
        """Test speed control functionality"""
        # Test setting speed when not loading
        self.loading.set_speed(0.02)
        assert not self.loading._clock_event  # Should not create clock event when not loading

        # Test setting speed when loading
        self.loading.show_loading()
        initial_event = self.loading._clock_event
        
        # Test setting to minimum speed
        self.loading.set_speed(0.01)  # Try to set below minimum
        assert self.loading._clock_event != initial_event  # Should create new event
        assert self.loading._clock_event.interval == self.loading.MIN_SPEED  # Should clamp to minimum

        # Test setting to maximum speed
        self.loading.set_speed(0.3)  # Try to set above maximum
        assert self.loading._clock_event.interval == self.loading.MAX_SPEED  # Should clamp to maximum

        # Test setting to valid speed
        test_speed = 0.05
        self.loading.set_speed(test_speed)
        assert self.loading._clock_event.interval == test_speed  # Should set exact speed

    def test_speed_constants(self):
        """Test speed constant values"""
        assert self.loading.MIN_SPEED == 0.02
        assert self.loading.MAX_SPEED == 0.2
        assert self.loading.DEFAULT_SPEED == 0.04
        assert self.loading.MIN_SPEED < self.loading.DEFAULT_SPEED < self.loading.MAX_SPEED

if __name__ == '__main__':
    TestLoadingApp().run() 