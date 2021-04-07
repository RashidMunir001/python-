import sys

name = sys.arg[1]
handle = open(name, 'r')
text = handle.read()
print(name, 'is', len(text), 'bytes')
