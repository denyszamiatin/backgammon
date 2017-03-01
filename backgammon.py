import random


BOARD_SIZE = 24
HALF_BOARD = 12
QUARTER_BOARD = 6
CHECKERS_QTY = 15
NOT_A_SCORE = -1
WHITE_CHECKER = 'w'
BLACK_CHECKER = 'b'
NOTHING = "  -  "

num_white_out_of_the_board = 0
num_black_out_of_the_board = 0


def get_score():
    return random.randint(1, 6)


def create_board():
    return [NOTHING] * BOARD_SIZE


def input_player_name(number):
    return input("What is the " + number + " player name?\n")


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


def get_num_white(a):
    try:
        num = int(a[0::-1])
        if a[-1] == WHITE_CHECKER:
            return num
    except ValueError:
        pass
    return 0


def get_num_black(a):
    try:
        num = int (a[0::-1])
        if(a[-1] == BLACK_CHECKER):
            return num
        else:
            return 0
    except:
        return 0

def assert_incorrect_board_state():
    num_white = num_white_out_of_the_board
    num_black = num_black_out_of_the_board
    for i in range(0, BOARD_SIZE, 1):
        num_white += get_num_white(board[i])
        num_black += get_num_black(board[i])
    print ("num_white = ", num_white, ", num_black = ", num_black)
    assert (num_white == num_black == CHECKERS_QTY)


def get_num_white_at_home():
    num = num_white_out_of_the_board
    for i in range(QUARTER_BOARD):
        num += get_num_white(board[i])
    return num


def can_move_white(score):
    all_white_at_home = get_num_white_at_home() == CHECKERS_QTY
    for index in range(BOARD_SIZE):
        if get_num_white(board[index]) and \
                index - score >= 0 and \
                (get_num_black(board[index - score]) == 0):
            return True
        if all_white_at_home and index - score < 0:
            return True
    return False


def invert_board_point (board_point):
    if board_point < HALF_BOARD:
        return HALF_BOARD + board_point
    else:
        return board_point - HALF_BOARD

def can_move_from(move_from, score1, score2):
    # check only for white checkers
    if score1 != NOT_A_SCORE:
        move_to = move_from - score1
        if move_to >= 0 and get_num_black(board[move_to]) == 0:
            return True
    if score2 != NOT_A_SCORE:
        move_to = move_from - score2
        if move_to >= 0 and get_num_black(board[move_to]) == 0:
            return True
    if get_num_white_at_home () == CHECKERS_QTY:
        if score1 != NOT_A_SCORE:
            move_to = move_from - score1
            if move_to < 0:
                return True
        if score2 != NOT_A_SCORE:
            move_to = move_from - score2
            if move_to < 0:
                return True
    return False


def get_point():
    while True:
        try:
            return int(input("Move from field = ")) - 1
        except ValueError:
            print("FROM :: Please input a number!")


def check_score(score_was_used, score):
    return NOT_A_SCORE if score_was_used else score


def move_white(score1, score2, board_is_inverted):
    # If board_is_inverted then we move black checkers
    print("scores:", score1, " ", score2)
    global board
    global num_white_out_of_the_board

    score1_was_used = False
    score2_was_used = False
    while ((not score1_was_used) and can_move_white(score1)) or ((not score2_was_used) and can_move_white(score2)):
        move_from = get_point()

        if board_is_inverted:
            move_from = invert_board_point(move_from)

        if not can_move_from(
                move_from,
                check_score(score1_was_used, score1),
                check_score(score2_was_used, score2)
        ):
            print("You can not move from that point. Input point again.")
            continue

        if 0 <= move_from < BOARD_SIZE and get_num_white(board[move_from]) > 0:
            while True:
                if get_num_white_at_home() == CHECKERS_QTY:
                    print("Input 0 to move checker out")
                move_to = int(input("Move to field = "))
                try:
                    move_to = int(move_to)
                except:
                    print("TO :: Please input a number!")
                    continue

                if move_to == 0:
                    if score1_was_used:
                        if move_from - score2 > 0:
                            print ("Not enough score to move checker out")
                            continue
                        else:
                            score2_was_used = True
                    elif score2_was_used:
                        if move_from - score1 > 0:
                            print("Not enough score to move checker out")
                            continue
                        else:
                            score1_was_used = True
                    else:
                        if move_from - score1 < 0:
                            score1_was_used = True
                        elif move_from - score2 < 0:
                            score2_was_used = True
                        else:
                            print("Not enough score to move checker out")
                            continue

                    num_white_out_of_the_board += 1
                    num_white = get_num_white(board[move_from])
                    if num_white == 1:
                        board[move_from] = NOTHING
                    else:
                        board[move_from] = str(num_white - 1) + WHITE_CHECKER
                    print_board(board, board_is_inverted)
                    print ("One checker was removed from the board")
                    if num_white_out_of_the_board == CHECKERS_QTY:
                        return
                    break

                move_to -= 1
                if board_is_inverted:
                    move_to = invert_board_point(move_to)

                if not 0 <= move_to < BOARD_SIZE:
                    print("Destination is out of the board")
                    continue
                elif move_from - move_to != score1 and move_from - move_to != score2:
                    print("You can move only on your score")
                    continue

                if (score1 != score2):
                    if move_from - move_to == score1 and score1_was_used == True:
                        print(str(score1) + " was used")
                        continue
                    elif move_from - move_to == score2 and score2_was_used == True:
                        print(str(score2) + " was used")
                        continue

                if get_num_black(board[move_to]) != 0:
                    print("You can not move your checker on enemy checker")
                    continue
                num_white = get_num_white(board[move_to])
                board[move_to] = str(num_white + 1) + WHITE_CHECKER
                num_white = get_num_white(board[move_from])
                if num_white == 1:
                    board[move_from] = NOTHING
                else:
                    board[move_from] = str(num_white - 1) + WHITE_CHECKER

                if (not score1_was_used) and move_from - move_to == score1:
                    score1_was_used = True
                else:
                    score2_was_used = True
                assert_incorrect_board_state()
                print ("After Move")
                print_board(board, board_is_inverted)
                break # break while for "move_to"
        else:
            print ("There is not your checkers in field ", (invert_board_point(move_from) if board_is_inverted else move_from)  + 1)
            continue
    else:
        if (not score1_was_used) and (not score2_was_used):
            print("Can not move. Next player turn.")
        else:
            print("Turn was succesfully finished")


