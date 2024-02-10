num=int(input("Enter the Number:"))
temp=num
power=len(str(num))
sum=0
for i in range(power):
    c=temp%10
    sum+=c**power
    temp=temp//10
if num==sum:
    print("It is an Armstrong Number")
else:
    print("It is Not an Armstrong Number")