num=int(input("Enter the Final Number:"))
a=c=sum=0
b=1
print(a,b,sep=' ',end=' ')
while(b<num):
    if((a+b)>num):
        break
    else:
        c=a+b
        a=b
        b=c
        print(c,sep=' ',end=' ')
        if(b%2==0 and b<=num):
            sum=sum+b
print("\nThe Sum of Even Valued Terms upto",num,"=",sum)