string = input("Enter a string: ")
substrings = []
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        substrings.append(string[i:j])

print("All substrings of the given string:")
for substring in substrings:
    print(substring)
