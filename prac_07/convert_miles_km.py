from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class ConvertMilesKm(App):

    def build(self):
        self.title = "Convert to miles to kilometer"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self,i):
        "Add number to the input."
        changed_value = self.valid_input() + i
        self.root.ids.user_input.text = str(changed_value)
        self.handle_conversion()

    def handle_conversion(self):
        miles = self.valid_input()
        result = miles * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def valid_input(self):
        try:
            input = float(self.root.ids.user_input.text)
            return input
        except ValueError:
            return 0
        self.handle_conversion(self)


ConvertMilesKm().run()