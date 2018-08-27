import json,requests,argparse

API_KEY = '9feb66f70f86c39a1d2214009bf703dd'

ENDPOINT = 'http://api.openweathermap.org/data/2.5/weather?q='


def getWeather(cityname=None):
	if not (cityname):
		cityname = 'Orlando'
	cw_endpoint = '%s%s&APPID=%s' % (ENDPOINT,cityname,API_KEY)
	cw_header = {'Content-Type': 'application/json'}
	r = requests.get(cw_endpoint, headers=cw_header)
	response = json.loads(r.text)
	if response['cod'] == 200:
		output = "Location/City Name:%s\nLongitude:%s\nLatitude:%s\nWind Speed:%s\nWeather Description:%s\nMaximum Temperature:%s\nMinimum Temperature:" % (response['name'],response['coord']['lon'],response['coord']['lat'],response['wind']['speed'],response['weather'][0]['description'],response['main']['temp_min'],response['main']['temp_max'])
	elif response['cod'] == 404:
		output = 'City not found: try typing it differently or capturing in quotes \"'
	elif response['cod'] == 429:
		output = 'Too many API calls - please wait for 10min so my app isn\'t blocked!'
	else:
		output = 'Sorry, API returned a %s' % response['cod']

	"""
	#EXAMPLE response
	{
		'coord': {
			'lon': -122.42, 'lat': 37.78
			},
		'weather': [
			{'id': 711, 'main': 'Smoke', 'description': 'smoke', 'icon': '50n'},
			{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50n'}
		],
		'base': 'stations',
		'main': {
			'temp': 289.69,
			'pressure': 1016,
			'humidity': 87,
			'temp_min': 286.15,
			'temp_max': 292.05
		},
		'visibility': 16093,
		'wind': {
			'speed': 2.1, 'deg': 200
		},
		'clouds': {
			'all': 90
		},
		'dt': 1535341200,
		'sys': {
			'type': 1,
			'id': 392,
			'message': 0.004, 
			'country': 'US',
			'sunrise': 1535376945,
			'sunset': 1535424345
		},
		'id': 5391959,
		'name': 'San Francisco',
		'cod': 200
	}
	"""
	print(response)

if __name__ == '__main__':
    # parse command-line arguments
    parser = argparse.ArgumentParser(description='Get the Weather')
    parser.add_argument('-cw', '--cityweather',
                         help='get the weather for a city, enter \'CITYNAME\' or \'CITYNAME,STATENAME\'')
    args = parser.parse_args()
    vargs = vars(args)
    if args.cityweather:
    	getWeather(args.cityweather)
    print('Done')