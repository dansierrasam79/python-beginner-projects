# The function accepts one parameter containing the board's current status
# and prints it out to the console.
def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+str(board[0][0])+"   |   "+str(board[0][1])+"   |   "+str(board[0][2])+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+str(board[1][0])+"   |   "+str(board[1][1])+"   |   "+str(board[1][2])+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+str(board[2][0])+"   |   "+str(board[2][1])+"   |   "+str(board[2][2])+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
# The function accepts the board's current status, asks the user about their move,
# checks the input, and updates the board according to the user's decision.
    user_move = int(input("Your turn, human. Select a number representing a free square: "))
    if user_move > 0 and user_move < 10 and user_move not in board_positions_filled:
        board_positions_filled.append(user_move)
        for key,value in board_positions.items():
            if user_move == key:
                row = board_positions[key][0]
                col = board_positions[key][1]
                board[row][col] = "O"
                break;
        display_board(board)
        return victory_for(board, "O")
    else:
        print("Incorrect entry!")
        enter_move(board)

def victory_for(board, sign):
# The function analyzes the board's status in order to check if
# the player using 'O's or 'X's has won the game
    for i in range(0, len(board)):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return sign
        elif board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return sign
        elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            return sign

def draw_move(board):
# The function draws the computer's move and updates the board.
    print("Come on Computer. Your Turn Now!")
    computer_move = randrange(1,9)
    if computer_move not in board_positions_filled:
        board_positions_filled.append(computer_move)
        for key,value in board_positions.items():
            if computer_move == key:
                row = board_positions[key][0]
                col = board_positions[key][1]
                board[row][col] = "X"
                break;
        display_board(board)
        return victory_for(board, "X")
    else:
        print("Dumbass Computer! Try again!")
        draw_move(board)

if __name__ == "__main__":
    from random import randrange
    board = [[1,2,3],[4,"X",6],[7,8,9]]
    board_positions = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]} 
    board_positions_filled = [5]
    whowins = ""
    print("This is your board. Computer gets first turn as marked by the letter X")
    display_board(board)
    while True:
        if enter_move(board) == "O" and len(board_positions_filled) < 9:
            whowins = "Human"
            print("Game over!", whowins, "wins!")
            break;
        elif draw_move(board) == "X" and len(board_positions_filled) < 9:
            whowins = "Computer"
            print("Game over!", whowins, "wins!")
            break;
        elif len(board_positions_filled) == 9 and victory_for(board, "X") != "X" and victory_for(board, "O") != "O":
            print("Game over! No winner!")
            break;
