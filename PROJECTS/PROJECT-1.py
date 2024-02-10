def find_nth_term(n):
    if n==0:
        return("Invalid Term!")
    elif n % 2 == 0:
        return (f"The term is: {3 ** (n // 2 - 1)}")
    else:
        return (f"The term is: {2 ** (n // 2)}")
print(find_nth_term(int(input("Enter the no. of terms: "))))
