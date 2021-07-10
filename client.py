import socket
import config
from window import Window
import pygame
from block import Block

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.connect((config.ADDRESS, config.PORT))

window = Window()
msg = sock.recv(1024)
print(f'recived msg = {msg.decode("utf-8")}')

blocks = [
    Block(1, 2, 0, False),
    Block(2, 1, 2, False)
]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.update(blocks=blocks)
