try:
    number = float(input("Enter a number: "))
    if number >= 0:
        print("You entered a positive or zero number:", number)
    else:
        raise ValueError("You've entered a negative number.")
except ValueError as e:
    print("Error:", e)
