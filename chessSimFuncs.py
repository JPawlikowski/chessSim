
def movePiece(board, piece, targetPosX, targetPosY):
    #add a section to check targetPosition is viable and not same
    currPiecePosX, currPiecePosY = findPiecePos(board, piece)

    updatePos(board, piece, targetPosX, targetPosY)

def findPiecePos(board, piece):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j].lower() == piece.lower():
                print("Found " + piece + " at " + str(i) + " - " + str(j))
                return i, j
    print("Piece " + str(piece) + " not found")
    return 0, 0

#Set specified piece to target location and current location to empty
def updatePos(board, piece, targetPosX, targetPosY):
    currPiecePosX, currPiecePosY = findPiecePos(board, piece)
    board[targetPosX][targetPosY] = piece
    board[currPiecePosX][currPiecePosY] = ' '
    return board

def checkPos(board, targetPosX, targetPosY):
    currentPosPiece = board[targetPosX][targetPosY]
    print("Position : " + str(targetPosX) + ", " + str(targetPosY) + " contains - " + str(currentPosPiece))

def checkMove(board, piece):
    #Need to define available moves for all piece types including borders
    if piece.lower.contains('pawn'):
        currPosX, currPosY = findPiecePos(board, piece)
        availPosX = currPosX
        availPosY = currPosY + 1
        return availPosX, availPosY
    else:
        print("current piece is not a pawn")

def displayBoard(board):
    for i in range(len(board)-1, -1, -1):
        for j in range(0, len(board[i])):
            print(' | ', end='')
            print(board[i][j].center(10, ' '), end='')
            if (j == len(board[i])-1):
                print(' | ', end='')
        print('\n')
        for h in range(0, 18):
            print(' - ', end='')
        print('\n')
