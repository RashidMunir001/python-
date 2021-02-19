hrs = input("Enter Hours:")
r=input("enter rate per hour")
try:
    h = float(hrs)
    rph=float(r)
except:
    print("error enter  numeric")
    quit()
print(h,rph)
if h<=40:
    a=h*rph;

    print("your pay" , a)
elif h>40:
    z=(h-40)*(1.5*rph)+40*rph
    print("pay is" , z)
#this following is  regaraded true by p4e editor tool
hrs = input("Enter Hours:")
r=input("enter rate per hour")
try:
    h = float(hrs)
    rph=float(r)
except:
    print("error enter  numeric")
    quit()

if h<=40:
    print(h*rph)
elif h>40:
    print((h-40)*(1.5*rph)+40*rph)
