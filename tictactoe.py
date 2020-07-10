board = [ ' ' for x in range(10)]

def insertSign(sign, pos):
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
    return (bo[1] == sg and bo[2] == sg and bo[3] == sg) or (bo[4] == sg and bo[5] == sg and bo[6] == sg) or (bo[7] == sg and bo[8] == sg and bo[9] == sg) or (bo[1] == sg and bo[5] == sg and bo[9] == sg) or (bo[7] == sg and bo[5] == sg and bo[3] == sg) or (bo[1] == sg and bo[4] == sg and bo[7] == sg) or (bo[2] == sg and bo[5] == sg and bo[8] == sg) or (bo[3] == sg and bo[6] == sg and bo[9] == sg)

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

# AI for opponent
# first checking for free position on corners after that if there is free position on center
# then checking if there is position on center of the sides (2, 4, 6 or 8 pos)
def compMove():
    possibleMoves = [x for x, sign in enumerate(board) if sign == ' ' and x != 0]
    move = 0

    for sgn in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = sgn
            if isWinner(boardCopy, sgn):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

# checking if the board is full
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print('TicTacToe Game.\nThe board has position from 1 to 9 starting at the top left.\nTo win you have to complete line of your sign (diagonal, horizontal or vertical).')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, opponent won this time ...')
            break
        if not(isWinner(board, 'X')):
            # program checking if there is a position were opponent can place sign
            # if not it is TIE GAME
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertSign('O', move)
                print('Computer placed an \' O \' in position', move, ':')
                printBoard(board)
        else:
            print('YOU WON!')
            break


    if isBoardFull(board):
        print('Tie Game!')


while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('----------------------------')
        main()
    else:
        break