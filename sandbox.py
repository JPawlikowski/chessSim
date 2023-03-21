
from chessSimFuncs import checkPos
from chessSimFuncs import movePiece
from chessSimFuncs import displayBoard
from chessSimFuncs import sanitizeInput
from chessSimFuncs import findPiecePos
from chessSimFuncs import checkMove

print("Starting chess simulation")
print("Input format is : <PieceName> <TargetX> <TargetY")
print("Enter 'Q' to exit")

board = [['WPawn1', 'WPawn2', 'WPawn3', 'WPawn4'],[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], ['BPawn1', 'BPawn2', 'BPawn3', 'BPawn4']]

print("Starting board : " + '\n')
displayBoard(board)

userInput = input('\n' + "-> ")
while userInput != 'Q':
    inputParsed, sanitizeResult = sanitizeInput(userInput)
    if sanitizeResult != 0:
        print("Re-enter : expected format is <piece> <targetPosX> <targetPosY>")
        userInput = input('\n' + "-> ")
        continue
    currPiece = inputParsed[0]
    targetPosX = int(inputParsed[2])
    targetPosY = int(inputParsed[1])

    currPiecePosX, currPiecePosY = findPiecePos(board, currPiece)
    if (currPiecePosX == -1 or currPiecePosY == -1):
        print("Entered piece : " + currPiece + " not found on the board")
        print("Re-enter : expected format is <piece> <targetPosX> <targetPosY>")
        userInput = input('\n' + "-> ")
        continue

    if currPiecePosX == targetPosX and currPiecePosY == targetPosY:
        print("Piece " + currPiece + " current (" + str(currPiecePosX) + ", " + str(currPiecePosY) + ") and target (" + str(targetPosX) + ", " + str(targetPosY) + ") positions are the same")
        print("Re-enter : expected format is <piece> <targetPosX> <targetPosY>")
        userInput = input('\n' + "-> ")
        continue

    #movePosX, movePosY = checkMove(board, currPiece)
    #print("Potential move : " + str(movePosX) + ", " + str(movePosY) )

    movePiece(board, currPiece, targetPosX, targetPosY)
    displayBoard(board)
    userInput = input('\n' + "-> ")

