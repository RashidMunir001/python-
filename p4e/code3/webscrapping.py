# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen

from bs4 import BeautifulSoup
#import ssl

# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html =urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
count=0
sum=0
for i in tags:
    x=int(i.text)
    sum=sum+x
print(sum)
        #print("number:" ,tag.get(('span'), None)
#print(sum(tag))
