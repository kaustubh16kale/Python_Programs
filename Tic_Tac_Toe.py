import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def auto_play(board):
    empty=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                empty.append((i,j))
    return random.choice(empty)

def win(board):
    if (board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X") or (board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X") or (board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X"):
        print("you won the game") 
    if (board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X") or (board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X") or (board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X"):
        print("you won the game")
    if (board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X") or (board[2][0]=="X" and board[1][1]=="X" and board[0][2]=="X"):
        print("You won the game")

    if (board[0][0]=="O"  and board[0][1]=="O"  and board[0][2]=="O" )or (board[1][0]=="O"  and board[1][1]=="O"  and board[1][2]=="O" ) or (board[2][0]=="O"  and board[2][1]=="O"  and board[2][2]=="O" ):
        print("comp won the game") 
    if (board[0][0]=="O"  and board[1][0]=="O"  and board[2][0]=="O" ) or (board[0][1]=="O"  and board[1][1]=="O"  and board[2][1]=="O" ) or (board[0][2]=="O"  and board[1][2]=="O"  and board[2][2]=="O" ):
        print("comp won the game")
    if (board[0][0]=="O"  and board[1][1]=="O"  and board[2][2]=="O" ) or (board[2][0]=="O"  and board[1][1]=="O"  and board[0][2]=="O" ):
        print("comp won the game")
    else:
        pass
    
def play_tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    print("You are 'X' computer is 'O'")
    print_board(board)
    while True:
        row_input=int(input("Enter the row:"))
        col_input=int(input("Enter the col no: "))

        if board[row_input][col_input]==" ":
            board[row_input][col_input]="X"
            print_board(board)
        else:
            print("cell is occupied")
            continue
        flag=win(board)
        if flag==True:
            break

        auto_row, auto_col = auto_play(board)
        board[auto_row][auto_col] = "O"
        print_board(board)
        flag=win(board)
        if flag==True:
            break

def main():
    play_tic_tac_toe()


if __name__=="__main__":
    main()