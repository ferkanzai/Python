# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# website to use: http://py4e-data.dr-chuck.net/known_by_Rahman.html 
# count: 7 and position: 18

# test website: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# count: 4 and position: 3

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input("Enter count: "))
pos = int(input("Enter position: ")) - 1
print("Retrieving: ", url)
name = ""
# Retrieve all of the anchor tags
tags = soup('a')
#print(tags[2].get('href', None))
#for tag in tags:
#    print(tag.get('href', None))

new_url = tags[pos].get('href', None)
for i in range(count):
    print("Retrieving: ", new_url)
    html = urllib.request.urlopen(new_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    new_tags = soup('a')
    if i == count - 1:
        names = re.findall('by_(.+)\.', new_url)
    new_url = new_tags[pos].get('href', None)
for name in names:
    print(name)
    