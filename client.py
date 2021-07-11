import socket
import config
from window import Window
import pygame
from block import Block
import controler

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.connect((config.ADDRESS, config.PORT))

window = Window()
msg = sock.recv(1024)
print(f'recived msg = {msg.decode("utf-8")}')

blocks = [
    Block(1, 2, 0, False),
    Block(2, 1, 2, False)
]

coins = [
    (0, 0),
    (3, 3)
]

player = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            controler.move_rotate_block(blocks[player], event.key)

    keys = pygame.key.get_pressed()

    window.update(blocks=blocks, coins=coins, curr_player=player)
