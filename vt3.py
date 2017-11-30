#!/usr/bin/env python3
import json, urllib
import urllib.request
import urllib.parse
from prettyprint import pp_json



"""
Submits single IP entry to VT IP scanner API and returns total AV detected file results
With public API only 4 requests/min are allowed. You will get an email registered to the account
if you repeatedly violate this threshold
"""

#Asks for user input of an IP and converts to a string for passing to virustotal
ipaddress = input('Enter an IP address to scan: \n')
ipaddress = str(ipaddress)

#Virus total API info
url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
parameters = {'ip': ipaddress,
              'apikey': '7d295c9e6cf99249731908b52eb274f45032ff3126dee4b01e340d486c7a87c4'} ##### ENTER YOUR VIRUSTOTAL API KEY HERE #####

#URL encoding, IP submission, and json response storage
response = urllib.request.urlopen('%s?%s' % (url, urllib.parse.urlencode(parameters))).read()
response_dict = json.loads(response)

pp_json(response_dict)
