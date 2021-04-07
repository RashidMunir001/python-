import re
fname=input("Enter name of file:")
fhand=open(fname)
count=0
sum=0
lst=list()
for line in fhand:
      x=re.findall('[0-9]+',line)

      for y in x:
          sum=sum+int(y)
          count=count+1
print(sum)
print(count)
