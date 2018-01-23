#!/usr/bin/python
#
import urllib2
import re

## Open Connection ##
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
website = urllib2.urlopen('http://www.example.com/')
website_html = website.read()

## Output of oururl to file ##
with open("Output.txt", "w") as text_file:
    text_file.write("Purchase Amount: %s" % website_html)

## IP Addresss finder ##
#theIP = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
#ip = re.search(theIP, str(html))

## Country finder ##
#roughCountry = re.compile('([A-Z]\w+)( [A-Z]\w+){0,2}(?=\<\/a\>\s\s)')
#Country = re.search(roughCountry, str(html))

## Print out ##
print "Your IP is:", ip
print "Your Country is:", Country
