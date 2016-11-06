#!/usr/bin/python
# Script to validate VPN connection and Country
# Troy Wilson
# Date: 1-28-2016
#
import urllib2
import re

## Open Connection ##
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
url = ('http://www.ip-lookup.net')
oururl = opener.open(url).read()

## IP Addresss finder ##
theIP = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}')
ip = re.search(theIP, oururl)

## Country finder ##
roughCountry = re.compile('([A-Z]\w+)( [A-Z]\w+){0,2}(?=\<\/a\>\s\s)')
Country = re.search(roughCountry, oururl)

## Print out ##
print "Your IP is:", ip.group()
print "Your Country is:", Country.group()
