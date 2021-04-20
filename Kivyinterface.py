import kivy
import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from data_koordinater import findkoordinater
from data_toilet import link_constructer

class MyGrid(Screen):
    adresse = ObjectProperty(None)
    antal = ObjectProperty(None)

    def toggleCheckBoxes(self):
        self.ids.ADA.disabled = not self.ids.custom.active
        self.ids.ADA.active = False
        self.ids.Unisex.disabled = not self.ids.custom.active
        self.ids.Unisex.active = False

    def checkBoxClick(self, instance,value,crit):
        print(crit,value)

    def btn(self):
        try:
            print("Finder toiletter for:", self.adresse.text)
            print("Antal toilleter:", self.antal.text)
            print(findkoordinater(self.adresse.text))
        except:
            print("Indtast en adresse")

class Resultat(Screen):
    pass

class MyApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MyGrid(name = 'category'))
        self.sm.add_widget(Resultat(name = 'Results'))
        return self.sm

MyApp().run()
