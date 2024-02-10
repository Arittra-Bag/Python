def gcd(a,b):
    while b:
        a,b = b,a % b
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)

num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {result}")  