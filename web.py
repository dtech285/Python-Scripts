#!/usr/bin/env python3

import subprocess, time, webbrowser, os, sys

# time delay variable
delay = 1
print("============================================================================================")
print("Open v7 VCS/APS in the same IE Window")
print("============================================================================================\n\n")
# Open v7 VCS and APS web console in the same IE window
p = subprocess.Popen(["powershell.exe", 
              "C:\\Users\\dboyett\\Documents\\PowerShellScripts\\ieTest.ps1"], 
              stdout=sys.stdout)
p.communicate()
time.sleep(delay)

print("============================================================================================")
print("Open v6 VCS/APS in same Chrome window")
print("============================================================================================\n\n")
# Open v6 VCS and APS web console in the same window
v6_Vcs_Monitor = "cmd /c start chrome https://support.omnijoin.com/_admin/VcsMonitor.aspx --new-window"
v6_Aps_Monitor = "cmd /c start chrome https://support.omnijoin.com/_admin/ApsMonitor.aspx --new-tab"
subprocess.Popen(v6_Vcs_Monitor,shell=True)
time.sleep(delay)
subprocess.Popen(v6_Aps_Monitor,shell=True)
time.sleep(delay)

print("============================================================================================")
print("Open v7 WPC and Backend webconsoles in separate Chrome window")
print("============================================================================================\n\n")
# Open v7 WPC and Backend web consoles
v7_WPC_Monitor = "cmd /c start chrome https://v7.omnijoin.com/_admin/WpcMonitor.aspx --new-window"
v7_Backend_Monitor = "cmd /c start chrome https://v7.omnijoin.com/_admin/BackendServerMonitor.aspx --new-tab"
subprocess.Popen(v7_WPC_Monitor,shell=True)
time.sleep(delay)
subprocess.Popen(v7_Backend_Monitor,shell=True)
time.sleep(delay)

print("============================================================================================")
print("Open v6 WPC and Backend webconsoles in separate Chrome window")
print("============================================================================================\n\n")
# Open v6 WPC and Backend web consoles
v6_WPC_Monitor = "cmd /c start chrome https://support.omnijoin.com/_admin/WpcMonitor.aspx --new-window"
v6_Backend_Monitor = "cmd /c start chrome https://support.omnijoin.com/_admin/BackendServerMonitor.aspx --new-tab"
subprocess.Popen(v6_WPC_Monitor,shell=True)
time.sleep(delay)
subprocess.Popen(v6_Backend_Monitor,shell=True)
time.sleep(delay)

print("============================================================================================")
print("Open testbuild VCS/APS/Backend/WPC in same Chrome window")
print("============================================================================================\n\n")
# Open testbuild VCS and APS web console in the same window
Testbuild_Vcs_Monitor = "cmd /c start chrome https://v7.ojtestbuild.com/_admin/SystemStatus.aspx --new-window"
Testbuild_Aps_Monitor = "cmd /c start chrome https://v7.ojtestbuild.com/_admin/SystemStatus.aspx --new-tab"
Testbuild_WPC_Monitor = "cmd /c start chrome https://v7.ojtestbuild.com/_admin/WpcMonitor_.aspx --new-tab"
Testbuild_Backend_Monitor = "cmd /c start chrome https://v7.ojtestbuild.com/_admin/BackendServerMonitor.aspx --new-tab"
#time.sleep(delay)
subprocess.Popen(Testbuild_Vcs_Monitor,shell=True)
time.sleep(delay)
subprocess.Popen(Testbuild_Aps_Monitor,shell=True)
time.sleep(delay)
subprocess.Popen(Testbuild_WPC_Monitor,shell=True)
time.sleep(delay)
subprocess.Popen(Testbuild_Backend_Monitor,shell=True)

print("============================================================================================")
print("DONE")
print("============================================================================================\n\n")
