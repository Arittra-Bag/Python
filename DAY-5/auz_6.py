l=list(input("Enter the Numbers (comma separated): ").split(","))
result=[]
for i in l:
    for j in l:
        if (int(i) * int(j))%2!=0:
            pair=(int(i),int(j))
            if pair in result:
                continue
            if (int(j),int(i)) not in result:
                result.append(pair)
print(f"Resultant List={result}")