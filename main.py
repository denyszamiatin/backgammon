import random


BOARD_SIZE = 24
HALF_BOARD = 12
CHECKERS_QTY = 15
WHITE_CHECKER = 'w'
BLACK_CHECKER = 'b'
global white_on_board
global black_on_board

def get_score():
    return random.randint(1, 6)


def print_score():
    print(get_score())


def input_player_name(number):
    return input("What is the " + number + " player name?\n")


def check_players():
    while True:
        if players[1] == players[0]:
            print('name already exist')
            players[1] = input_player_name('second')
        else:
            print(players[get_first_turn()])
            break
"""
def create_board():
    return [" _ "] * BOARD_SIZE


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
    print('\n')
"""

def create_alt_board():

    alt_board = [[i+1," "," "]for i in range(BOARD_SIZE)]
    alt_board = alt_board[::-1]
    return alt_board



def init_alt_board(alt_board):

    alt_board[0][1] = CHECKERS_QTY
    alt_board[0][2] = WHITE_CHECKER
    alt_board[12][1] = CHECKERS_QTY
    alt_board[12][2] = BLACK_CHECKER

def print_alt_board(alt_board):

    """
    Visualize the board
    """

    for i in range(HALF_BOARD, BOARD_SIZE):
        print('{0:4d}'.format(alt_board[::-1][i][0]), end=" ")

    print('\n')
    print(" ", end= " ")

    for i in range(HALF_BOARD, BOARD_SIZE):
        if alt_board[::-1][i][1] != " ":
            print('{0:4s}'.format(str(alt_board[::-1][i][1]) + alt_board[::-1][i][2]), end=" ")
        else:
            print('{0:4s}'.format('_'), end=' ')


    print("\n\n\n")
    print(" ", end= " ")

    for i in range(HALF_BOARD, BOARD_SIZE):
        if alt_board[i][1] != " ":
            print('{0:4s}'.format(str(alt_board[i][1]) + alt_board[i][2]), end=" ")
        else:
            print('{0:4s}'.format('_'), end=' ')

    print('\n')

    for i in range(HALF_BOARD, BOARD_SIZE):
        print('{0:4d}'.format(alt_board[i][0]), end=" ")
    print('\n')


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


#print_score()
#print_score()
#board = create_board()
#init_board(board)

alt_board = create_alt_board()
init_alt_board(alt_board)
print_alt_board(alt_board)

players = [input_player_name('first'), input_player_name('second')]
check_players()

#print_board(board)


def get_dice_result():

    dice_results = []
    roll = 0
    NUMBER_OF_ROLLS = 2

    while roll < NUMBER_OF_ROLLS:
        dice_results.append(get_score())
        roll += 1

    if dice_results[0] == dice_results[1]:
        dice_results = dice_results * 2

    return dice_results

print("First turn", players[get_first_turn()])
#print(get_dice_result())

def get_checkers_position():
    global white_on_board
    global black_on_board
    black_on_board = []
    white_on_board = []
    while True:
        for index,qty,color in alt_board:
            if color == 'b':
                black_on_board.append(index)
            elif color == 'w':
                white_on_board.append(index)

        return black_on_board,white_on_board

#print(get_checkers_position())

def check_move_possibility_white():
    move_is_possible = 0
    get_checkers_position()
    dice_result = get_dice_result()
    qty_of_steps = len(dice_result)
    while qty_of_steps>0:
        for i in dice_result:
            for j in white_on_board:
                for b in black_on_board:
                    if j-i != b:
                        print("White checker can be moved to position", j-i)
                        qty_of_steps=-1
                        move_is_possible = 1
                    else:
                        print("White checker can't be moved to position ",b, "because here is black checker")
    if move_is_possible == 1:
        return 0

def check_move_possibility_black():
    move_is_possible = 0
    get_checkers_position()
    dice_result = get_dice_result()
    qty_of_steps = len(dice_result)
    while qty_of_steps>0:
        for i in dice_result:
            for j in black_on_board:
                for w in white_on_board:
                    if j-i != w:
                        print("Black checker can be moved to position", j-i)
                        qty_of_steps=-1
                        move_is_possible = 1
                    else:
                        print("Black checker can't be moved to position ",w, "because here is white checker")
    if move_is_possible == 1:
        return 0

print(check_move_possibility_white())
print(check_move_possibility_black())