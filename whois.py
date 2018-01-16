#!/usr/bin/env python3
import sys

# Open the txt file and put addresses in list
IpAddressList = []

with open('addresses.txt') as f:
    # step through file
    for line in f:
        address = line.strip() # strip carriage return
        IpAddressList.append(address)
f.closed
#print(IpAddressList)
for IpAddr in IpAddressList:
    #print(IpAddr)
