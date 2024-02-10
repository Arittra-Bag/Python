from functools import reduce
num=[int(x) for x in input("Enter the Numbers(seperated by comma): ").split(",")]
print("Maximum Number is: ",reduce(lambda x,y:x if x>y else y,num))
