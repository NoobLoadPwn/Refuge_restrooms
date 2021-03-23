import http.client, urllib.parse
from pprint import pprint
import json


def findkoordinater(lokation):
    startlatitude=None
    endlatitude=None

    conn = http.client.HTTPConnection('api.positionstack.com')

    params = urllib.parse.urlencode({
        'access_key': '954f1d2dd6ec71f9e71b8ba50194fa7d',
        'query': lokation,
        'limit': 1,
        })

    conn.request('GET', '/v1/forward?{}'.format(params))

    res = conn.getresponse()
    data = res.read()

    decodeddata = data.decode('utf-8')

    decodeddatadict = json.loads(decodeddata)

    latitude = decodeddatadict['data'][0]['latitude']
    longitude = decodeddatadict['data'][0]['longitude']

    return latitude, longitude

print (findkoordinater('Copenhagen'))
