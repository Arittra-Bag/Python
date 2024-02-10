n=int(input("Enter the no. of Elements: "))
d={}
for i in range(n):
    d[i]=int(input(f"Enter Element-{i+1}: "))
print(f"The Dictionary is: {d}")
l=list(d.values())
l.sort()
t=list(d.keys())
for i in range(len(t)):
    for j in range(len(l)):
        if(i==j):
            d[t[i]]=l[j]
print(f"The Sorted Dictionary is: {d}")