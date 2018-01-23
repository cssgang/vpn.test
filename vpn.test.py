#!/usr/bin/python
#
import urllib
import urllib2
import re

## Open Connection ##
url = 'http://www.ip-look up.net'
user_agent = 'Mozilla/5.0'
headers = {'User-Agent':user_agent}

req = urllib2.Request(url, headers)
response = urllib2.urlopen(req)
the_page = response.read()


#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
#opener.addheaders = [('User-agent', 'Mozilla/5.0')]
#website = urllib2.urlopen('http://www.ip-lookup.net')
#website_html = website.read()

## Output of oururl to file ##
with open("Output.txt", "w") as text_file:
    text_file.write(the_page)

## IP Addresss finder ##
#theIP = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
#ip = re.search(theIP, str(html))

## Country finder ##
#roughCountry = re.compile('([A-Z]\w+)( [A-Z]\w+){0,2}(?=\<\/a\>\s\s)')
#Country = re.search(roughCountry, str(html))

## Print out ##
print "Your IP is:", ip
print "Your Country is:", Country
