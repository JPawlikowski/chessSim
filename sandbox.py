
from chessSimFuncs import checkPos
from chessSimFuncs import movePiece
from chessSimFuncs import displayBoard
from chessSimFuncs import sanitizeInput
from chessSimFuncs import findPiecePos
from chessSimFuncs import checkMoves
from chessSimFuncs import posTranslateStrToInt  


print("Starting chess simulation")
print("THERE IS AN ISSUE WITH FLIPPED COLUMN AND ROW SOMEWHERE")
print("UPDATE 05/05/2024 - I think this is FIXED, updated findPosPiece, swtiched I and J")
print("Input format is : <PieceName> <TargetX> <TargetY")
print("Enter 'Q' to exit")

#board = [['WPawn1', 'WPawn2', 'WPawn3', 'WPawn4', 'WPawn5', 'WPawn6'],[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ',' ', ' '], [' ', ' ', ' ', ' ',' ', ' '], ['BPawn1', 'BPawn2', 'BPawn3', 'BPawn4', 'BPawn5', 'BPawn6']]

#board = [['WRook1', 'WRook2', 'WRook3', 'WRook4'], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], ['BRook1', 'BRook2', 'BRook3', 'BRook4']]

board = [['WRook1', 'WKnight1', 'WBishop1', 'WQueen1', 'WKing1', 'WBishop2', 'WKnight2', 'WRook2'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['BRook1', 'BKnight1', 'BBishop1', 'BQueen1', 'BKing2', 'BBishop2', 'BKnight2', 'BRook2']]

# board = [['WRook1', 'WKnight1', 'WBishop1', 'WQueen1', 'WKing1', 'WBishop2', 'WKnight2', 'WRook2'],
#         ['WPawn1', 'WPawn2', 'WPawn3', 'WPawn4', 'WPawn5', 'WPawn6', 'WPawn7', 'WPawn8'],
#         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#         ['BPawn1', 'BPawn2', 'BPawn3', 'BPawn4', 'BPawn5', 'BPawn6', 'BPawn7', 'BPawn8'],
#         ['BRook1', 'BKnight1', 'BBishop1', 'BQueen1', 'BKing2', 'BBishop2', 'BKnight2', 'BRook2']]


currentMoveWhite = True

print("Starting board : " + '\n')
displayBoard(board)

print("White to move")

userInput = input('\n' + "-> ")
while userInput != 'Q':
    inputParsed, sanitizeResult = sanitizeInput(userInput)
    if sanitizeResult != 0:
        print("Re-enter : expected format is : <piece> <targetPosCol> <targetPosRow>")
        print("Enter 'Q' to exit")
        userInput = input('\n' + "-> ")
        continue
    currPiece = inputParsed[0]

    if (currentMoveWhite == True):
        if currPiece[0] == 'W':
            pass
        elif (currPiece[0] == 'B'):
            print("Current move is for WHITE")
            print("Re-enter : expected format is : <piece> <targetPosCol> <targetPosRow>")
            print("Enter 'Q' to exit")
            userInput = input('\n' + "-> ")
            continue
        else:
            print("Invalid color - first character of piece name defines the color")
            print("Re-enter : expected format is : <piece> <targetPosCol> <targetPosRow>")
            print("Enter 'Q' to exit")
            userInput = input('\n' + "-> ")
            continue
    else:
        if (currPiece[0] == 'B'):
            pass
        elif (currPiece[0] == 'W'):
            print("Current move is for BLACK")
            print("Re-enter : expected format is : <piece> <targetPosCol> <targetPosRow>")
            print("Enter 'Q' to exit")
            userInput = input('\n' + "-> ")
            continue
        else:
            print("Invalid color - first character of piece name defines the color")
            print("Re-enter : expected format is : <piece> <targetPosCol> <targetPosRow>")
            print("Enter 'Q' to exit")
            userInput = input('\n' + "-> ")
            continue
    
    targetPosColStr = inputParsed[1]
    targetPosCol = posTranslateStrToInt(targetPosColStr)
    targetPosRow = int(inputParsed[2])
    # x = Row , Y = Col

    print("Current move : Col " + str(targetPosCol) + ", Row " + str(targetPosRow) )

    currPiecePosRow, currPiecePosCol = findPiecePos(board, currPiece)

    print("Current piece position : Col " + str(currPiecePosCol) + ", Row " + str(currPiecePosRow))

    if (currPiecePosRow == -1 or currPiecePosCol == -1):
        print("Entered piece : " + currPiece + " not found on the board")
        print("Re-enter : expected format is <piece> <targetPosCol> <targetPosRow>")
        userInput = input('\n' + "-> ")
        continue

    if currPiecePosRow == targetPosRow and currPiecePosCol == targetPosCol:
        print("Piece " + currPiece + " current (" + str(currPiecePosCol) + ", " + str(currPiecePosRow) + ") and target (" + str(targetPosCol) + ", " + str(targetPosRow) + ") positions are the same")
        print("Re-enter : expected format is <piece> <targetPosCol> <targetPosRow>")
        userInput = input('\n' + "-> ")
        continue

    #movePosRow, movePosCol = checkMoves(board, currPiece)
    availMoves = checkMoves(board, currPiece)
    print("Potential moves : ")
    print(availMoves)

    moved = False
    for i in range(0, len(availMoves)):
            if (availMoves[i][0] == targetPosRow) and (availMoves[i][1] == targetPosCol):
                movedStatus = movePiece(board, currPiece, targetPosRow, targetPosCol)
                if (movedStatus == 0):
                    moved = True
                else:
                    moved = False
    
    if moved == False:
        print("current move is not an available move for " + str(currPiece))
        userInput = input('\n' + "-> ")
        continue
    """
    if (targetPosRow == movePosRow) and (targetPosCol == movePosCol):
        movePiece(board, currPiece, targetPosRow, targetPosCol)
    else:
        print("Piece " + currPiece + " target (" + str(targetPosCol) + ", " + str(targetPosCol) + ") positions are not available for this piece")
        print("Re-enter : expected format is <piece> <targetPosCol> <targetPosRow>")
        userInput = input('\n' + "-> ")
        continue
    """
    
    #movePiece(board, currPiece, targetPosRow, targetPosCol)
    displayBoard(board)
    print(board)
    if (currentMoveWhite == True):
        currentMoveWhite = False
        print("Black to move")
        userInput = input('\n' + "-> ")
        continue
    else:
        currentMoveWhite = True
        print("White to move")
    userInput = input('\n' + "-> ")