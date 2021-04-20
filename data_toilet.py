import requests
from data_koordinater import findkoordinater
import http.client, urllib.parse
from pprint import pprint
import json

test_number_of_toilets='10'
test_ADA=False
test_unisex=True
test_lokation='New York'

def page():
	return 'page=1'

def number_of_toilets(data_number_of_toilets):
	toiletamount='per_page='
	toiletamount+=data_number_of_toilets
	return toiletamount

def offset():
	return 'offset=0'

def ada_accesible(data_ADA):
	if data_ADA==True:
		return  'ada=true'
	elif data_ADA==False:
		return 'ada=false'

def unisex(data_unisex):
	if data_unisex==True:
		return 'unisex=true'
	elif data_unisex==False:
		return 'unisex=false'

def latitude(data_lokation):
	latitude='lat='
	latitude+=str(findkoordinater(data_lokation)[0])
	return latitude

def longitude(data_lokation):
	longitude='lng='
	longitude+=str(findkoordinater(data_lokation)[1])
	return longitude

def link_constructer(data_number_of_toilets, data_ADA, data_unisex, data_lokation):
	link='https://www.refugerestrooms.org/api/v1/restrooms/by_location?'
	for piecelink in [page(), number_of_toilets(data_number_of_toilets),offset(), ada_accesible(data_ADA), unisex(data_unisex), latitude(data_lokation), longitude(data_lokation)]:
		if piecelink!='':
			link+='&'+piecelink
	return link

test_link=link_constructer(test_number_of_toilets, test_ADA, test_unisex, test_lokation)

def data_constructer(link):
	datalink=requests.get(link).text
	decodeddatadict = json.loads(datalink) #laver
	addreses=[]
	directions=[]
	downvote=[]
	upvote=[]
	changing_table=[]
	approved=[]
	city=[]
	state=[]
	name=[]
	for dict in decodeddatadict:#går igennem de forskellige dicts
		addreses.append(dict['street']) #tager adressen og sætter den ind i adresses listen
		directions.append(dict['directions'])
		downvote.append(dict['downvote'])
		upvote.append(dict['upvote'])
		changing_table.append(dict['changing_table'])
		approved.append(dict['approved'])
		city.append(dict['city'])
		state.append(dict['state'])
		name.append(dict['name'])
	return addreses, directions, downvote, upvote, changing_table, approved, city, state, name

data=data_constructer(test_link)
