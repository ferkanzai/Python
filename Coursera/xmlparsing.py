# webs to use as inputs:
# http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553) 
# http://py4e-data.dr-chuck.net/comments_253730.xml (Sum ends with 34)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read()
#print(data)
tree = ET.fromstring(data)
#print(tree)

counts = tree.findall('comments/comment/count')
total = 0

for count in counts:
    total += int(count.text)
print(total)