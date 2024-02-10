def convert(base_from, base_to, num):
    try:
        if base_from == 10 and base_to == 2:
            result = bin(int(num))[2:]
        elif base_from == 2 and base_to == 10:
            result = str(int(num, 2))
        elif base_from == 10 and base_to == 8:
            result = oct(int(num))[2:]
        elif base_from == 8 and base_to == 10:
            result = str(int(num, 8))
        elif base_from == 10 and base_to == 16:
            result = hex(int(num))[2:]
        elif base_from == 16 and base_to == 10:
            result = str(int(num, 16))
        else:
            result = "Invalid conversion"
        return result
    except ValueError:
        return "Invalid input"

while True:
    base_choices = {
        1: (10, 2),
        2: (2, 10),
        3: (10, 8),
        4: (8, 10),
        5: (10, 16),
        6: (16, 10)
    }
    print("\nNumber Base Converter\n1. Decimal to Binary\n2. Binary to Decimal\n3. Decimal to Octal\n4. Octal to Decimal\n5. Decimal to Hexadecimal\n6. Hexadecimal to Decimal\n7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 7:
        print("Exiting...")
        break
    if choice not in range(1, 7):
        print("Invalid choice!")
    num = input(f"Enter the number in base {base_choices[choice][0]}: ")
    base_from, base_to = base_choices[choice]
    result = convert(base_from, base_to, num)
    print(f"Converted number: {result}")