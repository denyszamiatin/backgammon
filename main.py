import random


BOARD_SIZE = 24
HALF_BOARD = 12
BOARD_START = 0
CHECKERS_QTY = 15
WHITE = 'w'
BLACK = 'b'
CELL_NUMBER = 0
QTY = 1
COLOR = 2


def get_score():
    return random.randint(1, 6)


def print_score():
    print(get_score())


def input_player_name(number):
    return input("What is the " + number + " player name?\n")


def input_second_player_name(player1_name):
    while True:
        player2_name = input_player_name('second')
        if player1_name != player2_name:
            return player2_name


def create_board():
    return [[i, 0, " "] for i in range(BOARD_SIZE, 0, -1)]


def init_board(board):
    board[BOARD_START][QTY] = CHECKERS_QTY
    board[BOARD_START][COLOR] = WHITE
    board[HALF_BOARD][QTY] = CHECKERS_QTY
    board[HALF_BOARD][COLOR] = BLACK


def print_half_board(board):
    for cell in board[HALF_BOARD:BOARD_SIZE]:
        if cell[QTY] != 0:
            print(
                '{0:4s}'.format(str(cell[QTY]) + cell[COLOR]),
                end=" "
            )
        else:
            print('{0:4s}'.format('_'), end=' ')


def print_board_numbers(board):
    for cell in board[HALF_BOARD:BOARD_SIZE]:
        print('{0:4d}'.format(cell[CELL_NUMBER]), end=" ")


def print_board(board):
    """
    Visualize board
    """
    print_board_numbers(board[::-1])
    print('\n')
    print("  ", end="")
    print_half_board(board[::-1])
    print("\n\n\n")

    print("  ", end="")
    print_half_board(board)
    print('\n')
    print_board_numbers(board)
    print('\n')


def get_first_turn():
    while True:
        player_1_score = get_score()
        player_2_score = get_score()
        if player_1_score > player_2_score:
            return 0
        elif player_1_score < player_2_score:
            return 1


board = create_board()
init_board(board)
print_board(board)

players = []
players.append(input_player_name('first'))
players.append(input_second_player_name(players[0]))


def roll_dices():

    dice_results = [get_score() for _ in range(2)]

    if dice_results[0] == dice_results[1]:
        dice_results *= 2

    return dice_results

dice_res = roll_dices()


def get_checkers_position(board, color):
    return [index for index, cell in enumerate(board) if cell[COLOR] == color]


print('checkers_pos: ', get_checkers_position(board, BLACK))
print('checkers_pos: ', get_checkers_position(board, WHITE))


def move_white(pos, dice):
    return pos - dice


def move_black(pos, dice):
    new_pos = pos - dice
    if new_pos <= 0:
        new_pos += BOARD_SIZE
    return new_pos


def inverse_color(color):
    if color == BLACK:
        return WHITE
    else:
        return BLACK


def check_move_possibility(dices, color):
    print("dice_res: ", dices)
    for dice in dices:
        for pos in get_checkers_position(board, color):
            if color == BLACK:
                new_pos = move_black(pos, dice)
            else:
                new_pos = move_white(pos, dice)
            if board[new_pos][COLOR] != inverse_color(color):
                print("Checker can be moved to position",
                      new_pos)
            else:
                print("Checker can't be moved to position ",
                      new_pos,
                      "because here is enemy's checker")


def check_possible_turn():
    """
    function determines who goes first,
    then asks to enter the cell number from which will start the turn, and how much,
    then check for the possibility of the implementation, if the turn is possible the function returns
    a list that consists of a cell number and the number of dice
    :return:
    """
    possible_numbers = [i for i in range(1, BOARD_SIZE + 1)]
    res_list = []
    print(board)
    first_turn = players[get_first_turn()]
    print('first turn: ', first_turn)
    number_of_field = None
    number_of_dice = None

    if first_turn == players[0]:
        print('Player', players[0] + ' throws the dice...')
        check_move_possibility(dice_res)

        while True:
            try:
                number_of_field = int(input('please, enter the number of the field from which '
                                                'you will start the turn (1-24): '))
                number_of_dice = int(input('please, enter the number to which you want '
                                                       'to move the check (1,6): '))
                if number_of_field not in possible_numbers or number_of_dice not in dice_res:
                    raise ValueError
                else:
                    for cell in alt_board:
                        if cell[0] == number_of_field and cell[2] == 'b':
                            print("you can't move the checker there")
                            break
                    else:
                        res_list.append(number_of_field)
                        res_list.append(number_of_dice)
                        break
            except ValueError:
                print('ValueError, try again...')
                continue

    else:
        print('Player', players[1] + ' throws the dice...')
        check_move_possibility_black(dice_res)

        while True:
            try:
                number_of_field = int(input('please, enter the number of the field from which '
                                                'you will start the turn (1-24): '))
                number_of_dice = int(input('please, enter the number to which you want '
                                                       'to move the check (1,6): '))
                if number_of_field not in possible_numbers or number_of_dice not in dice_res:
                    raise ValueError
                else:
                    for cell in alt_board:
                        if cell[0] == number_of_field and cell[2] == 'w':
                            print("you can't move the checker there")
                            break
                    else:
                        res_list.append(number_of_field)
                        res_list.append(number_of_dice)
                        break
            except ValueError:
                print('ValueError, try again...')
                continue

    return res_list


possible_move = check_possible_turn()
print(possible_move)
