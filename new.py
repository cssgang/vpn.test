#!/usr/bin/python
#
import urllib2
import requests
import re

## Get IP ##
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
my_ip = opener.open('http://ipchickenhawk.com/')
my_ip =  my_ip.read()
iplist = re.findall( r'[0-9]+(?:\.[0-9]+){3}', my_ip ) [0]


print iplist

## Get Geolocation ##
#geo = requests.get('http://ipinfo.io/%s/country' % my_ip)
#print geo
