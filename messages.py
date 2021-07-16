import socket
import config
from typing import Tuple, List
import block
from board import Board


def get_msg_type(sock: socket.socket) -> int:
    msg = sock.recv(3).decode('utf-8')
    try:
        return config.MSG_TYPES[msg]
    except KeyError:
        return -1


def get_initial_config(sock: socket.socket) -> \
        Tuple[int, int, Board]:
    config_str = sock.recv(2).decode('utf-8')
    player_num = int(config_str[0])
    current_turn = int(config_str[1])
    board_config_str = get_config_str(sock)
    board = Board(None, None)
    board.get_board_from_str(board_config_str)
    return player_num, current_turn, board


def get_config_str(sock: socket.socket) -> str:
    config_str = sock.recv(12).decode('utf-8')
    return config_str
