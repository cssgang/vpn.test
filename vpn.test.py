#!/usr/bin/python
#Date: 1.23.18
import urllib2
import re
import requests

## Get IP ##
OPENER = urllib2.build_opener()
OPENER.addheaders = [('User-agent', 'Mozilla/5.0')]
MY_IP = OPENER.open('http://ipchicken.com/')
MY_IP = MY_IP.read()
IP = re.findall(r'[0-9]+(?:\.[0-9]+){3}', MY_IP)[0]
print "IP Address: %s" % IP

## Get GeoLOCation - Country ##
GEO_LO = requests.get('http://ipinfo.io/%s/country' % IP)
LOC = str(GEO_LO.content).rstrip()
print "Country: %s" % LOC

## Get GeoLOCation - City ##
GEO_REGION = requests.get('http://ipinfo.io/%s/region' % IP)
REGION = str(GEO_REGION.content).rstrip()
print "Region: %s" % REGION
