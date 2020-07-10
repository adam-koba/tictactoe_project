# TicTacToe

# board
# display board
# play game

board = [' ' for x in range(10)]

def insertLetter(sign, pos)
    board[pos] = sign
def spaceIsFree(pos):
    return board[pos] == ' '
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('------------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('------------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')