#!/usr/bin/env python

import json
import urllib.request
import urllib.parse

url = 'https//www.virustotal.com/vtapi/v2/ip-address/report'
parameters = {'ip': '90.156.201.27', 'apikey': '7d295c9e6cf99249731908b52eb274f45032ff3126dee4b01e340d486c7a87c4'}
#response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
response = urllib.request.urlopen(url, urllib.parse.urlencode(parameters)).read()
response_test = json.loads(response)
print(response_test)
