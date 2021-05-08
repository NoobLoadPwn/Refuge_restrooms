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
	coords = ListProperty((0,0)) #Laver en ListProperty for klasse variabel coords
	mark_coords = None #Sætter klassevariabel mark_coords til at være None.
	markerList = [] #laver en liste for klassevariabel markerList
	ADA = False #Sætter klassevariabel ADA til False
	UNISEX = False#Sætter klassevariabel UNISEX til False
	newMap = MapView() #Lavet et en tom MapView til klassevariabel newMap

	def load_map(self, lokation):
		self.coords = findkoordinater(lokation,0) #Sætter coords til at være findkordinater
		self.newMap = MapView(zoom = 10, lat = self.coords[0], lon = self.coords[1])#Laver mapview med data fra coords
		self.ids.map_view.add_widget(self.newMap)#tilføjer MapView som widget til boxlayout i MyApp.kv

	def criteria(self, ada, unisex):
			if ada == "down": #Hvis id'en ADA's state er down
				self.ADA = True #Sæt ada til at være true
			else:
				self.ADA = False#ellers skal det være false

			if unisex == "down": #Hvis id'en Unisex's state er down
				self.UNISEX = True #Sæt unisex til at være True
			else:
				self.UNISEX = False#ellers skal det være false

	def load_markers(self, antal,lokation):
		link = link_constructer(antal, self.ADA, self.UNISEX, lokation) #Bruger link_constructor fra data_toiley.py
		data = data_constructer(link)#Bruger data_constructer fra data_toilet.py

		for address in range(len(data[0])): #Laver en løkke som går fra n til længden af data[0] for at finde hvor mange markers der skal laves
			self.mark_coords = findkoordinater(data[0][address],0) #Sætter mark_coords til at være findkordinater af [0][n] for at få koordinater
			if self.mark_coords != None:#Er self.mark_coords None?
				newMarker = MapMarker(lat=self.mark_coords[0], lon=self.mark_coords[1],source = "marker1.png") #laver en MapMarker med data fra self.mark_coords og bliver gemt i newMarker
				self.newMap.add_widget(newMarker)#tilføjer newMarker som widget til newMap
				self.markerList.append(newMarker)#tilføjer newMarker til klasse variablen markerList
				#print("dette er",self.mark_coords)

	def remove_markers(self):
		self.ids.map_view.remove_widget(self.newMap)#fjerner newMap fra map_view i MyApp.kv
		for marker in self.markerList:#Går igennem hver marker i markerList
			self.newMap.remove_widget(marker)#fjerner widget marker fra newMap

class MyApp(App):
	def build(self):
		self.sm = ScreenManager() #Laver screenmanager
		self.sm.add_widget(homeScreen(name = 'category')) #Tilføjer en screen widget og giver navnet category
		self.sm.add_widget(Resultat(name = 'Results')) #Tilføjer en screen widget og giver navnet Results
		return self.sm

MyApp().run() #Kører appen
