l1=list(input("Enter the Numbers for List-1(comma separated): ").split(","))
l2=list(input("Enter the Numbers for List-2(comma separated): ").split(","))
result=[]
for i in l2:
    if i not in l1:
        result.append(i)
print(f"Resultant List={result}")