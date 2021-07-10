import socket
import config
from window import Window
import pygame

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.connect((config.ADDRESS, config.PORT))

window = Window()
msg = sock.recv(1024)
print(f'recived msg = {msg.decode("utf-8")}')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.update()
