n1=int(input("Enter no. of terms for Dict-1: "))
d1={}
for i in range(1,n1+1):
    s=input(f"Enter Key-{i} for Dict-1: ").lower()
    d1[s]=int(input(f"Enter Element-{i} for Dict-1: "))
n2=int(input("Enter no. of terms for Dict-2: "))
d2={}
for i in range(1,n2+1):
    s=input(f"Enter Key-{i} for Dict-2: ").lower()
    d2[s]=int(input(f"Enter Element-{i} for Dict-2: "))
print(f"The Dictionary-1 is: {d1}")
print(f"The Dictionary-2 is: {d2}")
print("The Merged Dictionary is: ",{**d1,**d2})