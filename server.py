import config
import socket
import threading

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.bind((socket.gethostname(), config.PORT))
sock.listen(5)

print('Server is running...')

players = []


def game_loop():
    print(players)
    for player_index, player in enumerate(players):
        message = f'ini{player_index}0120021200033'  # index, turn, block1, block2, coin1, coin2
        print(message)
        player.send(bytes(message, 'utf-8'))


while len(players) < 2:
    client_sock, address = sock.accept()
    if len(players) < 2:
        players.append(client_sock)
    print(f'connected from: {address}')

game = threading.Thread(target=game_loop, args=[])
game.start()
