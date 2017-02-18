import random


BOARD_SIZE = 24
HALF_BOARD = 12
CHECKERS_QTY = 15
WHITE_CHECKER = 'w'
BLACK_CHECKER = 'b'


def get_score():
    return random.randint(1, 6)


def print_score():
    print(get_score())


def create_board():
    return [" _ "] * BOARD_SIZE


def input_player_name(number):
    return input("What is the " + number + " player name?\n")


def init_board(board):
    board[BOARD_SIZE - 1] = str(CHECKERS_QTY) + WHITE_CHECKER
    board[HALF_BOARD - 1] = str(CHECKERS_QTY) + BLACK_CHECKER


def print_board(board):
    for index in range(HALF_BOARD + 1, BOARD_SIZE + 1):
        print('{0:3d}'.format(index), end='')
    print('')

    for element in board[HALF_BOARD:]:
        print('{0:3s}'.format(element), end='')
    print('\n\n\n')

    for element in board[HALF_BOARD - 1::-1]:
        print('{0:3s}'.format(element), end='')
    print('')

    for index in range(HALF_BOARD, 0, -1):
        print('{0:3d}'.format(index), end=''),


def get_first_turn():
    while True:
        player_1_score = get_score()
        player_2_score = get_score()
        if player_1_score != player_2_score:
            break
    if player_1_score > player_2_score:
        return 0
    else:
        return 1


print_score()
print_score()
board = create_board()
init_board(board)

players = [input_player_name('first'), input_player_name('second')]

print(players[get_first_turn()])
print_board(board)