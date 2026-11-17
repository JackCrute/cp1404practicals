"""
CP1404 - Practical 8
Program for Dynamic Labels exercise
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    """Dynamic Labels class."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Jane", "Gibraltar", "Geoff"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from names and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.labels_box.add_widget(temp_label)


DynamicLabels().run()
