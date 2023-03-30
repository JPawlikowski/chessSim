
from chessSimFuncs import checkPos
from chessSimFuncs import movePiece
from chessSimFuncs import displayBoard
from chessSimFuncs import sanitizeInput
from chessSimFuncs import findPiecePos
from chessSimFuncs import checkMove
from chessSimFuncs import posTranslateStrToInt  
from chessSimFuncs import posTranslateIntToStr

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
        print("Re-enter : expected format is : <piece> <targetPosCol> <targetPosRow>")
        print("Enter 'Q' to exit")
        userInput = input('\n' + "-> ")
        continue
    currPiece = inputParsed[0]
    
    targetPosColStr = inputParsed[1]
    targetPosCol = posTranslateStrToInt(targetPosColStr)
    targetPosRow = int(inputParsed[2])
    # x = Row , Y = Col

    print("Current move : Row " + str(targetPosRow) + ", Col " + str(targetPosCol) )

    currPiecePosCol, currPiecePosRow = findPiecePos(board, currPiece)

    print("Current piece position : row " + str(currPiecePosRow) + ", Col " + str(currPiecePosCol))

    if (currPiecePosRow == -1 or currPiecePosCol == -1):
        print("Entered piece : " + currPiece + " not found on the board")
        print("Re-enter : expected format is <piece> <targetPosCol> <targetPosRow>")
        userInput = input('\n' + "-> ")
        continue

    if currPiecePosRow == targetPosRow and currPiecePosCol == targetPosCol:
        print("Piece " + currPiece + " current (" + str(currPiecePosRow) + ", " + str(currPiecePosCol) + ") and target (" + str(targetPosRow) + ", " + str(targetPosCol) + ") positions are the same")
        print("Re-enter : expected format is <piece> <targetPosCol> <targetPosRow>")
        userInput = input('\n' + "-> ")
        continue

    
    movePosRow, movePosCol = checkMove(board, currPiece)
    print("Potential move : " + str(movePosRow) + ", " + str(movePosCol) )
    
    if (targetPosRow == movePosRow) and (targetPosCol == movePosCol):
        movePiece(board, currPiece, targetPosRow, targetPosCol)
    else:
        print("Piece " + currPiece + " target (" + str(targetPosCol) + ", " + str(targetPosCol) + ") positions are not available for this piece")
        print("Re-enter : expected format is <piece> <targetPosCol> <targetPosRow>")
        userInput = input('\n' + "-> ")
        continue
    
    #movePiece(board, currPiece, targetPosRow, targetPosCol)
    displayBoard(board)
    print(board)
    userInput = input('\n' + "-> ")

