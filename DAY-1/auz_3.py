#using a 3rd Var.
a=int(input("Enter 1st No.:"))
b=int(input("Enter 2nd No.:"))
temp=a
a=b
b=temp
print("After Swapping, 1st No.=",a)
print("After Swapping, 2nd No.=",b)

#without using 3rd Var.
a=int(input("Enter 1st No.:"))
b=int(input("Enter 2nd No.:"))
a,b=b,a
print("After Swapping, 1st No.=",a)
print("After Swapping, 2nd No.=",b)