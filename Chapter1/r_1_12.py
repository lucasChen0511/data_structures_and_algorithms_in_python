from random import randrange

def choice(list):
    x = randrange(0, len(list))
    return x

print(choice([2,3,4,5,6,7]))