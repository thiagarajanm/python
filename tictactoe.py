from __future__ import print_function


game_board = {'a1': '', 'a2': '', 'a3': '',
              'b1': '', 'b2': '', 'b3': '',
              'c1': '', 'c2': '', 'c3': ''}


def print_board(board):
    print(board['a1'] + '|' + board['a2'] + '|' + board['a3'])
    print('-----')
    print(board['b1'] + '|' + board['b2'] + '|' + board['b3'])
    print('-----')
    print(board['c1'] + '|' + board['c2'] + '|' + board['c3'])
    return ''


print(print_board(game_board))


def choose_player():
    # choice = ''
    # while not (choice == 'X' or choice == 'O'):
    #     choice = raw_input('Please enter the player symbol "X" or "O". Not anything else!').upper()
    #     print(choice)
    # return choice
    while True:
        choice = raw_input('Please enter the player symbol "X" or "O". Not anything else!').upper()
        if choice == 'X' or choice == 'O':
            return choice
            break
        else:
            continue

def check_space(board,value,user):
    while True:
        if board[value] == '':
            board[value] = user
            break
        else:
            print('Board value ' + value + ' already entered. Please enter value for empty board value')
            value = raw_input()
            continue


def winner(board, play):
    if (board['a1'] == board['a2'] == board['a3'] == play) or \
       (board['b1'] == board['b2'] == board['b3'] == play) or \
       (board['c1'] == board['c2'] == board['c3'] == play) or \
       (board['a1'] == board['b1'] == board['c1'] == play) or \
       (board['a2'] == board['b2'] == board['c2'] == play) or \
       (board['a3'] == board['b3'] == board['c3'] == play) or \
       (board['a1'] == board['b2'] == board['c3'] == play) or \
       (board['c1'] == board['b2'] == board['a3'] == play):
        return True
    else:
        return False


player = choose_player()


for i in range(9):
    if player == 'X':
        game_value = raw_input('Player X enter the column and row to mark the board: ')
        check_space(game_board,game_value,player)
        print(print_board(game_board))
        if winner(game_board, player):
            print(player + ' won the game')
            break
        player = 'O'
        # else:
        #     print('Board value ' + game_value + ' already entered. Please enter value for empty board value')
    else:
        game_value = raw_input('Player O enter the column and row to mark the board: ')
        check_space(game_board, game_value, player)
        # if game_board[game_value] == '':
        #     game_board[game_value] = 'O'
        print(print_board(game_board))
        if winner(game_board,player):
            print(player + ' won the game')
            break
        player = 'X'
        # else:
        #     print('Board value ' + game_value + ' already entered. Please enter value for empty board value')
