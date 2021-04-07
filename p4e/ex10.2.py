#program to select specific string from line of a families
#then check its occurence  by using dic and lists
#thats is using dic get its key,value pair
#and then using list reverse its k,v to v,k and sort it as we need value not index


fname=input("enter name of file")
fhand=open(fname)
dic=dict()

for line in fhand:
              if line.startswith("From "):
                    words=line.split()[5].split(":")
                    dic[words[0]]=dic.get(words[0],0) +1


print(sorted(dic.items(), key=lambda x: x[0]))
temp=list()
for k,v in dic.items():
    temp.append((k,v))
temp.sort()
print("sorted",temp[:10])
for (k,v) in temp:
     print (k,v)
