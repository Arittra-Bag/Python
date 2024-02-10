n=int(input("Enter the Number: "))
c=len(str(n))
num=n
sum=0
for i in range(c):
    temp=num%10
    sum+=temp**c
    num=num//10
if(sum==n):
    print("It is an Armstrong Number")
else:
    print("It is Not an Armstrong Number")  