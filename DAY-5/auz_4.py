l1=list(input("Enter the Numbers for List-1(comma separated): ").split(","))
l2=list(input("Enter the Numbers for List-2(comma separated): ").split(","))
result=[num for num in l1]+[num for num in l2]
print(f"Resultant List={result}")