import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1488128.json (Sum ends with 37)


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
fhand = urllib.request.urlopen(address)

data = fhand.read().decode()
info = json.loads(data)
#print(info)
#print('User count:', len(info))
#print(info['note'])
results_list = []
for item in (info['comments']):
    results_list.append(int(item['count']))
print(sum(results_list))