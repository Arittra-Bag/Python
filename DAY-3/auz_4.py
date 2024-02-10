low=int(input("Enter the Lower Limit:"))
high=int(input("Enter the Lower Limit:"))
sum=0
for num in range(low,high+1):
    if(num==0 or num==1):
        continue
    else:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            sum+=num
print("Sum =",sum)