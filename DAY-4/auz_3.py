s=input("Enter a string: ")
l=list(s)
p=l.pop()
for i in range(len(l)):
    if l[i]==p.upper() or l[i]==p.lower():
        l[i]="*"
l.append(p)
print(''.join(l))