
def movePiece(board, piece, targetPosRow, targetPosCol):
    #add a section to check targetPosition is viable and not same
    currPiecePosRow, currPiecePosCol = findPiecePos(board, piece)

    updatePos(board, piece, targetPosRow, targetPosCol)

#Given board and piece find current piece position
def findPiecePos(board, piece):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j].lower() == piece.lower():
                print("Found " + piece + " at : row " + str(i) + ", Col " + str(j))
                return i, j
    print("Piece " + str(piece) + " not found")
    return -1, -1

#Set specified piece to target location and current location to empty
#target position not sanitized
#Return the updated board
def updatePos(board, piece, targetPosRow, targetPosCol):
    currPiecePosRow, currPiecePosCol = findPiecePos(board, piece)
    board[targetPosRow][targetPosCol] = piece
    board[currPiecePosRow][currPiecePosCol] = ' '
    return board

#take input as raw string
#Expected format: <piece> <targetPosX> <targetPosY>
#This requires more validations for format/length/content of each inputted field
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
def checkPos(board, targetPosRow, targetPosCol):
    currentPosPiece = board[targetPosRow][targetPosCol]
    print("Position : " + str(targetPosRow) + ", " + str(targetPosCol) + " contains - " + str(currentPosPiece))
    return currentPosPiece

#Determine potential allowed moves for a given piece
#Note for a white pawn this is +1 however for a black pawn its -1
def checkMove(board, piece):
    #Need to define available moves for all piece types including borders
    if ('pawn' in piece.lower()):
        if (piece[0] == 'W'):
            currPosRow, currPosCol = findPiecePos(board, piece)
            availPosCol = currPosCol
            availPosRow = currPosRow + 1
            return availPosRow, availPosCol
        else:
            currPosRow, currPosCol = findPiecePos(board, piece)
            availPosCol = currPosCol
            availPosRow = currPosRow - 1
            return availPosRow, availPosCol
    else:
        print("current piece is not a pawn")
        return -1, -1

def posTranslateStrToInt(targetPosColStr):
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'G']
    for i in range(0, len(columns)):
        if (columns[i] == targetPosColStr):
            return i
    print("entry for column not found in available options : " + str(columns))
    return -1

#Is this required? 
#Might be able to hold the Int and Str in local vars in the main runner..
def posTranslateIntToStr(targetPosColInt):
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'G']
    return columns[targetPosColInt]

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
