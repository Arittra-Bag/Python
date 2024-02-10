import random
try:
    num=random.uniform(-100,100)
    if num<0.5:
        raise ValueError("ValueError: The number generated is below '0.5'")
    else:
        print(f"The number generated is: {num:.2f}")
except ValueError as e:
    print(e)
