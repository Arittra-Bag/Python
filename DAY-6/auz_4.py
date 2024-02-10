n=int(input("Enter No. of Players: "))
cricket={}
name=[]
runs=[]
for i in range(n):
    name.append(input(f"Enter Name-{i+1}: ").lower().capitalize())
    runs.append(int(input("Enter Runs: ")))
    cricket[name[i]]=runs[i]
cf=cricket.keys()
print(f"Name of the Players is: {cf}")
nm=input("Enter Name: ").lower().capitalize()
if nm in cf:
    print(f"{nm} has scored {cricket[nm]} Runs!")
else:
    print(-1)