import kivy
import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapSource,MapMarker
from kivy.properties import ListProperty
from data_koordinater import findkoordinater
from data_toilet import link_constructer, data_constructer

class homeScreen(Screen):

	def checkBoxClick(self, instance,value):
		pass

class Resultat(Screen):
	coords = ListProperty((0,0)) #Laver en ListProperty for coords
	mark_coords = None #Sætter mark_coords til at være None. SKAL VÆRE NONE OG IKKE ListProperty FORDI AT DEN IKKE MÅ STARTE MED FORM X,Y
	markerList = [] #Klasse variabler
	ADA = False
	UNISEX = False

	def load_coords(self, lokation):
		self.coords = findkoordinater(lokation,0) #Sætter coords til at være findkordinater

	def criteria(self, ada, unisex):
			if ada == "down": #Hvis id'en ADA's state er down
				self.ADA = True #Sæt ada til at være true
			else:
				self.ADA = False
			if unisex == "down": #Hvis id'en Unisex's state er down
				self.UNISEX = True #Sæt unisex til at være True
			else:
				self.UNISEX = False

	def load_markers(self, antal,lokation):

		link = link_constructer(antal, self.ADA, self.UNISEX, lokation) #Bruger link_constructor fra data_toiley.py
		data = data_constructer(link)#Bruger data_constructer fra data_toilet.py

		for address in range(len(data[0])): #Laver en løkke som går fra n til længden af data[0] for at finde hvor mange markers der skal laves
			self.mark_coords = findkoordinater(data[0][address],0) #Sætter mark_coords til at være findkordinater af [0][n] for at få koordinater
			if self.mark_coords != None:
				newMarker = MapMarker(lat=self.mark_coords[0], lon=self.mark_coords[1],source = "marker1.png")
				self.ids.map_coords.add_widget(newMarker)
				self.markerList.append(newMarker)
				#print("dette er",self.mark_coords)

	def remove_markers(self):
		for marker in self.markerList:
			self.ids.map_coords.remove_widget(marker)

class MyApp(App):
	def build(self):
		self.sm = ScreenManager() #Laver screenmanager
		self.sm.add_widget(homeScreen(name = 'category')) #Tilføjer en screen widget og giver navnet category
		self.sm.add_widget(Resultat(name = 'Results')) #Tilføjer en screen widget og giver navnet Results
		return self.sm

MyApp().run() #Kører appen
