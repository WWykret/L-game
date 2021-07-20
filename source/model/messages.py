import socket
from typing import Tuple
from source.model.board import Board
from source.model.player import Player


def get_msg_type(sock: socket.socket) -> str:
    try:
        return sock.recv(3).decode('utf-8')
    except KeyError:
        return ''


def get_initial_config(sock: socket.socket) -> Tuple[Player, Board]:
    player_config_str = sock.recv(2).decode('utf-8')
    player_id = int(player_config_str[0])
    current_turn = int(player_config_str[1])

    board_config_str = get_config_str(sock)
    board = Board(None, None)
    board.get_board_from_str(board_config_str)
    return Player(player_id=player_id, player_turn=player_id == current_turn), board


def get_config_str(sock: socket.socket) -> str:
    return sock.recv(12).decode('utf-8')
