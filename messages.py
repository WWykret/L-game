import socket
import config
from typing import Tuple, List
import block


def get_msg_type(sock: socket.socket) -> int:
    msg = sock.recv(3).decode('utf-8')
    try:
        return config.MSG_TYPES[msg]
    except KeyError:
        return -1


def get_initial_config(sock: socket.socket) -> \
        Tuple[int, int, List[block.Block], List[Tuple[int, int]]]:
    config_str = sock.recv(2).decode('utf-8')
    player_num = int(config_str[0])
    current_turn = int(config_str[1])
    blocks, coins = get_config(sock)
    return player_num, current_turn, blocks, coins


def get_config(sock: socket.socket) -> Tuple[List[block.Block], List[Tuple[int, int]]]:
    config_str = sock.recv(12).decode('utf-8')
    print(config_str)
    blocks = [get_block_from_str(config_str[0:4]), get_block_from_str(config_str[4:8])]
    coins = [(int(config_str[8]), int(config_str[9])), (int(config_str[10]), int(config_str[11]))]
    return blocks, coins


def get_block_from_str(block_str: str) -> block.Block:
    x = int(block_str[0])
    y = int(block_str[1])
    rotation = int(block_str[2])
    flipped = (int(block_str[3]) == 1)
    return block.Block(x, y, rotation, flipped)


def get_state_string(state: Tuple[List[block.Block], List[Tuple[int, int]]]):
    state_str = ''
    for l_block in state[0]:
        temp_str = f'{l_block.x}{l_block.y}{l_block.rotation}{1 if l_block.inverted else 0}'
        state_str += temp_str
        print(temp_str)

    for pair in state[1]:
        state_str += str(pair[0]) + str(pair[1])

    return state_str
