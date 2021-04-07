#this is customized version of dr.chuck json2.py
#here have to get input from user and extract comment coounts from it
import urllib.request,urllib.parse
import json
url=input("Enter Location:")
print("Retrieving URL:",url)
connection=urllib.request.urlopen(url)
data=connection.read().decode()
js=json.loads(data)
print(json.dumps(js, indent=4))
sum=0
count=0
#y=0
 #for i in data:
#      x=len(i)
#      y= y+x

print('characters',len(data))
for u in js['comments']:
              s=u['count']
              sum=sum+s
              count+=1
print('count:',count)
print('sum',sum)
