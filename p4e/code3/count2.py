import string
import json
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

#print(counts)
count=0
#for k,v in counts.items():
mylist=list(counts.keys())
print(mylist)
for i in mylist:
        z=len(i)
        count=count+z

print("sum of all occurences of characters is:", sum(counts.values()))
print("sum of length of all keys:",count)
