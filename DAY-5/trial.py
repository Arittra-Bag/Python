t=tuple(int(num) for num in input("Enter the Numbers for Tuple(comma separated): ").split(","))
l=list(t)
d={}
for i in range(len(l)):
    d[str(l[i])]=l.count(l[i])
print(d)