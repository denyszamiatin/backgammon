import random

def score():
    return random.randint(1, 6)

def print_score():
    print(score())

print_score()
print_score()

# Lets ask players for their name first, so then we refer to them by their name instead of "Player"
player_1 = input("What is the first player name?\n")
player_2 = input("What is the second player name?\n")

# Then, lets determine who is going first

def first_turn():
    while True:
        player_1_score = score() + score()
        player_2_score = score() + score()
        print(player_1, "has:", player_1_score)
        print(player_2, "has:", player_2_score)
        if player_1_score == player_2_score:
            print("OK, lets make another roll")
        elif player_1_score > player_2_score:
            print(player_1,"- go first!")
            return
        else:
            print(player_2,"- go first!")
            return

first_turn()