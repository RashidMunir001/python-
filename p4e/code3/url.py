# to access web data ,scrap href at certain position after getting input (position) from user


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url- ')
position=int(input('Enter position'))
count=int(input('Enter repetitions'))


print('Retreving: %s' % url)
for i in  range(0,count):
         html = urllib.request.urlopen(url, context=ctx).read()
         soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
         tags = soup('a')
         p=0
         c=0
         for tag in tags:
             c+=1
             if c==position:
               print('Retreving: %s' % str(tag.get('href',None)))
               url=str(tag.get('href',None))
               c=0
               break
         #print('Last name in sequence is',s[position-1])
         #print('Last name in sequence is',t[position-1])
