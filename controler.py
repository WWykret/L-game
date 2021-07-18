from board import Board
from player import Player, PlayerState
import pygame


def react_to_key_press(player: Player, board: Board, key: int) -> None:
    if player.state in [PlayerState.MOVE_BLOCK, PlayerState.MOVE_COIN]:
        if player.state == PlayerState.MOVE_BLOCK:
            element = board.blocks[player.player_id]
        else:
            element = board.coins[player.selected_coin]

        if key == pygame.K_LEFT:
            element.move(-1, 0)
        elif key == pygame.K_RIGHT:
            element.move(1, 0)
        elif key == pygame.K_UP:
            element.move(0, -1)
        elif key == pygame.K_DOWN:
            element.move(0, 1)
        elif key == pygame.K_r:
            element.rotate()
        elif key == pygame.K_f:
            element.flip()
    elif key == pygame.K_r:
        player.switch_selected_coin()

    if key == pygame.K_SPACE:
        is_move_legal = board.check_board_state()
        player.go_to_next_state(is_move_legal)
