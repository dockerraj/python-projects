from __future__ import print_function
from IPython.display import clear_output
def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
def player_input():
    player_markers={'p1':'','p2':''}
    
    print("Player 1, Choose your marker - X or O ? ")
    player_markers['p1']=raw_input('Player 1: Do you want to be X or O? ').upper()
    if (player_markers['p1']=='X'):
        player_markers['p2']='O'
    elif(player_markers['p1']=='O'):
        player_markers['p2']='X'
    else:
        player_markers=player_input()
    return player_markers