def move_black(score1, score2):
    global board
    board = invert_board()
    move_white(score1, score2, True)
    board = invert_board()


def init_board(board):
    board[BOARD_SIZE - 1] = str(CHECKERS_QTY) + WHITE_CHECKER
    board[HALF_BOARD - 1] = str(CHECKERS_QTY) + BLACK_CHECKER


def init_board2(board):
    board[23] = str(3) + WHITE_CHECKER
    board[22] = str(3) + WHITE_CHECKER
    board[21] = str(3) + WHITE_CHECKER
    board[0] = str(3) + WHITE_CHECKER
    board[5] = str(3) + WHITE_CHECKER
    board[2] = str(3) + BLACK_CHECKER
    board[10] = str(2) + BLACK_CHECKER
    board[12] = str(5) + BLACK_CHECKER
    board[17] = str(5) + BLACK_CHECKER
    assert_incorrect_board_state()

def init_board3(board):
    board[23] = str(3) + WHITE_CHECKER
    board[22] = str(3) + WHITE_CHECKER
    board[21] = str(1) + WHITE_CHECKER
    board[20] = str(1) + WHITE_CHECKER
    board[19] = str(1) + WHITE_CHECKER
    board[0] = str(3) + WHITE_CHECKER
    board[5] = str(3) + WHITE_CHECKER
    board[12] = str(1) + BLACK_CHECKER
    global num_black_out_of_the_board
    num_black_out_of_the_board = 14
    global num_white_out_of_the_board
    num_white_out_of_the_board = 0
    assert_incorrect_board_state()

def print_board(board, board_is_inverted):
    if (board_is_inverted):
        board = invert_board()
    for index in range(HALF_BOARD + 1, BOARD_SIZE + 1):
        print(str(index).center(5), end='')
    print('')
    for element in board[HALF_BOARD:]:
        print(str(element).center(5), end='')
    #print('\n\n\n')
    print('\n')
    for element in board[HALF_BOARD - 1::-1]:
        print(str(element).center(5), end='')
    print('')
    for index in range(HALF_BOARD, 0, -1):
        print(str(index).center(5), end=''),
    print('\n')


def invert_board ():
    global board
    temp_board = create_board()
    for i in range(0, HALF_BOARD, 1):
        temp_board[i] = board[HALF_BOARD + i]
        temp_board[HALF_BOARD + i] = board[i]
        if temp_board[i][-1] == WHITE_CHECKER:
            temp_board[i] = str(get_num_white(temp_board[i])) + BLACK_CHECKER
        elif temp_board[i][-1] == BLACK_CHECKER:
            temp_board[i] = str(get_num_black(temp_board[i])) + WHITE_CHECKER
        if temp_board[HALF_BOARD + i][-1] == WHITE_CHECKER:
            temp_board[HALF_BOARD + i] = str(get_num_white(temp_board[HALF_BOARD + i])) + BLACK_CHECKER
        elif temp_board[HALF_BOARD + i][-1] == BLACK_CHECKER:
            temp_board[HALF_BOARD + i] = str(get_num_black(temp_board[HALF_BOARD + i])) + WHITE_CHECKER
    global num_black_out_of_the_board
    global num_white_out_of_the_board
    temp = num_black_out_of_the_board
    num_black_out_of_the_board = num_white_out_of_the_board
    num_white_out_of_the_board = temp

    return temp_board


def main():
    global board
    #players = [input_player_name('first'), input_player_name('second')]
    while True:
        print("WHITE TURN: ")
        print_board(board, False)
        move_white(get_score(), get_score(), False)
        if num_white_out_of_the_board == CHECKERS_QTY:
            break
        print("BLACK TURN: ")
        print_board(board, False)
        move_black (get_score(), get_score())
        if num_black_out_of_the_board == CHECKERS_QTY:
            break
    if num_white_out_of_the_board == CHECKERS_QTY:
        print("WHITE WIN")
    elif num_black_out_of_the_board == CHECKERS_QTY:
        print("BLACK WIN")

# Main activities
board = create_board()
init_board2(board)
num_white_out_of_the_board = 0
num_black_out_of_the_board = 0
main()

