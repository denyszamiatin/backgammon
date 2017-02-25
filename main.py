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


def roll_dices():

    dice_results = [get_score() for _ in range(2)]

    if dice_results[0] == dice_results[1]:
        dice_results *= 2

    return dice_results


def get_checkers_position(board, color):
    return [index for index, cell in enumerate(board) if cell[COLOR] == color]


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

def change_player():
    global current_player
    if current_player == players[0]:
        current_player =  players[1]
        return current_player
    else:
        current_player =  players[0]
        return current_player

def check_move_possibility(dices, color):
    print("dice_res: ", dices)
    possible_positions = []
    for dice in dices:
        for pos in get_checkers_position(board, color):
            if color == BLACK:
                new_pos = move_black(pos, dice)
                possible_positions.append(new_pos)
            else:
                new_pos = move_white(pos, dice)
                possible_positions.append(new_pos)
            if board[new_pos][COLOR] != inverse_color(color):
                print("Checker can be moved to position",
                      new_pos)
            else:
                print("Checker can't be moved to position ",
                      new_pos,
                      "because here is enemy's checker")
    return possible_positions


board = create_board()
init_board(board)
print_board(board)

# print('checkers_pos: ', get_checkers_position(board, BLACK))
# print('checkers_pos: ', get_checkers_position(board, WHITE))

players = []
players.append(input_player_name('first'))
players.append(input_second_player_name(players[0]))

current_player = players[get_first_turn()]

print(current_player, " goes first")
#
# change_player()

# print("Now ",current_player, " goes")

dice_res = roll_dices()

def enter_the_number_of_field(current_player):
    possible_numbers = [i for i in range(1, BOARD_SIZE + 1)]
    number_of_field = 0
    if current_player == players[0]:
        check_move_possibility(dice_res, WHITE)
        while True:
            try:
                number_of_field = int(input('please, enter the number of the field from which '
                                            'you will start the turn (1-24): '))
                if number_of_field not in possible_numbers:
                    raise ValueError
                else:
                    for cell in board:
                        if cell[0] == number_of_field and cell[2] == BLACK:
                            print("you can't move the checker there")
                            break
                    else:
                        return number_of_field
            except ValueError:
                print('ValueError, try again...')
                continue
    else:
        check_move_possibility(dice_res, BLACK)
        while True:
            try:
                number_of_field = int(input('please, enter the number of the field from which '
                                            'you will start the turn (1-24): '))
                if number_of_field not in possible_numbers:
                    raise ValueError
                else:
                    for cell in board:
                        if cell[0] == number_of_field and cell[2] == WHITE:
                            print("you can't move the checker there")
                            break
                    else:
                        return number_of_field
            except ValueError:
                print('ValueError, try again...')
                continue


def enter_the_number_of_dice(dices):
    dices = dice_res
    number_of_dice = 0
    while True:
        try:
            number_of_dice = int(input('please, enter the number to which you want '
                                       'to move the check (1,6): '))
            if number_of_dice not in dices:
                raise ValueError
            else:
                return number_of_dice
        except ValueError:
            print('ValueError, try again...')
            continue


field_and_number = []
field_and_number = [enter_the_number_of_field(current_player), enter_the_number_of_dice(dice_res)]
print(field_and_number)


def check_checkers_in_house(board, color):
    sum_ = 0
    for cell in board:
        if cell[2] == color:
            for index, argument_of_cell in enumerate(cell):
                if index == 1:
                    sum_ += argument_of_cell
    if sum_ ==  CHECKERS_QTY:
        # print('all checkers are in house')
        return True
    else:
        # print('all checkers are not in house, the game continues')
        return False


WHITE_CHECKERS_HOUSE = board[18:]
BLACK_CHECKERS_HOUSE = board[6:12]
check_checkers_in_house(WHITE_CHECKERS_HOUSE, BLACK)
check_checkers_in_house(BLACK_CHECKERS_HOUSE, WHITE)
