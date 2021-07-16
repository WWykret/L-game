from block import Block, Coin
from typing import Tuple, Optional


def does_board_intersect(blocks: Tuple[Block, Block], coins: Tuple[Coin, Coin]) -> bool:
    for block1 in blocks:
        for block2 in blocks:
            if block1 is block2:
                continue
            for pos1 in block1:
                for pos2 in block2:
                    if pos1 == pos2:
                        return True
        for coin in coins:
            for pos in block1:
                if pos == coin.get_pos():
                    return True
    return False


def get_block_from_str(block_str: str) -> Block:
    x = int(block_str[0])
    y = int(block_str[1])
    rotation = int(block_str[2])
    flipped = (int(block_str[3]) == 1)
    return Block(x, y, rotation, flipped)


class Board:
    def __init__(self, blocks: Optional[Tuple[Block, Block]]=None, coins: Optional[Tuple[Coin, Coin]]=None) -> None:
        if blocks is not None:
            self.blocks = blocks
        else:
            self.blocks = ()
        if coins is not None:
            self.coins = coins
        else:
            self.coins = ()

    def change_board_state(self, blocks: Tuple[Block, Block], coins: Tuple[Coin, Coin]) -> bool:
        new_blocks_set = {block.get_pos() for block in blocks}
        old_blocks_set = {block.get_pos() for block in self.blocks}
        if old_blocks_set == new_blocks_set:
            return False
        elif does_board_intersect(blocks, coins):
            return False
        else:
            self.blocks = blocks
            self.coins = coins
            return True

    def get_board_from_str(self, config_str: str) -> None:
        blocks = (get_block_from_str(config_str[0:4]), get_block_from_str(config_str[4:8]))
        coins = (Coin((int(config_str[8]), int(config_str[9]))),
                 Coin((int(config_str[10]), int(config_str[11]))))
        self.blocks = blocks
        self.coins = coins

    def __str__(self):
        state_str = ''
        for block in self.blocks:
            state_str += str(block)
        for coin in self.coins:
            state_str += str(coin)
        return state_str
