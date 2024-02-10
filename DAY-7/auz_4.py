start=int(input("Enter the Start of the Range: "))
end=int(input("Enter the End of the Range: "))
print(f"Numbers Divisible between {start} and {end}:",list(filter(lambda x:x%5==0 and x%7==0,range(start,end+1))))
