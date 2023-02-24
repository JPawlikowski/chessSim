
from chessSimFuncs import checkPos
from chessSimFuncs import movePiece
from chessSimFuncs import displayBoard

print("Starting chess simulation")
print("Input format is : <PieceName> <TargetX> <TargetY")
print("Enter 'Q' to exit")

board = [['WPawn1', 'WPawn2', 'WPawn3', 'WPawn4'],[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], ['BPawn1', 'BPawn2', 'BPawn3', 'BPawn4']]

print("Starting board : " + '\n')
displayBoard(board)

userInput = input('\n' + "-> ")
while userInput != 'Q':
    inputParsed = userInput.split(' ')
    currPiece = inputParsed[0]
    targetPosX = int(inputParsed[1])
    targetPosY = int(inputParsed[2])
    movePiece(board, currPiece, targetPosX, targetPosY)
    displayBoard(board)
    userInput = input('\n' + "-> ")

