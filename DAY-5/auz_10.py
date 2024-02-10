t=tuple(int(num) for num in input("Enter the Numbers for Tuple(comma separated): ").split(","))
un=[]
dp=[]
for i in t:
    if i not in un:
        un.append(i)
    else:
        dp.append(i)
for i in dp:
    if i in un:
        un.remove(i)
print("Unique Values=",tuple(un),"\nDuplicate Values=",tuple(dp))