
try:
    hrs = input("Enter Hours :")
    rph=input(" enter rate per hour")
    fh=float(hrs)
    frph=float(rph)
except:
    print("you have entered string, enter numerics")
    quit()
def computepay(fh,frph):
    if fh<=40:
             pay=fh*frph

    elif fh>40:

             extpay=(fh-40)*(1.5*frph)+ 40*frph
    return extpay

#from now on the program code submitted on py4e debugger by sir chuck,exactly same as above
p = computepay(fh,frph);
print("Pay",p)



try:
    hrs = input("Enter Hours of work :")
    rph=input(" enter rate per hour")
    fh=float(hrs)
    frph=float(rph)
except:
    print("you have entered string, enter numerics")
    quit()
def computepay(fh,frph):
    if fh<=40:
             pay=fh*frph

    else:

             extpay=(fh-40)*(1.5*frph)+ 40*frph
    return extpay


p = computepay(fh,frph)
print("Pay",p)
