import requests, sys
from prettyprint import pp_json

HashValue = sys.argv[1]
params = {'apikey': '7d295c9e6cf99249731908b52eb274f45032ff3126dee4b01e340d486c7a87c4', 'resource': HashValue}
headers = {
  "Accept-Encoding": "gzip, deflate",
  "User-Agent" : "gzip,  My Python requests library example client or username"
  }
response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
  params=params, headers=headers)
json_response = response.json()
#print(json_response)
pp_json(json_response)
