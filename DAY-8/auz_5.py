from shuffle import *

mi=int(input("Enter Minimum Number: "))
ma=int(input("Enter Maximum Number: "))
r=int(input("Enter Range of Numbers: "))
num=generate_random_number(mi,ma,r)
print("Original List of random numbers:",num)
print("Shuffled List of random numbers:",shuffle_list_elements(num))
