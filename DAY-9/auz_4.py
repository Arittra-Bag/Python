import random
try:
    for i in range(1, 11):
        print(random.randint(1, 100))
    raise StopIteration
except StopIteration:
    print("StopIteration exception raised. Exiting the program.")
