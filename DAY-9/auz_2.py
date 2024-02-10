try:
    num1 = float(input("Enter the 1st Number: "))
    num2 = float(input("Enter the 2nd Number: "))
    sum_r = num1 + num2
    diff_r = num1 - num2
    pro_r = num1 * num2
    if num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    div_r = num1 / num2
    print(f"Addition result: {sum_r}")
    print(f"Subtraction result: {diff_r}")
    print(f"Multiplication result: {pro_r}")
    print(f"Division result: {div_r}")
except ValueError as e:
    print(f"ValueError: {e}. Please enter valid numeric input.")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting...")
