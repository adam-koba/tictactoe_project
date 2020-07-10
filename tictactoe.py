# TicTacToe

# board
# display board
# play game

board = [' ' for x in range(10)]

def insertLetter(sign, pos):
    global board
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

# This function return True if player win
# sg is for sign, that means it is X or O
def isWinner(bo, sg):
    return (bo[1] == sg and bo[2] == sg and bo[3] == sg) or # across the top row
    (bo[4] == sg and bo[5] == sg and bo[6] == sg) or # across the middle row
    (bo[7] == sg and bo[8] == sg and bo[9] == sg) or # across the bottom row
    (bo[1] == sg and bo[5] == sg and bo[9] == sg) or # diagonal
    (bo[7] == ag and bo[5] == sg and bo[3] == sg) or # diagonal
    (bo[1] == sg and bo[4] == sg and bo[7] == sg) or # down the left side
    (bo[2] == sg and bo[5] == sg and bo[8] == sg) or # down the middle
    (bo[3] == sg and bo[6] == sg and bo[9] == sg) # down the right side

