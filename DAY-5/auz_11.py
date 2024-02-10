#1st Code Format
t=tuple(int(num) for num in input("Enter the Numbers for Tuple(comma separated): ").split(","))
l=[]
c=()
for i in range(len(t)):
    l.append(0)
    if t[i] in c:
        continue
    else:
        c=c+t[i:i+1]
        for j in range(len(t)):
            if t[i]==t[j]:
                l[i]+=1
    print(f"Frequency of '{t[i]}' = {l[i]}")

# OR
#2nd Code Format
t=tuple(int(num) for num in input("Enter the Numbers for Tuple(comma separated): ").split(","))
l=[]
c=()
for i in range(len(t)):
    l.append(0)
    for j in range(len(t)):
        if t[i]==t[j]:
            l[i]+=1
    if t[i] in c:
        continue
    else:
        c=c+t[i:i+1]
        print(f"Frequency of '{t[i]}' = {l[i]}")