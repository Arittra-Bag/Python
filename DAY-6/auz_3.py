n=int(input("Enter no. of Inputs: "))
d={}
name=[]
salary=[]
for i in range(n):
    name.append(input(f"Enter Name-{i+1}: "))
    salary.append(int(input("Enter Salary: ")))
    d[name[i]]=salary[i]
print(f"The Dictionary is: {d}")