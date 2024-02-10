t=tuple(int(num) for num in input("Enter the Numbers for Tuple(comma separated): ").split(","))
result=[]
for i in t:
    for j in t:
        if (int(i) * int(j))%2==0:
            pair=(int(i),int(j))
            if pair in result:
                continue
            if (int(j),int(i)) not in result:
                result.append(pair)
print(f"Resultant Tuple={tuple(result)}")