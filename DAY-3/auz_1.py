num=int(input("Enter the Number:"))
if(num==0 or num==1):
    print("It is neither Prime nor Composite")
elif num==2:
    print("It is a Prime Number")
else:
    for i in range(2,num):
        if num%i==0:
            print("It is a Composite Number")
            break
        else:
            print("It is a Prime Number")
            break