start,end=int(input("Enter the Start of the Range: ")),int(input("Enter the End of the Range: "))
print(f"Prime Numbers between {start} and {end}:",list(filter(lambda x:all(x%i!=0 for i in range(2,int(x**0.5)+1)) and x>1,range(start,end+1))))
