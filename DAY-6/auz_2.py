s=input("Enter the String: ").lower().replace(" ","")
d={}
for i in s:
    d[i]=s.count(i)
print(f"The Dictionary is: {d}")