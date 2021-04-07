#
import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET

url=input('Enter location')
print("Retreving ", url)

xml=urllib.request.urlopen(url).read()
Tree=ET.fromstring(xml)

lst=Tree.findall('comments/comment')
sum=0
count=0
for item in lst:
     y=item.find('count').text
     sum=sum+int(y)
     count+=1
print('Retreived' + str(count) + 'characters')
x=lst.count(item)
print('Sum',sum)
print('count:',item)
print(lst.count(x))
