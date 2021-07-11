import socket
import config
from window import Window
import pygame
from block import Block
import controler
import messages

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.connect((config.ADDRESS, config.PORT))

window = Window()

blocks = [
    # Block(1, 2, 0, False),
    # Block(2, 1, 2, False)
]

coins = [
    # (0, 0),
    # (3, 3)
]

player = 0
player_turn = 0
waiting_for_turn = True

msg_type = messages.get_msg_type(sock)
if msg_type == config.MSG_TYPES['ini']:
    player, player_turn, blocks, coins = messages.get_initial_config(sock)
    waiting_for_turn = (player == player_turn)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            controler.react_to_key_press(blocks[player], event.key)

    keys = pygame.key.get_pressed()

    window.update(blocks=blocks, coins=coins, curr_player=player)
