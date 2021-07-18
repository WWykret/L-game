import config
from enum import IntEnum


class PlayerState(IntEnum):
    MOVE_BLOCK = 0
    SELECT_COIN = 1
    MOVE_COIN = 2
    SEND_DATA_TO_SERVER = 3
    WAIT_FOR_TURN = 4


class Player:

    def __init__(self, player_id: int, player_turn: bool) -> None:
        self.player_id = player_id
        self.color = config.PLAYER_COLORS[player_id]
        self.state = PlayerState.MOVE_BLOCK if player_turn else PlayerState.WAIT_FOR_TURN
        self.selected_coin = 0

    def switch_selected_coin(self) -> None:
        self.selected_coin = 1 - self.selected_coin

    def go_to_next_state(self, is_move_legal: bool) -> None:
        if self.state == PlayerState.MOVE_BLOCK and is_move_legal:
            self.state = PlayerState.SELECT_COIN
        elif self.state == PlayerState.MOVE_COIN and is_move_legal:
            self.state = PlayerState.SEND_DATA_TO_SERVER
        elif self.state == PlayerState.SELECT_COIN:
            self.state = PlayerState.MOVE_COIN

