import subprocess, time, webbrowser, os, sys

ArgLength = len(sys.argv)
UrlList = []
delay = 1

# Populate the IP address list
for x in range(ArgLength):
    UrlList.append(sys.argv[x])

# drop the script name from the list
del UrlList[0]

def launch_web(RequestURL):
    site1 = "cmd /c start chrome http://www.urlvoid.com/scan/" + RequestURL + "/ --new-window"
    site2 = "cmd /c start chrome https://sitecheck.sucuri.net/results/" + RequestURL + " --new-tab"
    subprocess.Popen(site1, shell=False)
    time.sleep(delay)
    subprocess.Popen(site2, shell=False)
    time.sleep(delay)


def validate_url(RequestURL):
    launch_web(RequestURL)
    # to validate - is in range 0-65,000 and is numeric

# ----- End function: launch_web -----

for Hash in UrlList:
    validate_url(RequestURL)
