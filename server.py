import config
import socket

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.bind((socket.gethostname(), config.port))
sock.listen(5)

while True:
    client_sock, address = sock.accept()
    print(f'connected from: {address}')
    client_sock.send(bytes('This is a test', 'utf-8'))
