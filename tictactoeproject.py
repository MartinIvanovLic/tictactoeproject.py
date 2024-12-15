def print_as_grid(table):
    for i in table:
        print(" ".join(i))

def main():
    board_n_value = int(input("input n: "))

    symbol_2 = input("Player 1, input X or O: ")
    if symbol_2 == "X":
        symbol_1 = "O"
        print("Player 2 is O. ")

    else:
        symbol_2 = "X"
        print("Player 2 is X. ")


    board = create_board(board_n_value)
    print_as_grid(board)


    turn_count = 1
    tie_req_turn_count = 0
    p1_victory_counter = 0
    p2_victory_counter = 0
    game_over = False


    while not game_over:
        result = make_a_move(symbol_1, symbol_2, turn_count, board, board_n_value)
        if result == 0:
            turn_count += 1
            if board_n_value < 4:
                p1_victory_counter, p2_victory_counter = victory_pos(symbol_1, symbol_2, board, board_n_value)
            else:
                p1_victory_counter, p2_victory_counter = victory_pos_x4(symbol_1, symbol_2, board, board_n_value)

            if p1_victory_counter > 0:
                print(symbol_1, "is victorious")
                game_over = True

            elif p2_victory_counter > 0:
                print(symbol_2, "is victorious")
                game_over = True

            elif if_tie(tie_req_turn_count, board_n_value, p1_victory_counter, p2_victory_counter):
                print("Tie")
                game_over = True

            print_as_grid(board)

            tie_req_turn_count += 1


def create_board(board_n_value):
    sub_board = ["."] * board_n_value
    board = []

    for i in range(board_n_value):
        board.append(sub_board.copy())
  
    return board


def make_a_move(symbol_1, symbol_2, turn_count, board, board_n_value):
    result = 0
    if turn_count % 2 == 0:
        player = symbol_1

    else:
        player = symbol_2

    row = int(input("input row: "))-1
    column = int(input("input column: "))-1

    if (row > board_n_value-1 or row < 0) or (column > board_n_value-1 or column < 0):
        print("out of board")
        result = 1
    elif (board[row][column] == symbol_1) or (board[row][column] == symbol_2):
        print("illegal move")
        result = 2
    else:
        if player == symbol_1:
            board[row][column] = symbol_1
        else:
            board[row][column] = symbol_2

    return result

def if_tie(tie_req_turn_count, board_n_value, p1_victory_counter, p2_victory_counter):
    is_tie = False
    if tie_req_turn_count >= board_n_value*board_n_value and p1_victory_counter == 0 and p2_victory_counter == 0:
        is_tie = True
    
    return is_tie


def victory_pos(symbol_1, symbol_2, board, board_n_value):
    p1_victory_counter = 0
    p2_victory_counter = 0

    for row in range(1, board_n_value-1):
        for column in range(1, board_n_value-1):

            if board[row][column] == symbol_1 and board[row-1][column-1] == symbol_1 and board[row+1][column+1] == symbol_1:
                p1_victory_counter = 1

            elif board[row][column] == symbol_1 and board[row+1][column-1] == symbol_1 and board[row-1][column+1] == symbol_1:
                p1_victory_counter = 1

            elif board[row][column] == symbol_1 and board[row][column-1] == symbol_1 and board[row][column+1] == symbol_1:
                p1_victory_counter = 1

            elif board[row][column] == symbol_1 and board[row-1][column] == symbol_1 and board[row+1][column] == symbol_1:
                p1_victory_counter = 1


            elif board[row][column] == symbol_2 and board[row-1][column-1] == symbol_2 and board[row+1][column+1] == symbol_2:
                p2_victory_counter = 1

            elif board[row][column] == symbol_2 and board[row+1][column-1] == symbol_2 and board[row-1][column+1] == symbol_2:
                p2_victory_counter = 1

            elif board[row][column] == symbol_2 and board[row][column-1] == symbol_2 and board[row][column+1] == symbol_2:
                p2_victory_counter = 1

            elif board[row][column] == symbol_2 and board[row-1][column] == symbol_2 and board[row+1][column] == symbol_2:
                p2_victory_counter = 1

    for row in range(1, board_n_value-1):
        for column in [0, board_n_value-1]:
            if board[row][column] == symbol_1 and board[row-1][column] == symbol_1 and board[row+1][column] == symbol_1:
                p1_victory_counter = 1

            elif board[row][column] == symbol_2 and board[row-1][column] == symbol_2 and board[row+1][column] == symbol_2:
                p2_victory_counter = 1
                
    for column in range(1, board_n_value-1):
        for row in [0, board_n_value-1]:
            if board[row][column] == symbol_1 and board[row][column-1] == symbol_1 and board[row][column+1] == symbol_1:
                p1_victory_counter = 1

            elif board[row][column] == symbol_2 and board[row][column-1] == symbol_2 and board[row][column+1] == symbol_2:
                p2_victory_counter = 1
    
    return p1_victory_counter, p2_victory_counter


