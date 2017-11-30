#!/usr/bin/env python3

import os, sys
from investigate import launch_web, validate_ip
from port import validate_port
from hash import validate_hash

#-------------------------------------------------------
# FUNCTIONS
#-------------------------------------------------------
def ip_address():
    IpAddr = input("Enter an IP Address: ")
    validate_ip(IpAddr)

def file_hash():
    file_hash = input("Enter a file hash: ")
    validate_hash(file_hash)

def port_number():
    PortNumber = input("Enter a port number: ")
    validate_port(PortNumber)


#-------------------------------------------------------

ans=True
while ans:
    os.system('cls')
    print("\n\nINVESTIGATION MENU")
    print("""
    1. IP Address Investigation
    2. File Hash lookup
    3. Port Number lookup
    4. Quit
    """)
    ans = input("Enter choice: ")
    if ans == "1":
        ip_address()

    elif ans == "2":
        file_hash()

    elif ans=="3":
        port_number()

    elif ans=="4":
        break

    else:
       print("\n Not Valid Choice Try again")
