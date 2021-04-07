#simple arrays print names using for loop
names=['rashid','taimoor','awais','hassan','zain']
for name in names:
        print(name)

print("rashid's brothers and nephew", name)

# simple using built in sum function for sum of arrays and length  of array
numbers=[1,2,3,4,5,6,7,8,9,1,12,34,56,78,11,23]
print("sum of list is",sum(numbers))

print("length of list is",len(numbers))

#to find largest and smallest from following List
largest=None
print("before",largest)
for n in [2,66,87,90,34,6677,32,1,0,32]:
 if largest is None or n > largest:
   largest=n
print("still largest",n ,largest)
print("largest is",largest)

smallest= None
print("before",None)
for n in [1,2,3,4,5,6,8,9,0,1/10,0.99]:
    if smallest is None or n < smallest:
        smallest=n
    print("smallest is ",n,smallest)
print("smallets of all is", smallest)

#program to count ,find avg and total of input numbers by user
num=0
total=0
while True:
   number=input("ente a number")
   if number=='done':
    break
   try:
    num1=float(number)
   except:
     print("please enter numeric or done")
     continue
   num=num+1
   total=total+num1


print("all done")
print("total,count and avg is",total,num,total/num)
