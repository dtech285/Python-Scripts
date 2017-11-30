
import subprocess, time, webbrowser, os, sys
import ipaddress

ArgLength = len(sys.argv)
IpAddressList = []
delay = 1
IpAddr = "8.8.8.8"

sites = {
    'site1': "cmd /c start chrome https://www.virustotal.com/en/ip-address/" + IpAddr + "/information/ --new-window",
    'site2': "cmd /c start chrome https://www.tcpiputils.com/browse/ip-address/" + IpAddr + " --new-tab",
    'site3': "cmd /c start chrome http://ipindetail.com/ip-lookup/" + IpAddr + ".html --new-tab",
    'site4': "cmd /c start chrome https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a" + IpAddr + "&run=toolpage/ --new-tab",
    'site5': "cmd /c start chrome https://ransomwaretracker.abuse.ch/ip/" + IpAddr + " --new-tab",
    'site6': "cmd /c start chrome https://www.threatminer.org/host.php?q=" + IpAddr + " --new-tab",
    'site7': "cmd /c start chrome https://www.threatcrowd.org/ip.php?ip=" + IpAddr + " --new-tab",
    'site8': "cmd /c start chrome https://www.abuseipdb.com/check/" + IpAddr + " --new-tab",
    'site9': "cmd /c start chrome https://feodotracker.abuse.ch/host/" + IpAddr + " --new-tab",
    'site10': "cmd /c start chrome https://www.malwares.com/report/ip?ip="+ IpAddr + "--new-tab",
    'site11': "cmd /c start chrome https://www.abuseat.org/lookup.cgi --new-tab"
    }

def launch_browser(site):
    site = site
    delay = 1
    subprocess.Popen(site, shell=False)
    time.sleep(delay)

for site, v in sites.items():
    #print(site + " - " + v)
    launch_browser(v)
