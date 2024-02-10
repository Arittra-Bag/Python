import random
def gen_random(min_val,max_val,r):
    return [random.randint(min_val,max_val) for i in range(r)]