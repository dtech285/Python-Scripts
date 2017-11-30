#!/usr/bin/env python3
import ipaddress

def validate_ip(IP_ADDR):
    #ipaddress.ip_address(IP_ADDR)
    if ipaddress.ip_address(IP_ADDR):
        print("GOOD")
    else:
        print("BAD")
    print("DONE")

IP_ADDR = input("Enter IP Address: ")

validate_ip(IP_ADDR)





#
#try:
#    socket.inet_aton(IP_ADDR)
#    print (IP_ADDR, " IS A VALID IP")
#except socket.error:
#print("INVALID IP")
