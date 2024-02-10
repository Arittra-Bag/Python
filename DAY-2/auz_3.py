n=int(input("Enter the No. of Rows:"))
c=1
for i in range(n):
    for j in range(i):
        print(c,end=',')
        c=c+1
    print(c,"\n")
    c+=1