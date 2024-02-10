string = input("Enter a string: ")
string = string.replace(" ", "").lower()
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
