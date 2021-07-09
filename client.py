import socket
import config

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.connect((config.address, config.port))
msg = sock.recv(1024)
print(f'recived msg = {msg.decode("utf-8")}')
