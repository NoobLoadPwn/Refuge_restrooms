import http.client, urllib.parse
from pprint import pprint
import json


def findkoordinater(lokation):
	conn = http.client.HTTPConnection('api.positionstack.com')#definerer hvilken api den skal gå ind

	params = urllib.parse.urlencode({#tildeler nødvendige parametre
		'access_key': '954f1d2dd6ec71f9e71b8ba50194fa7d',#bruger acces kodenfor at få adgang til api
		'query': lokation,#sætter parameteren til at være det samme som den givede data
		'limit': 1,
		})

	conn.request('GET', '/v1/forward?{}'.format(params)) #kalder inputtet fra apien, med de rigtige parametre
	res = conn.getresponse()#får response (denne del aer mere sikkerhed end nødvendig)
	data = res.read() #læser reponsen, og dermed får dataen, fra at kalde apien.
	decodeddata = data.decode('utf-8') #sætter data til rigtig datatype altså string, for at programmet kan læse det.
	decodeddatadict = json.loads(decodeddata) #bruger json til at lave string om til dictionaries, for at kunne plukke de rigtige dele af data.

	latitude = decodeddatadict['data'][0]['latitude'] #tager latitude fra decodeddatadict
	longitude = decodeddatadict['data'][0]['longitude'] #tager longitude fra decodeddatadict

	return latitude, longitude #returnere latitude og longitude
