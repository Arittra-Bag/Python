start,end=int(input("Enter the Start of the Range: ")),int(input("Enter the End of the Range: "))
print(f"Prime Numbers between {start} and {end}:",list(filter(lambda x:all(x%i!=0 for i in range(2,int(x**0.5)+1)) and x>1,range(start,end+1))))

#or

start,end=int(input("Enter the Start of the Range: ")),int(input("Enter the End of the Range: "))
if start<0 or end<0:
    print("Invalid Input! Range starting from 0 upto inf")
    exit()
l=[num for num in range(start,end+1) if all(num%i!=0 for i in range(2,int(num**0.5)+1)) and num>1]
print(l)