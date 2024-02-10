n1=int(input("Enter the 1st No.:"))
n2=int(input("Enter the 2nd No.:"))
m=max(n1,n2)
while not(m%n1==0 and m%n2==0):
    m=m+1
print("LCM=",m)