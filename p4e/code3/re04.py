# Search for lines that start with From and have an at sign
import re
count=0
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)
        count=count+1
print(count)
