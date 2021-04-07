import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
lst=list()
dic=dict()
cnt=0
for line in fhand:
    words=line.decode().strip()
    lst.append(words)
    for word in words:
         dic[words]=dic.get(word,0)+1
        #to get each single word in dic,but have to write split() than strip() ,dic[word]=dic.get(word,0)+1
#print(dic)
for k,v in dic.items():
    print(k,v)
print('this is list',lst)
#print('this is dictionery',dic.items())
