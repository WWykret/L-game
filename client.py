import socket
import config
from window import Window
import pygame
import controler
import messages
import threading
from board import Board
from player import Player, PlayerState

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.connect((config.ADDRESS, config.PORT))

window = Window()

player = Player(-1, False)

running = True
board = Board(None, None)


def recv_message():
    global player, board
    while True:
        msg_type = messages.get_msg_type(sock)
        if msg_type == 'ini':
            player, board = messages.get_initial_config(sock)
        elif msg_type == 'tur':
            board.get_board_from_str(messages.get_config_str(sock))
            player.state = PlayerState.MOVE_BLOCK


recv_thread = threading.Thread(target=recv_message, args=[])
recv_thread.start()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sock.close()
            running = False
        elif event.type == pygame.KEYDOWN:
            controler.react_to_key_press(player, board, event.key)

    if player.state == PlayerState.SEND_DATA_TO_SERVER:
        sock.send(bytes(f'sta{str(board)}', 'utf-8'))
        player.state = PlayerState.WAIT_FOR_TURN

    window.update(board=board, player=player)
