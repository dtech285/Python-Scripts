#!/usr/bin/env python3

import subprocess, time, webbrowser, os, sys
import ipaddress

ArgLength = len(sys.argv)
IpAddressList = []
delay = 1

# Populate the IP address list
for x in range(ArgLength):
    IpAddressList.append(sys.argv[x])

# drop the script name from the list
del IpAddressList[0]

#==============================================
# Function: launch_web
#==============================================
# create the string
def launch_web(IpAddr):
    # dictionary to hold URLs
    sites = {'virustotal': 'cmd /c start chrome https://www.virustotal.com/en/ip-address/{}/information/ --new-window'.format(IpAddr),
            'tcpiputils': 'cmd /c start chrome https://www.tcpiputils.com/browse/ip-address/{} --new-tab'.format(IpAddr),
            'ipindetail': 'cmd /c start chrome http://ipindetail.com/ip-lookup/{}.html --new-tab'.format(IpAddr),
            'mxtoolbox': 'cmd /c start chrome https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a{}&run=toolpage/ --new-tab'.format(IpAddr),
            'ransomwaretracker': 'cmd /c start chrome https://ransomwaretracker.abuse.ch/ip/{} --new-tab'.format(IpAddr),
            'threatminer': 'cmd /c start chrome https://www.threatminer.org/host.php?q={} --new-tab'.format(IpAddr),
            'threatcrowd': 'cmd /c start chrome https://www.threatcrowd.org/ip.php?ip={} --new-tab'.format(IpAddr),
            'abuseipdb': 'cmd /c start chrome https://www.abuseipdb.com/check/{} --new-tab'.format(IpAddr),
            'feodotracker': 'cmd /c start chrome https://feodotracker.abuse.ch/host/{} --new-tab'.format(IpAddr),
            'malwares': 'cmd /c start chrome https://www.malwares.com/report/ip?ip={} --new-tab'.format(IpAddr),
            'abuseat': 'cmd /c start chrome https://www.abuseat.org/lookup.cgi --new-tab',
    }

    # loop through dictionary and pass the url to investigate function
    for site, url in sites.items():
        investigate(url)

#==============================================
# Function: launch_web
#==============================================
# opens browser with url
def investigate(url):
    global delay
    subprocess.Popen(url, shell=False)
    time.sleep(delay)


# ----- End function: launch_web -----

#==============================================
# Function: validate_ip
#==============================================
# validate the input ip address
def validate_ip(IpAddr):
    #ipaddress.ip_address(IP_ADDR)
    if ipaddress.ip_address(IpAddr):
        launch_web(IpAddr)
        #print("GOOD")
    else:
        print("BAD")
    #print("DONE")

# ----- End function: launch_web -----

for IpAddr in IpAddressList:
    validate_ip(IpAddr)
    #print(IpAddr)
    #launch_web(IpAddr)
