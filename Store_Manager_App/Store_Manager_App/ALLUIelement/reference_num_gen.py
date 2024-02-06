import random

def generate(n):
    start_point = 10**(n-1)
    end_point = (10**n)-1
    return random.randint(start_point,end_point)




