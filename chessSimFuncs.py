
def movePiece(board, piece, targetPosX, targetPosY):
    #add a section to check targetPosition is viable and not same
    currPiecePosX, currPiecePosY = findPiecePos(board, piece)

    updatePos(board, piece, targetPosX, targetPosY)

#Given board and piece find current piece position
def findPiecePos(board, piece):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j].lower() == piece.lower():
                print("Found " + piece + " at " + str(i) + ", " + str(j))
                return i, j
    print("Piece " + str(piece) + " not found")
    return -1, -1

#Set specified piece to target location and current location to empty
#target position not sanitized
#Return the updated board
def updatePos(board, piece, targetPosX, targetPosY):
    currPiecePosX, currPiecePosY = findPiecePos(board, piece)
    board[targetPosX][targetPosY] = piece
    board[currPiecePosX][currPiecePosY] = ' '
    return board

#take input as raw string
#Expected format: <piece> <targetPosX> <targetPosY>
def sanitizeInput(input):
    try:
        inputParsed = input.split(' ')
        if len(inputParsed) == 3:
            return inputParsed, 0
        else:
            return [], 1
    except:
        print("issue with parse split by space on user input")
        return [], 2


#Print piece in given position and return piece as string
def checkPos(board, targetPosX, targetPosY):
    currentPosPiece = board[targetPosX][targetPosY]
    print("Position : " + str(targetPosX) + ", " + str(targetPosY) + " contains - " + str(currentPosPiece))
    return currentPosPiece

#Determine potential allowed moves for a given piece
def checkMove(board, piece):
    #Need to define available moves for all piece types including borders
    if piece.lower.contains('pawn'):
        currPosX, currPosY = findPiecePos(board, piece)
        availPosX = currPosX
        availPosY = currPosY + 1
        return availPosX, availPosY
    else:
        print("current piece is not a pawn")

#User input should be in format 'A1'
def posTranslate():
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'G']


#Display board in visual manner, note reversed sequence as 0,0 is bottom left
def displayBoard(board):
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'G']
    for i in range(len(board)-1, -1, -1):
        print('  ', end='')
        for h in range(0, len(board[0])*4 + 2):  #note this lenth might depend on size of board, testing with like a 5/5
            print(' - ', end='')
        print('\n')

        for j in range(0, len(board[i])):
            if (j == 0):
                print(str(i), end='')
            print(' | ', end='')
            print(board[i][j].center(10, ' '), end='')
            if (j == len(board[i])-1):
                print(' | ', end='')
        
        if (i == 0):
            print('\n')
            print('  ', end='')
            for h in range(0, len(board[0])*4 + 2):  #note this lenth might depend on size of board, testing with like a 5/5
                print(' - ', end='')
            print('\n')
            
            for g in range(0, len(board[0])):  #note this lenth might depend on size of board, testing with like a 5/5
                if (g == 0):
                    print('   ', end='')
                print(columns[g].center(10, ' '), end='')

                print('   ', end='')
        #if (dashCount / 2 == 0):
        ##        print(' ' + columns[colNum] + ' ', end='')
        #        colNum = colNum + 1
        #        continue
        print('\n')
