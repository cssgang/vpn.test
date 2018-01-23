#!/usr/bin/python
#
from json import load
from urllib2 import urlopen

## Get IP ##
my_ip = load(urlopen('http://httpbin.org/ip'))['origin']
print my_ip
