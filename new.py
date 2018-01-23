#!/usr/bin/python
#
from json import load
from urllib2 import urlopen
import requests

## Get IP ##
my_ip = urlopen('http://www.ipchicken.com/')
print my_ip

## Get Geolocation ##
#geo = requests.get('http://ipinfo.io/%s/country' % my_ip)
#print geo
