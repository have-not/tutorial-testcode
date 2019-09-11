import random

def d6(n=None):
    random.seed(n)
    return random.randint(1, 6)

def roll_2d(x, y):
    return x + y
