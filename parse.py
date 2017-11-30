#!/usr/bin/env python3

import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-hv', help='hash value')
parser.add_argument('-a', help='IP address')
parser.add_argument('-p', help='Port Number')

#parser.add_argument('--foo', help='foo help')
args = parser.parse_args()


print(args)

print("TEST")
