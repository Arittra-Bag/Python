t=tuple(int(num) for num in input("Enter the Numbers for Tuple(comma separated): ").split(","))
sum=0
for i in t:
    sum+=i
print("Mean=",sum/len(t))