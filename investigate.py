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
    site1 = "cmd /c start chrome https://www.virustotal.com/en/ip-address/" + IpAddr + "/information/ --new-window"
    site2 = "cmd /c start chrome https://www.tcpiputils.com/browse/ip-address/" + IpAddr + " --new-tab"
    site3 = "cmd /c start chrome http://ipindetail.com/ip-lookup/" + IpAddr + ".html --new-tab"
    site4 = "cmd /c start chrome https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a" + IpAddr + "&run=toolpage/ --new-tab"
    site5 = "cmd /c start chrome https://ransomwaretracker.abuse.ch/ip/" + IpAddr + " --new-tab"
    site6 = "cmd /c start chrome https://www.threatminer.org/host.php?q=" + IpAddr + " --new-tab"
    site7 = "cmd /c start chrome https://www.threatcrowd.org/ip.php?ip=" + IpAddr + " --new-tab"
    site8 = "cmd /c start chrome https://www.abuseipdb.com/check/" + IpAddr + " --new-tab"
    site9 = "cmd /c start chrome https://feodotracker.abuse.ch/host/" + IpAddr + " --new-tab"
    site10 = "cmd /c start chrome https://www.malwares.com/report/ip?ip="+ IpAddr + "--new-tab"
    site11 = "cmd /c start chrome https://www.abuseat.org/lookup.cgi --new-tab"
    subprocess.Popen(site1, shell=False)
    time.sleep(delay)
    subprocess.Popen(site2, shell=False)
    time.sleep(delay)
    subprocess.Popen(site3, shell=False)
    time.sleep(delay)
    subprocess.Popen(site4, shell=False)
    time.sleep(delay)
    subprocess.Popen(site5, shell=False)
    time.sleep(delay)
    subprocess.Popen(site6, shell=False)
    time.sleep(delay)
    subprocess.Popen(site7, shell=False)
    time.sleep(delay)
    subprocess.Popen(site8, shell=False)
    time.sleep(delay)
    subprocess.Popen(site9, shell=False)
    time.sleep(delay)
    subprocess.Popen(site10, shell=False)
    time.sleep(delay)
    subprocess.Popen(site11, shell=False)

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
