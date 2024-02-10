try:
    num = float(input("Enter a number: "))
    sq = num * num
    print(f"The square of {num} is {sq}")
except KeyboardInterrupt:
    print("\nCtrl + C was pressed. Program terminated.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
