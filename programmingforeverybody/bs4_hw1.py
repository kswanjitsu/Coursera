# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1488125.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#print(soup)

# Retrieve all of the anchor tags
final_list = []
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    x = re.findall('[0-9]+', str(tag))
    for i in x:
        final_list.append(int(i))

print(sum(final_list))