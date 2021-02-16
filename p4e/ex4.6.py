def computepay(fh,frph):
    if fh<=40:
             extpay2=fh*frph

    elif fh>40:

             extpay3=(fh-40)*(1.5*frph)+ 40*frph
    return extpay3

try:
    hrs = input("Enter Hours:")
    rph=input(" enter rate per hour")
    fh=float(hrs)
    frph=float(rph)
except:
    print("you have entered string, enter numerics")
    quit()

p = computepay(45,10.50)
print("Pay",p)
