import http.client, urllib.parse
from pprint import pprint
import json


def findkoordinater(lokation, fails):
	if fails <= 5:
		conn = http.client.HTTPConnection('api.positionstack.com')#definerer hvilken api den skal gå ind

		params = urllib.parse.urlencode({#tildeler nødvendige parametre
			'access_key': '7198557e74d9402117311a3c30187caa',#bruger access koden for at få adgang til api
			'query': lokation,#sætter parameteren til at være det samme som den givede data
			'limit': 1,
			})

		conn.request('GET', '/v1/forward?{}'.format(params)) #kalder inputtet fra apien, med de rigtige parametre
		res = conn.getresponse()#får response (denne del aer mere sikkerhed end nødvendig)
		data = res.read() #læser reponsen, og dermed får dataen, fra at kalde apien.
		decodeddata = data.decode('utf-8') #sætter data til rigtig datatype altså string, for at programmet kan læse det.
		decodeddatadict = json.loads(decodeddata) #bruger json til at lave string om til dictionaries, for at kunne plukke de rigtige dele af data.

		#print(decodeddatadict)
		#print(decodeddatadict['data'])
		#print(decodeddatadict['data'][0]['longitude'])
		#print(type(decodeddatadict))
		if len(decodeddatadict['data']) > 0 and isinstance(decodeddatadict['data'][0], dict):
			if len(decodeddatadict['data'][0]) > 0:
				latitude = decodeddatadict['data'][0]['latitude'] #tager latitude fra decodeddatadict
				longitude = decodeddatadict['data'][0]['longitude'] #tager longitude fra decodeddatadict
				return latitude, longitude #returnere latitude og longitude
		else:
			fails = fails+1
			findkoordinater(lokation,fails)

#list = ["Rosenthaler Str. 36","Rosa-Luxemburg-Straße 49","52.499846,13.270597","københavn"]
#for lists in list:
	#findkoordinater(lists,0)