def victory_pos_x4(symbol_1, symbol_2, board, board_n_value):
    p1_victory_counter = 0
    p2_victory_counter = 0

    for row in range(2, board_n_value-2):
        for column in range(2, board_n_value-2):

            if board[row][column] == symbol_1 and board[row-1][column-1] == symbol_1 and board[row+1][column+1] == symbol_1 and (board[row-2][column-2] == symbol_1 or board[row+2][column+2] == symbol_1):
                p1_victory_counter = 1
                print("case1")

            elif board[row][column] == symbol_1 and board[row+1][column-1] == symbol_1 and board[row-1][column+1] == symbol_1 and (board[row+2][column-2] == symbol_1 or board[row-2][column+2] == symbol_1):
                p1_victory_counter = 1
                print("case2")

            elif board[row][column] == symbol_1 and board[row][column-1] == symbol_1 and board[row][column+1] == symbol_1 and (board[row][column-2] == symbol_1 or board[row][column+2] == symbol_1):
                p1_victory_counter = 1
                print("case3")

            elif board[row][column] == symbol_1 and board[row-1][column] == symbol_1 and board[row+1][column] == symbol_1 and (board[row-2][column] == symbol_1 or board[row+2][column] == symbol_1):
                p1_victory_counter = 1
                print("case4")


            elif board[row][column] == symbol_2 and board[row-1][column-1] == symbol_2 and board[row+1][column+1] == symbol_2 and (board[row-2][column-2] == symbol_2 or board[row+2][column+2] == symbol_2):
                p2_victory_counter = 1
                print("case1.1")

            elif board[row][column] == symbol_2 and board[row+1][column-1] == symbol_2 and board[row-1][column+1] == symbol_2 and (board[row+2][column-2] == symbol_2 or board[row-2][column+2] == symbol_2):
                p2_victory_counter = 1
                print("case2.1")

            elif board[row][column] == symbol_2 and board[row][column-1] == symbol_2 and board[row][column+1] == symbol_2 and (board[row][column-2] == symbol_2 or board[row][column+2] == symbol_2):
                p2_victory_counter = 1
                print("case3.1")

            elif board[row][column] == symbol_2 and board[row-1][column] == symbol_2 and board[row+1][column] == symbol_2 and (board[row-2][column] == symbol_2 or board[row+2][column] == symbol_2):
                p2_victory_counter = 1
                print("case4.1")

    for row in range(2, board_n_value-2):
        for column in [0, board_n_value-2]:
            if board[row][column] == symbol_1 and board[row-1][column] == symbol_1 and board[row+1][column] == symbol_1 and (board[row-2][column] == symbol_1 or board[row+2][column] == symbol_1):
                p1_victory_counter = 1
                print("case1.2")

            elif board[row][column] == symbol_2 and board[row-1][column] == symbol_2 and board[row+1][column] == symbol_2 and (board[row-2][column] == symbol_2 or board[row+2][column] == symbol_2):
                p2_victory_counter = 1
                print("case2.2")
                
    for column in range(2, board_n_value-2):
        for row in [0, board_n_value-2]:
            if board[row][column] == symbol_1 and board[row][column-1] == symbol_1 and board[row][column+1] == symbol_1 and (board[row][column-2] == symbol_1 or board[row][column+2] == symbol_1):
                p1_victory_counter = 1
                print("case1.3")

            elif board[row][column] == symbol_2 and board[row][column-1] == symbol_2 and board[row][column+1] == symbol_2 and (board[row][column-2] == symbol_2 or board[row][column+2] == symbol_2):
                p2_victory_counter = 1
                print("case2.3")
    
    return p1_victory_counter, p2_victory_counter
        


main()
