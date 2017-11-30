#!/usr/bin/env python3

import sys

ArgLength = len(sys.argv)
IpAddressList = []

# Populate the IP address list
for x in range(ArgLength):
    IpAddressList.append(sys.argv[x])


del IpAddressList[0]
IpAddr = 0

for IpAddr in IpAddressList:
    print(IpAddr)
# print the list
