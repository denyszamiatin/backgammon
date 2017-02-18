import random

def score():
    return random.randint(1, 6)

def print_score():
    print(score())

def list_w():
    for i in range (1,13):
        list_w = [['w'+str(i)]]
        print(list_w)

def list_b():
    for i in range(13,25):
        list_b = [['b'+str(i)]]
        print(list_b)


def board():
    return list_w(), list_b()

print_score()
print_score()
board()
