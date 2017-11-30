import subprocess, time, webbrowser, os, sys

ArgLength = len(sys.argv)
PortNumberList = []
delay = 1

# Populate the IP address list
for x in range(ArgLength):
    PortNumberList.append(sys.argv[x])

# drop the script name from the list
del PortNumberList[0]


def launch_web(PortNumber):
    site1 = "cmd /c start chrome https://www.speedguide.net/port.php?port=" + PortNumber + "--new-window"
    subprocess.Popen(site1, shell=False)
    time.sleep(delay)

def validate_port(PortNumber):
    launch_web(PortNumber)
    # to validate - is in range 0-65,000 and is numeric


# ----- End function: launch_web -----

for PortNumber in PortNumberList:
    validate_port(PortNumber)
