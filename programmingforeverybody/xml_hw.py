import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_1488127.xml


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
fhand = urllib.request.urlopen(address)
data = fhand.read()
data = data.decode()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
sum_list = []
for i in counts:
    j = int(i.text)
    sum_list.append(j)
print(sum(sum_list))

