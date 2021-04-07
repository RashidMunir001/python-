# reading.opening a file and then deal it as an dictionery
fname=input("enter name of file")
fhand=open(fname)
sss=dict()
for line in fhand:
    if line.startswith("From"):
        if line.startswith("From:"):
            words=line.rstrip().split()

            for word in words[1:3]:
                if word in sss:
                    sss[word]=sss[word] +1
                else:
                    sss[word]=1
bigcount=None
bigword=None
for word,count in sss.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=word
print(bigword,bigcount)
#big successs for you rashid,solved yourself ,how to show string line in list and then into dictionery
#and then split some portion and check how kuch repeated(histogram)
