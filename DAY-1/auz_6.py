n=int(input("Enter the Number:"))
for i in range(len(str(n)),0,-1):
    n=n%(10**i)
    if(i==1):
        print(n)
    else:
        print(n,end=', ')