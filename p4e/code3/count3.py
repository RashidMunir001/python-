import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)


fname=input("Enter name of file")
fh=open(fname)
counts=0
for line in fh:
     if line.startwith("Received:"):
               num=line.split()[2]
               num=counts+len(num)
print("total counts is :",num)
