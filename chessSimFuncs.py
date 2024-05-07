#Added return for status, 0 for success (moved) and -1 for not moved due to same color target and source pieces
def movePiece(board, piece, targetPosRow, targetPosCol):
    #add a section to check targetPosition is viable and not same
    currPiecePosRow, currPiecePosCol = findPiecePos(board, piece)

    if (piece[0] == 'W'):
        targetPosPiece = checkPos(board, targetPosRow, targetPosCol)
        if (targetPosPiece[0] == 'W'):
            return -1
        else:
            updatePos(board, piece, targetPosRow, targetPosCol)
            return 0
    
    if (piece[0] == 'B'):
        targetPosPiece = checkPos(board, targetPosRow, targetPosCol)
        if (targetPosPiece[0] == 'B'):
            return -1
        else:
            updatePos(board, piece, targetPosRow, targetPosCol)
            return 0

#Given board and piece find current piece position
def findPiecePos(board, piece):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j].lower() == piece.lower():
                print("Found " + piece + " at : Col " + str(j) + ", Row " + str(i))
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
#May 8th: Bishop and Rook can jump over other pieces
def checkMoves(board, piece):
    availMoves = []
    #Need to define available moves for all piece types including borders
    if ('pawn' in piece.lower()):
        print("Finding available moves for pawn")
        if (piece[0] == 'W'):
            currPosRow, currPosCol = findPiecePos(board, piece)
            availPosCol = currPosCol
            availPosRow = currPosRow + 1
            availMoves.append([availPosRow, availPosCol])
            checkPawnTakeLeft = checkPos(board, availPosRow, availPosCol-1)
            if  (checkPawnTakeLeft[0] == 'B'):
                availMoves.append([availPosRow, availPosCol-1])
            checkPawnTakeRight = checkPos(board, availPosRow, availPosCol+1)
            if  (checkPawnTakeRight[0] == 'B'):
                availMoves.append([availPosRow, availPosCol+1])
            #return availMoves
        else:
            currPosRow, currPosCol = findPiecePos(board, piece)
            availPosCol = currPosCol
            availPosRow = currPosRow - 1
            availMoves.append([availPosRow, availPosCol])
            checkPawnTakeLeft = checkPos(board, availPosRow, availPosCol-1)
            if  (checkPawnTakeLeft[0] == 'W'):
                availMoves.append([availPosRow, availPosCol-1])
            checkPawnTakeRight = checkPos(board, availPosRow, availPosCol+1)
            if  (checkPawnTakeRight[0] == 'W'):
                availMoves.append([availPosRow, availPosCol+1])
            #return availMoves
        
    #Rook and bishop will need separate logic for takes
    if ('bishop' in piece.lower() or 'queen' in piece.lower()):
        print("Finding available moves for bishop or queen")
    
        currPosRow, currPosCol = findPiecePos(board, piece)
        #All diagonals going right and up
        posPiece = ' '
        moveIncr = 1

        print("Length of board[0] " + str(len(board[0])))
        #this used to be str(len(board[0][0]) but it somehow returned 6? Get back to check correct width and height of board (05/05/2024)
        print("Length of board[0][0] " + str(len(board[0])))
        
        print("ALL DIAG RIGHT AND UP")
        while posPiece == ' ':
            print("next row check " + str(currPosRow+moveIncr))
            if (currPosRow+moveIncr >= len(board[0])):
                break
            print("next column check " + str(currPosCol+moveIncr))
            if (currPosCol+moveIncr >= len(board[0])):
                break
            else: 
                posPiece = checkPos(board, currPosRow+moveIncr, currPosCol+moveIncr)
                availMoves.append([currPosRow+moveIncr, currPosCol+moveIncr])
                moveIncr = moveIncr + 1
            continue

        #All diagonals going left and up
        print("ALL DIAG LEFT AND UP")
        posPiece = ' '
        moveIncr = 1
        while posPiece == ' ':
            print("next row: " + str(currPosRow+moveIncr))
            if (currPosRow+moveIncr >= len(board[0])):
                break
            print("Next col: " + str(currPosCol-moveIncr))
            if (currPosCol-moveIncr < 0):
                break
            else: 
                posPiece = checkPos(board, currPosRow+moveIncr, currPosCol-moveIncr)
                availMoves.append([currPosRow+moveIncr, currPosCol-moveIncr])
                moveIncr = moveIncr + 1
            continue

        #All diagonals going left and down
        print("ALL DIAG LEFT AND DOWN")
        posPiece = ' '
        moveIncr = 1
        while posPiece == ' ':
            print("next row: " + str(currPosRow+moveIncr))
            if (currPosRow-moveIncr < 0):
                break
            print("next col: " + str(currPosCol-moveIncr))
            if (currPosCol-moveIncr < 0):
                break
            else: 
                posPiece = checkPos(board, currPosRow-moveIncr, currPosCol-moveIncr)
                availMoves.append([currPosRow-moveIncr, currPosCol-moveIncr])
                moveIncr = moveIncr + 1
            continue

        #All diagonals going right and down
        print("ALL DIAG RIGHT AND DOWN")
        posPiece = ' '
        moveIncr = 1
        while posPiece == ' ':
            print("next row: " + str(currPosRow-moveIncr))
            if (currPosRow-moveIncr < 0):
                break
            print("next col: " + str(currPosCol+moveIncr))
            if (currPosCol+moveIncr >= len(board[0])):
                break
            else: 
                posPiece = checkPos(board, currPosRow-moveIncr, currPosCol+moveIncr)
                availMoves.append([currPosRow-moveIncr, currPosCol+moveIncr])
                moveIncr = moveIncr + 1
            continue
       #return availMoves
    
    #Consider checking if target position contains piece of same color then its not available
    #TODO: UPDATE checking if target position contains same color is already done as part of MOVE function, can remove it from here
    if ('knight' in piece.lower()):
        print("Finding available moves for knight")
        #Consider 8 possible moves of a knight, clockwise starting from the top
        currPosRow, currPosCol = findPiecePos(board, piece)
        print("Current piece color : " + piece[0])

        #TOP RIGHT
        topRightRow = currPosRow + 2
        topRightCol = currPosCol + 1
        if (topRightRow < len(board[0])):
            if (topRightCol < len(board[0])):
                posPiece = checkPos(board, topRightRow, topRightCol)
                if posPiece == ' ':
                    print("Top right target position is empty")
                    availMoves.append([topRightRow, topRightCol])
                elif (posPiece[0] != piece[0]):
                    #Current piece color DIFFERENT than color of piece in position
                    print("Top right move contains piece of different color, move appended")
                    availMoves.append([topRightRow, topRightCol])
                else:
                    print("Current piece and top right position are same color")
            else:
                print("Top right position is off board by column")
        else:
            print("Top right position is off board by row")

        #UPPER RIGHT
        upperRightRow = currPosRow + 1
        upperRightCol = currPosCol + 2
        if (upperRightRow < len(board[0])):
            if (upperRightCol < len(board[0])):
                posPiece = checkPos(board, upperRightRow, upperRightCol)
                if posPiece == ' ':
                    print("Upper right target position is empty")
                    availMoves.append([upperRightRow, upperRightCol])
                elif (posPiece[0] != piece[0]):
                    #Current piece color DIFFERENT than color of piece in position
                    print("Upper right move contains piece of different color, move appended")
                    availMoves.append([upperRightRow, upperRightCol])
                else:
                    print("Current piece and upper right position are same color")
            else:
                print("Upper right position is off board by column")
        else:
            print("Upper right position is off board by row")

        #LOWER RIGHT
        lowerRightRow = currPosRow - 1
        lowerRightCol = currPosCol + 2
        if (lowerRightRow < len(board[0])):
            if (lowerRightCol < len(board[0])):
                posPiece = checkPos(board, lowerRightRow, lowerRightCol)
                if posPiece == ' ':
                    print("Lower right target position is empty")
                    availMoves.append([lowerRightRow, lowerRightCol])
                elif (posPiece[0] != piece[0]):
                    #Current piece color DIFFERENT than color of piece in position
                    print("Lower right move contains piece of different color, move appended")
                    availMoves.append([lowerRightRow, lowerRightCol])
                else:
                    print("Current piece and lower right position are same color")
            else:
                print("Lower right position is off board by column")
        else:
            print("Lower right position is off board by row")

        #BOTTOM RIGHT
        bottomRightRow = currPosRow - 2
        bottomRightCol = currPosCol + 1
        if (bottomRightRow < len(board[0])):
            if (bottomRightCol < len(board[0])):
                posPiece = checkPos(board, bottomRightRow, bottomRightCol)
                if posPiece == ' ':
                    print("Bottom right target position is empty")
                    availMoves.append([bottomRightRow, bottomRightCol])
                elif (posPiece[0] != piece[0]):
                    #Current piece color DIFFERENT than color of piece in position
                    print("Bottom right move contains piece of different color, move appended")
                    availMoves.append([bottomRightRow, bottomRightCol])
                else:
                    print("Current piece and bottom right position are same color")
            else:
                print("Bottom right position is off board by column")
        else:
            print("Bottom right position is off board by row")

        #BOTTOM LEFT
        bottomLeftRow = currPosRow - 2
        bottomLeftCol = currPosCol - 1
        if (bottomLeftRow < len(board[0])):
            if (bottomLeftCol < len(board[0])):
                posPiece = checkPos(board, bottomLeftRow, bottomLeftCol)
                if posPiece == ' ':
                    print("Bottom left target position is empty")
                    availMoves.append([bottomLeftRow, bottomLeftCol])
                elif (posPiece[0] != piece[0]):
                    #Current piece color DIFFERENT than color of piece in position
                    print("Bottom left move contains piece of different color, move appended")
                    availMoves.append([bottomLeftRow, bottomLeftCol])
                else:
                    print("Current piece and bottom left position are same color")
            else:
                print("Bottom left position is off board by column")
        else:
            print("Bottom left position is off board by row")

        #LOWER LEFT
        lowerLeftRow = currPosRow - 1
        lowerLeftCol = currPosCol - 2
        if (lowerLeftRow < len(board[0])):
            if (lowerLeftCol < len(board[0])):
                posPiece = checkPos(board, lowerLeftRow, lowerLeftCol)
                if posPiece == ' ':
                    print("Lower left target position is empty")
                    availMoves.append([lowerLeftRow, lowerLeftCol])
                elif (posPiece[0] != piece[0]):
                    #Current piece color DIFFERENT than color of piece in position
                    print("Lower left move contains piece of different color, move appended")
                    availMoves.append([lowerLeftRow, lowerLeftCol])
                else:
                    print("Current piece and lower left position are same color")
            else:
                print("Lower left position is off board by column")
        else:
            print("Lower left position is off board by row")

        #UPPER LEFT
        upperLeftRow = currPosRow + 1
        upperLeftCol = currPosCol - 2
        if (upperLeftRow < len(board[0])):
            if (upperLeftCol < len(board[0][0])):
                print(str(len(board[0]) - 1))
                print(str(upperLeftRow))
                print(str(upperLeftCol))
                posPiece = checkPos(board, upperLeftRow, upperLeftCol)
                if posPiece == ' ':
                    print("Upper left target position is empty")
                    availMoves.append([upperLeftRow, upperLeftCol])
                elif (posPiece[0] != piece[0]):
                    #Current piece color DIFFERENT than color of piece in position
                    print("Upper left move contains piece of different color, move appended")
                    availMoves.append([upperLeftRow, upperLeftCol])
                else:
                    print("Current piece and upper left position are same color")
            else:
                print("Upper left position is off board by column")
        else:
            print("Upper left position is off board by row")

        #TOP LEFT
        topLeftRow = currPosRow + 2
        topLeftCol = currPosCol - 1
        if (topLeftRow < len(board[0])):
            if (topLeftCol < len(board[0])):
                posPiece = checkPos(board, topLeftRow, topLeftCol)
                if posPiece == ' ':
                    print("Top left target position is empty")
                    availMoves.append([topLeftRow, topLeftCol])
                elif (posPiece[0] != piece[0]):
                    #Current piece color DIFFERENT than color of piece in position
                    print("Top left move contains piece of different color, move appended")
                    availMoves.append([topLeftRow, topLeftCol])
                else:
                    print("Current piece and top left position are same color")
            else:
                print("Top left position is off board by column")
        else:
            print("Top left position is off board by row")

        #return availMoves
    
    if ('rook' in piece.lower() or 'queen' in piece.lower()):
        print("Finding available moves for rook or queen")
        currPosRow, currPosCol = findPiecePos(board, piece)
        #All rows going up
        posPiece = ' '
        moveIncr = 1
        while posPiece == ' ':
            if (currPosRow+moveIncr >= len(board[0])):
                break
            posPiece = checkPos(board, currPosRow+moveIncr, currPosCol)
            availMoves.append([currPosRow+moveIncr, currPosCol])
            moveIncr = moveIncr + 1
            continue
        print("Found all moves going up: " + str(availMoves))

        #All columns going right
        posPiece = ' '
        moveIncr = 1
        while posPiece == ' ':
            if (currPosCol+moveIncr >= len(board[0])):
                break
            print("Adding move to the right..")
            posPiece = checkPos(board, currPosRow, currPosCol+moveIncr)
            availMoves.append([currPosRow, currPosCol+moveIncr])
            moveIncr = moveIncr + 1
            continue
        print("Found all moves going right: " + str(availMoves))

        #All rows going down
        posPiece = ' '
        moveIncr = 1
        while posPiece == ' ':
            if (currPosRow-moveIncr < 0):
                break
            posPiece = checkPos(board, currPosRow-moveIncr, currPosCol)
            availMoves.append([currPosRow-moveIncr, currPosCol])
            moveIncr = moveIncr + 1
            continue
        print("Found all moves going down: " + str(availMoves))

        #All columns going left
        posPiece = ' '
        moveIncr = 1
        while posPiece == ' ':
            if (currPosCol-moveIncr < 0):
                break
            posPiece = checkPos(board, currPosRow, currPosCol-moveIncr)
            availMoves.append([currPosRow, currPosCol-moveIncr])
            moveIncr = moveIncr + 1
            continue
        print("Found all moves going left: " + str(availMoves))

    if ('king' in piece.lower()):
        print("Finding available moves for king")
        currPosRow, currPosCol = findPiecePos(board, piece)
        posPiece = ' '
        moveIncr = 1
        #Move right 1 column
        if (currPosCol+moveIncr <= len(board[0])):
            availMoves.append([currPosRow, currPosCol+moveIncr])

        #Move upper right
        if (currPosCol+moveIncr <= len(board[0]) and currPosRow+moveIncr <= len(board[0])):
            availMoves.append([currPosRow+moveIncr, currPosCol+moveIncr])

        #Move up 1 row
        if (currPosRow+moveIncr <= len(board[0])):
            availMoves.append([currPosRow+moveIncr, currPosCol])

        #Move upper left
        if (currPosCol-moveIncr <= len(board[0]) and currPosRow+moveIncr <= len(board[0])):
            availMoves.append([currPosRow+moveIncr, currPosCol-moveIncr])

        #Move Left 1 column
        if (currPosCol-moveIncr <= len(board[0])):
            availMoves.append([currPosRow, currPosCol-moveIncr])

        #Move lower left
        if (currPosCol-moveIncr <= len(board[0]) and currPosRow-moveIncr <= len(board[0])):
            availMoves.append([currPosRow-moveIncr, currPosCol-moveIncr])

        #Move Down 1 row
        if (currPosRow-moveIncr <= len(board[0])):
            availMoves.append([currPosRow-moveIncr, currPosCol])

        #Move lower right
        if (currPosCol+moveIncr <= len(board[0]) and currPosRow-moveIncr <= len(board[0])):
            availMoves.append([currPosRow-moveIncr, currPosCol+moveIncr])

    if (len(availMoves) > 1):
        return availMoves
    else:
        print("current piece is not a pawn / rook / bishop / queen")
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
