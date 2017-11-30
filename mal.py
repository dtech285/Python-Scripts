import requests
from prettyprint import pp_json


params = {'api_key': 'B8316F985C61539D360EAA8E21801B4CA16543AA6E924D7A3166B19C54B32C7E', 'ip': '59.38.35.243'}
response = requests.get('https://www.malwares.com/api/v2/ip/info', params=params)
response_json = response.json()
pp_json(response_json)
