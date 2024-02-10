import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + "@#$%&"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def is_valid(password):
    return any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in "@#$%&" for c in password)

if __name__ == "__main__":
    while True:
        length = int(input("Enter the desired password length: "))
        while True:
            password = generate_password(length)
            if is_valid(password):
                break
        print("Generated Password:", password)
        another = input("Generate another password? (y/n): ").lower()
        if another != "y":
            break
