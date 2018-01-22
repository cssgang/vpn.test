#!/usr/bin/python
#
from bs4 import BeautifulSoup
import urllib2
import re

## Open Connection ##
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
oururl = opener.open('http://www.ip-lookup.net')

## IP Addresss finder ##
theIP = re.compile(r"d{1,3}.d{1,3}.d{1,3}.d{1,3}")
ip = re.search(theIP, str(oururl))

## Country finder ##
roughCountry = re.compile('([A-Z]\w+)( [A-Z]\w+){0,2}(?=\<\/a\>\s\s)')
Country = re.search(roughCountry, str(oururl))

## Print out ##
print "Your IP is:", ip
print "Your Country is:", Country
