# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fhand=open(fname)
except:
    print("you have entered incorrect/bad file name")
    quit()
lines=fhand.read()
lines=lines.upper()
lines=lines.rstrip()
print(lines)
