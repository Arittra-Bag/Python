import math
import random

def generate_random_number(min_value, max_value,r):
    return [random.randint(min_value,max_value) for _ in range(r)]

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        median = (middle1 + middle2) / 2
    else:
        median = sorted_numbers[n // 2]
    return median

def calculate_std_deviation(numbers):
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_deviation = math.sqrt(variance)
    return std_deviation