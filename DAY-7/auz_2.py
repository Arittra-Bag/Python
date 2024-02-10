def count(s):
    uc=0
    lc=0
    for char in s:
        if char.isupper():
            uc+=1
        elif char.islower():
            lc+=1
    return uc,lc
s=input("Enter a String: ").replace(" ","")
uc,lc=count(s)
print(f"Count of Uppercase Letters: {uc}")
print(f"Count of Lowercase Letters: {lc}")
