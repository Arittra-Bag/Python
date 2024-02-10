i=c=p=0
while(i>=0):
    num=int(input("Enter the Number:"))
    if num==-1:
        break
    elif num==1:
        continue
    else:
        for i in range(2,num):
            if num%i==0:
                c+=1
        else:
            p=p+1
print("Count of Prime No.s=",p)
print("Count of Composite No.s=",c)