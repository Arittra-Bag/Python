import random

def generate_random_number(min_value, max_value,r):
    return [random.randint(min_value,max_value) for _ in range(r)]

def shuffle_list_elements(input_list):
    random.shuffle(input_list)
    return input_list
