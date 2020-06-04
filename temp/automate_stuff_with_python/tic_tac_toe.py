import random


def inputPlayerLetter():
    # playerLetter = input("Do you want to be X or O? ").upper()
    playerLetter = ''
    while playerLetter not in ('X', 'O'):
        playerLetter = input("Invalid letter, please again. Do you want to be X or O?\n>>>").upper()

    if playerLetter == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def whoGoesFirst():
    if random.randint(0, 1) == 1:
        return 'computer'
    else:
        return 'player'

def drawBoard(board):
    print(' {} | {} | {} '.format(board[7], board[8], board[9]))
    print('---+---+---')
    print(' {} | {} | {} '.format(board[4], board[5], board[6]))
    print('---+---+---')
    print(' {} | {} | {} '.format(board[1], board[2], board[3]))

def isSpace(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpace(board, int(move)):
        move = input('What is your next move?(1-9) ')

    return int(move)

def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def chooseRandomMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpace(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    playerLetter = 'O' if computerLetter == 'X' else 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpace(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for j in range(1, 10):
        copy = getBoardCopy(board)
        if isSpace(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return j

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if isSpace(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])



def makeMove(board, letter, move=0):
    board[move]  = letter

def isWinner(board, letter):
    return ((board[7] == board[8] == board[9] == letter) or
            (board[4] == board[5] == board[6] == letter) or
            (board[1] == board[2] == board[3] == letter) or
            (board[1] == board[4] == board[7] == letter) or
            (board[2] == board[5] == board[8] == letter) or
            (board[3] == board[6] == board[9] == letter) or
            (board[1] == board[5] == board[9] == letter) or
            (board[3] == board[5] == board[7] == letter)
            )

def isBoardFull(board):
    return (' ' not in board[1:10])

def playAgain():
    return input("Do you want to play again? (yes or no)").lower().startswith('y')

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('the {} will go first.'.format(turn))
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            print(move)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Hooray, You have won the game!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie.")
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("The computer has beaten you, you lose.")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break