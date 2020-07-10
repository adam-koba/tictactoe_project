# TicTacToe
board = [ ' ' for x in range(10)]

def insertSign(sign, pos):
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
    return ((bo[1] == sg and bo[2] == sg and bo[3] == sg) or # across the top row
    (bo[4] == sg and bo[5] == sg and bo[6] == sg) or # across the middle row
    (bo[7] == sg and bo[8] == sg and bo[9] == sg) or # across the bottom row
    (bo[1] == sg and bo[5] == sg and bo[9] == sg) or # diagonal
    (bo[7] == sg and bo[5] == sg and bo[3] == sg) or # diagonal
    (bo[1] == sg and bo[4] == sg and bo[7] == sg) or # down the left side
    (bo[2] == sg and bo[5] == sg and bo[8] == sg) or # down the middle
    (bo[3] == sg and bo[6] == sg and bo[9] == sg)) # down the right side

# choosing position to put X
def playerMove():
    run = True
    while run:
        move = input('Please select a position to place \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertSign('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Type a number within the range!')
        except:
            print('Please print a number!')
#
def compMove():
    pass

#
def selectRandom():
    pass

# checking if the board is full
def isBoardFull():
    if board.count(' ') > 1:
        return True
    else:
        return False
#
def main():
    print('TicTacToe Game. The board has position from 1 to 9 starting at the top left. To win you have to complete line of your sign (diagonal, horizontal or vertical)')
    printBoard()

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print('Sorry, opponent won this time ...')
            break
        if not(isWinner(board, 'X')):
            compMove()
            printBoard()
        else:
            print('YOU WON!')
            break


    if isBoardFull(board):
        print('Tie Game!')

