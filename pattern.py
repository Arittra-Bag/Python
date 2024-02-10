n=int(input("Enter the Rows: "))
c=1
for i in range(n):
    for j in range(i+1):
        if j!=i:
            print(c,end=',')
        else:
            print(c)
        c=c+1


num=int(input("Enter the Rows:"))
for i in range(num):
    for j in range(i):
        print(' ',end=' ')     
    for j in range(num-i):
        print("*",end=' ')
    for j in range(num-i-1):
        print("*",end=' ')
    print()

 
