from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
import requests
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

Builder.load_file('MyApp.kv')

class MyGridLayout(GridLayout):

    def checkbox_click(self, instance, value):
        if value is True:
            self.label.text = "Checkbox Checked"

        else:
            self.label.text = "Checkbox Unchecked"

class CheckBoxEx(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    CheckBoxEx().run()
