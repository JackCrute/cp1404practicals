"""
Practical 8
Program to convert miles to kilometres via GUI.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.609344


class ConvertMilesKilometres(App):
    """ConvertMilesKilometres class."""
    output_kilometres = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self, value):
        """Handle convert button presses"""
        try:
            result = float(value) * MILES_TO_KM
            self.output_kilometres = str(result)
        except ValueError:
            self.output_kilometres = "0.0"

    def handle_increment(self, value):
        """Increment distance in miles up or down by value."""
        try:
            result = int(self.root.ids.input_miles.text) + value
        except ValueError:
            result = 0 + value
        self.root.ids.input_miles.text = str(result)


ConvertMilesKilometres().run()
