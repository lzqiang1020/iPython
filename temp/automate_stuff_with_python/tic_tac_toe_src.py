import random

# theBoard = {
#     7: 'O', 8: 'O', 9: 'O',
#     4: 'X', 5: 'X', 6: ' ',
#     1: ' ', 2: ' ', 3: 'X'
# }
# theBoard = [' ', ' ', ' ', 'X', 'X', 'X', ' ', 'O', 'O', 'O']

# 绘制棋盘
def draw_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])      # 7 | 8 | 9
    print('--+---+--')                                         # --+---+---
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])      # 4 | 5 | 6
    print('--+---+--')                                         # --+---+---
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])      # 1 | 2 | 3

# 玩家选子（X, O)
def input_player_letter():
    letter = ' '
    while not(letter == 'X' or letter == 'O'):
        letter = input('Do you want to be X or O?').upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

# 确定谁先落子
def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

# 是否再来一盘
def play_again():
    return input('Do you want to play again? (yes or no)').lower().startswith('y')

# 判断棋盘指定位置是否为空
def is_space_free(board, move):
    return board[move] == ' '

# 获取player的落子（含其落子是否合法）
def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        move = input('What is your next move? (1-9)')
    return int(move)

# 从当前棋盘任选一个可落子的位置
def choose_random_move_fromlist(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

# 复制当前棋盘
def get_board_copy(board):
    dupe_board = []

    for i in board:
        dupe_board.append(i)

    return dupe_board

# 落子
def make_move(board, letter, move):
    board[move] = letter

# 判断是否取胜
def is_winner(bo, le):
    return (
            (bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)     # diagonal
    )

# 获取机器落子位置
def get_computer_move(board, computer_letter):
    player_letter = 'O' if computer_letter == 'X' else 'X'
    # 落子后取胜的位置，有则在其落子
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i
    # 验证玩家下一步落子后有无取胜的位置，有则提前落子堵上
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, i):
                return i

    move = choose_random_move_fromlist(board, [1, 3, 7, 9])
    if move != None:
        return move
    if is_space_free(board, 5):
        return 5
    return choose_random_move_fromlist(board, [2, 4, 6, 8])

# 判断棋盘是否已满
def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    else:
        return True


# begin
print('Welcome to Tic Tac Toe!')
while True:
    the_board = [' '] * 10
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print('The {} will go first'.format(turn))
    game_is_playing = True

    while game_is_playing:
        if turn == 'player':
            draw_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)

            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print('Hooray! You have won the game!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)

            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print('The computer has beaten you! You lose.')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
