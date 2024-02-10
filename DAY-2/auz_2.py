p=float(input("Enter Principal:"))
t=float(input("Enter Time:"))
if p<200000:
    r=10
    si=(p*r*t)/100
    print("The Simple Interest is:",si)
elif p>200000 and p<1000000:
    r=12
    si=(p*r*t)/100
    print("The Simple Interest is:",si)
else:
    r=15
    si=(p*r*t)/100
    print("The Simple Interest is:",si)