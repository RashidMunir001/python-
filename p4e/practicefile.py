
fname=input("Enter name of file")
fh=open(fname)
counts=0
lst=list()
for line in fh:
     if line.startswith("From "):
               num=line.split()
               counts=counts+int(num[4])

print("total counts is :",counts)
