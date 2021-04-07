# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
   fh = open(fname)
except:
    print("you have entered incorrect file name")
    quit()
count=0
total=0
for lines in fh:

   if not lines.startswith('X-DSPAM-Confidence: '): continue
   count=count+1
   t=lines.find('0')
   num=float(lines[t:])
   total=total+num

avg=float(total/count)
print("Average spam confidence: ",avg)
