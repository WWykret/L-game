import socket
import config
from window import Window
import pygame
import controler
import messages
import threading
from board import Board

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.connect((config.ADDRESS, config.PORT))

window = Window()

player = 0
player_state = 0  # 0-move block, 1-send to server, 2-wait for turn, 3-wait for response, 4-select coin, 5-move coin

running = True
board = Board(None, None)


def recv_message():
    global player, player_state, board, running
    while running:
        msg_type = messages.get_msg_type(sock)
        if msg_type == config.MSG_TYPES['ini']:
            player, player_turn, board = messages.get_initial_config(sock)
            player_state = 0 if player == player_turn else 2
        elif msg_type == config.MSG_TYPES['acp']:
            player_state = 2
        elif msg_type == config.MSG_TYPES['tur']:
            print(f'{player=}')
            board.get_board_from_str(messages.get_config_str(sock))
            player_state = 0


recv_thread = threading.Thread(target=recv_message, args=[])
recv_thread.start()

selected_coin = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sock.close()
            running = False
        elif event.type == pygame.KEYDOWN:
            if player_state == 0:
                player_state = controler.react_to_key_press((board, 'blocks', player), event.key, player_state)
            elif player_state == 4:
                player_state, selected_coin = controler.react_to_key_press(selected_coin, event.key, player_state)
            elif player_state == 5:
                player_state = controler.react_to_key_press((board, 'coins', selected_coin), event.key, player_state)

    if player_state == 1:
        sock.send(bytes(f'sta{str(board)}', 'utf-8'))
        player_state = 3

    window.update(board=board, curr_player=player, curr_coin=selected_coin, curr_state=player_state)
