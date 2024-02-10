try:
    age=int(input("Enter your age: "))
    if age<0:
        raise ValueError("ValueError: Age cannot be negative.")
    else:
        print(f"Your age is {age}.")
except ValueError as e:
    print(e)