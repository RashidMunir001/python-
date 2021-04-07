#numlist = list()
#while (True):
#    inp = input('Enter a number: ')
#    if inp == 'done': break
#    value = float(inp)
#    numlist.append(value)
#print(numlist)
#average = sum(numlist) / len(numlist)
#print('Average:', average)


numlst= list()
total=0
count=0
while (True):
       num=input("Enter a num for list:")
       if num=="done":break
       value=float(num)
       total=total+value
       count+=1
       numlst.append(value)
print(numlst)
avg=total/count
print("number are :",count)
print("avg is:",avg)
