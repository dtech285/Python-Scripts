import subprocess, time, webbrowser, os, sys

ArgLength = len(sys.argv)
HashList = []
delay = 1

# Populate the IP address list
for x in range(ArgLength):
    HashList.append(sys.argv[x])

# drop the script name from the list
del HashList[0]

def launch_web(Hash):
    site1 = "cmd /c start chrome https://www.virustotal.com/#/file/" + Hash + "/detection --new-window"
    site2 = "cmd /c start chrome https://www.malwares.com/report/file?hash=" + Hash + "--new-tab"
    subprocess.Popen(site1, shell=False)
    time.sleep(delay)
    subprocess.Popen(site2, shell=False)
    time.sleep(delay)


def validate_hash(Hash):
    launch_web(Hash)
    # to validate - is in range 0-65,000 and is numeric

# ----- End function: launch_web -----

for Hash in HashList:
    validate_hash(Hash)
