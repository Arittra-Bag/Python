num=[int(x) for x in input("Enter the Numbers(seperated by comma): ").split(",")]
print("Even Numbers:",list(filter(lambda x:x%2==0,num)))
