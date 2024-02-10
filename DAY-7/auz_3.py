def unique(l):
    ul=[]
    rl=[]
    for i in l:
        if i not in ul and i not in rl:
            ul.append(i)
        elif i in ul:
            ul.remove(i)
            rl.append(i)
    return ul
l=input("Enter the Elements(seperated by comma): ").lower().split(",")
print(f"Unique Elements: {unique(l)}")
