def computepay(a,b):
    if(a<=40):
        x=a*b
        return x
    else:
        x=40*b+(a-40)*1.5*b
        return x
hrs=input("Enter hours:")
try:
    h=float(hrs)
except:
    print("Error")
    quit()
rate=input("Enter Rate:")
try:
    r=float(rate)
except:
    print("Error")
    quit()
y=computepay(h,r)
print(y)
