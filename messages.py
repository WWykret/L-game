import socket
import config
from typing import Tuple, List
import block


def get_msg_type(sock: socket.socket) -> int:
    return config.MSG_TYPES[sock.recv(3).decode('utf-8')]


def get_initial_config(sock: socket.socket) -> \
        Tuple[int, int, List[block.Block], List[Tuple[int, int]]]:
    config_str = sock.recv(14).decode('utf-8')
    player_num = int(config_str[0])
    current_turn = int(config_str[1])
    blocks = [get_block_from_str(config_str[2:6]), get_block_from_str(config_str[6:10])]
    coins = [(int(config_str[10]), int(config_str[11])), (int(config_str[12]), int(config_str[13]))]
    return player_num, current_turn, blocks, coins


def get_block_from_str(block_str: str) -> block.Block:
    x = int(block_str[0])
    y = int(block_str[1])
    rotation = int(block_str[2])
    flipped = (int(block_str[3]) == 1)
    return block.Block(x, y, rotation, flipped)
