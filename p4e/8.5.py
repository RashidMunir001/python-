#mbox-short.txt with lists
fname=input("enter file name:")
fh=open(fname)
cont_set=set(fh)
count=0

for line in cont_set:

            if line.startswith("From"):
                if line.startswith("From:"):
                  continue
                else:
                     words=line.strip().split()
                     print(words[1])
                     count+=1



print("There were", count, "lines in the file with From as the first word")
