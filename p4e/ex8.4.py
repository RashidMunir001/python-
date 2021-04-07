#program for lists
fname=input("enter name of file:")
fh=open(fname)
lst=list()
for line in fh:
    words=line.rstrip().split()
    for element in words:
        if element in lst:
            continue
        else:
         lst.append(element)
lst.sort()
print(lst)
