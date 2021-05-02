from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label

class DynamicLabelsApp(App):
    """Kivy app to demo dynamic labels creation."""


    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # dictionary of names and phone number
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456", "Kathy":"0423568199"}


    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.display_names()
        return self.root

    def display_names(self):
        """Create labels from dictionary entries and add them to the GUI."""
        for name in self.name_to_phone:       #Getting name from dictionary of names and phone number
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

DynamicLabelsApp().run()
