import config
import socket
import threading
import messages

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.bind((socket.gethostname(), config.PORT))
sock.listen(5)

print('Server is running...')

players = []


def game_loop():
    for player_index, player in enumerate(players):
        message = f'ini{player_index}0120021200033'  # index, turn, block1, block2, coin1, coin2
        player.send(bytes(message, 'utf-8'))
    turn = 0
    while True:
        msg_type = messages.get_msg_type(players[turn])
        print(msg_type)
        if msg_type == 'sta':
            state = players[turn].recv(12).decode('utf-8')
            players[1 - turn].send(bytes(f'tur{state}', 'utf-8'))
            turn = 1 - turn


while len(players) < 2:
    client_sock, address = sock.accept()
    if len(players) < 2:
        players.append(client_sock)
    print(f'connected from: {address}')

game = threading.Thread(target=game_loop, args=[])
game.start()
