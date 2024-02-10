def fact(n):
    if n<0:
        print("Not Defined!")
        exit(1)
    if n == 0:
        return 1
    else:
        return n * fact(n-1)