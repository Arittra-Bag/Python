from functools import reduce
unique = lambda l: reduce(lambda acc, i: (acc[0] + [i], acc[1]) if i not in acc[0] and i not in acc[1] else ([x for x in acc[0] if x != i], acc[1] + [i] if i in acc[0] else acc[1]),l,([], []))[0]
l = input("Enter the Elements(seperated by comma): ").lower().split(",")
print(f"Unique Elements: {unique(l)}")
