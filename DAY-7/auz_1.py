def gcd(n1,n2):
    while n2:
        n1,n2=n2,n1%n2
    return n1

def lcm(n1,n2):
    return (n1*n2)//gcd(n1,n2)

n1=int(input("Enter the 1st No.: "))
n2=int(input("Enter the 2nd No.: "))
r_gcd=gcd(n1,n2)
r_lcm=lcm(n1,n2)
print(f"GCD of {n1} and {n2} is: {r_gcd}")
print(f"LCM of {n1} and {n2} is: {r_lcm}")
