num=int(input("Enter the No. of Rows:"))
for i in range(num):
    for j in range(i):
        print(' ',end=' ')     
    for j in range(num-i):
        print("*",end=' ')
    for j in range(num-i-1):
        print("*",end=' ')
    print()