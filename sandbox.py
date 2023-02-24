
from chessSimFuncs import checkPos
from chessSimFuncs import movePiece
from chessSimFuncs import displayBoard


board = [['WPawn1', 'WPawn2', 'WPawn3', 'WPawn4'],[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], ['BPawn1', 'BPawn2', 'BPawn3', 'BPawn4']]

print(board)

displayBoard(board)

movePiece(board, 'WPawn1', 1, 1)

print('Updated board')

displayBoard(board)


BKing