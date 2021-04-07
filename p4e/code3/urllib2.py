import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
counts=dict()
for line in fhand:
    words=line.decode().strip()
    for word in words:
        counts[words]=counts.get(word,0)+1

print(counts)
