# test website: http://py4e-data.dr-chuck.net/comments_42.json
# sum = 2553

# website: http://py4e-data.dr-chuck.net/comments_253731.json
# sum ends with 29

import json
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, "html.parser")

info = json.loads(data)
#print('User count:', len(info))
total = 0

for comment in info["comments"]:
    total += comment["count"]
print(total)
