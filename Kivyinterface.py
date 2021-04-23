import kivy
import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapSource
from data_koordinater import findkoordinater
from data_toilet import link_constructer, data_constructer

class MyGrid(Screen):

	#normal = false, down = true

	def checkBoxClick(self, instance,value,crit):
		pass

	def btn(self):

		ada = False
		if self.ids.ADA.state == "down":
			ada = True
			print("ADA is true")

		unisex = False
		if self.ids.Unisex.state == "down":
			unisex = True
			print("Unisex is true")

		#link = link_constructer(self.antal.text, ada, unisex,self.adresse.text)
		#data = data_constructer(link)
		#self.ids.ads.text = str(data[0])

class Resultat(Screen):
	def update(self):
		#print(self.parent.ids.resultatscreen.ids.map_coords.lat)
		#print(self.parent.ids.resultatscreen.ids.map_coords.lon)
		print((findkoordinater(self.parent.ids.textinput.ids.adresse.text)))
		print((findkoordinater(self.parent.ids.textinput.ids.adresse.text)))


class MyApp(App):
	def build(self):
		self.sm = ScreenManager()
		self.sm.add_widget(MyGrid(name = 'category'))
		self.sm.add_widget(Resultat(name = 'Results'))
		return self.sm

MyApp().run()
