def find_primes(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers

if __name__ == '__main__':
    start = int(input("Enter the Starting Number: "))
    end = int(input("Enter the Ending Number: "))
    print(f"Prime Numbers between {start} and {end} are:", find_primes(start, end))