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
	toiletamount+=data_number_of_toilets#tiljøer den tildelte data til inket, som skal være et tal
	return toiletamount

def offset():
	return 'offset=0'

def ada_accesible(data_ADA):
	if data_ADA==True:#hvis ada er sand bliver der skrevet en string med true, og hvis ikke bliver der skrevet false
		return  'ada=true'
	elif data_ADA==False:
		return 'ada=false'

def unisex(data_unisex):
	if data_unisex==True:#hvis unisex er sand bliver der skrevet en string med true, og hvis ikke bliver der skrevet false
		return 'unisex=true'
	elif data_unisex==False:
		return 'unisex=false'

def latitude(data_lokation):
	latitude='lat='
	latitude+=str(findkoordinater(data_lokation,0)[0])#kalder findkordinater for  latitude, ud fra det input den modtager, og laver det om til string, for at det i linket
	return latitude

def longitude(data_lokation):
	longitude='lng='
	longitude+=str(findkoordinater(data_lokation,0)[1])#kalder findkordinater for  longitude, ud fra det input den modtager, og laver det om til string, for at det i linket
	return longitude

def link_constructer(data_number_of_toilets, data_ADA, data_unisex, data_lokation):
	link='https://www.refugerestrooms.org/api/v1/restrooms/by_location?'#sætter basis delen af linket, der altid skal være det samme
	#kalder alle de forskellige funktioner som piecelink, for at kunne indsætte inputet i rigtig form som et link til api'en.
	for piecelink in [page(), number_of_toilets(data_number_of_toilets),offset(), ada_accesible(data_ADA), unisex(data_unisex), latitude(data_lokation), longitude(data_lokation)]:
		if piecelink!='':#går igennem de forskellige dele af linket, hvis de ikke er blanke
			link+='&'+piecelink #sætter de forskellige dele af linket ind i linket, med et & tegn imellem
	return link

def data_constructer(link):
	datalink=requests.get(link).text #finder linkets input
	decodeddatadict = json.loads(datalink) #laver linkets
	addreses=[]#opretter tomme lister
	directions=[]
	downvote=[]
	upvote=[]
	changing_table=[]
	approved=[]
	city=[]
	state=[]
	name=[]
	for dict in decodeddatadict:#går igennem de forskellige dicts
		addreses.append(dict['street']) #tager dataen fra dict og sætter den ind i dens tilgivne liste
		directions.append(dict['directions'])
		downvote.append(dict['downvote'])
		upvote.append(dict['upvote'])
		changing_table.append(dict['changing_table'])
		approved.append(dict['approved'])
		city.append(dict['city'])
		state.append(dict['state'])
		name.append(dict['name'])
	return addreses, directions, downvote, upvote, changing_table, approved, city, state, name
