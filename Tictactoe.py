'''Tictactoe game without GUI'''
'''Concept : functions, error handling'''

def show_board(board):
    for row in board:
        for col in row:
            print(col, end=' ')
        print()


def update_board(x, y, board, sym):
    board[x][y] = "[" + str(sym) + "]"
    return board


def check_win(board, sym):
    if board[0][0] == f"[{sym}]" and board[0][1] == f"[{sym}]" and board[0][2] == f"[{sym}]": # First Row
        return True
    if board[1][0] == f"[{sym}]" and board[1][1] == f"[{sym}]" and board[1][2] == f"[{sym}]": # Second Row
        return True
    if board[2][0] == f"[{sym}]" and board[2][1] == f"[{sym}]" and board[2][2] == f"[{sym}]": # Third Row
        return True
    if board[0][0] == f"[{sym}]" and board[1][0] == f"[{sym}]" and board[2][0] == f"[{sym}]": # Column One
        return True
    if board[0][1] == f"[{sym}]" and board[1][1] == f"[{sym}]" and board[2][1] == f"[{sym}]": # Column Two
        return True
    if board[0][2] == f"[{sym}]" and board[1][2] == f"[{sym}]" and board[2][2] == f"[{sym}]": # Column Three
        return True
    if board[0][0] == f"[{sym}]" and board[1][1] == f"[{sym}]" and board[2][2] == f"[{sym}]": # Diagnol 1
        return True
    if board[0][2] == f"[{sym}]" and board[1][1] == f"[{sym}]" and board[2][0] == f"[{sym}]": # Diagnol 2
        return True
    return False
    
    
def is_full(board):
    for i in board:
        for j in i:
            if j == "[ ]":
                return False
    return True


def turn_changer(turn):
    if turn == 0:
        return 1
    else:
        return 0


def tictactoe():
    print("")
    print("------Welcome to TICTACTOE------")
    board = [["[ ]"] * 3, ["[ ]"] * 3, ["[ ]"] * 3]
    show_board(board)
    print("Please give coordinates in format : x y\n where x and y are values between 0 and 2")
    symbols = ['X', 'O']
    moves = []
    turn = 0 # Gives turn of each player. Initially of 'X'

    while is_full(board) != True:
        sym = symbols[turn]
        print(f"Give Coordinates for {sym} :", end=" ")
        try:
            x, y = list(map(int, input().split()))
        except:
            print("Wrong Input")
            continue
        
        if x < 0 or x > 2 or y < 0 or y > 2: # Checks for Invalid Moves
            print("Invalid Move")
        else:
            if [x, y] in moves: # Checks if position is already taken
                print("Position Already Taken")
            else:
                board = update_board(x, y, board, sym)
                if check_win(board, sym) == True:
                    show_board(board)
                    print("horaay!!!!!")
                    print(sym, "Wins")
                    break
                moves.append([x, y])
                turn = turn_changer(turn)
        show_board(board)
    print("Draw")
    print("Do you want to play again? Type 'y' for 'yes'")
    reply = input()
    if reply == 'y' or reply == 'Y':
        tictactoe()
    else:
        print("Thank you for playing")
        

if __name__=='__main__':
    tictactoe()
