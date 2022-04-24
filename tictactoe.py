board = ["-","-","-"
         "-","-","-"
         "-","-","-"]
currentPlayer = "x"
winner = None
gameRunning = True

#printing the game board
def printBoard(board):
    print(board[0] + "|" +board[1] + "|" + board[2])
    print("--------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("--------")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("--------")
    printBoard(board)

#take the player input
def playerInput(board):
    inp = int(input("Enter a number 1-9:"))
    if inp >= 1 and inp>= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already in that spot")

#check for a win or tie

#switch the player

#check for a win a tie again

while gameRunning:
    printBoard(board)
    playerInput(board)
