from rand import *

mi=int(input("Enter Minimum Number: "))
ma=int(input("Enter Maximum Number: "))
r=int(input("Enter Range of Numbers: "))
num=generate_random_number(mi,ma,r)
print("Generated random numbers:",num)
print(f"Mean: {calculate_mean(num):.2f}")
print(f"Median: {calculate_median(num):.2f}")
print(f"Standard Deviation: {calculate_std_deviation(num):.2f}")
