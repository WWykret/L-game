import pygame
from source import config
from source.model.board import Board
from source.model.player import Player, PlayerState
from source.view.drawing import draw_grid, draw_board_element


class Window:
    def __init__(self):
        self.width = config.GRID_SIZE * (config.RECT_SIZE + config.SPACING) - config.SPACING
        self.height = config.GRID_SIZE * (config.RECT_SIZE + config.SPACING) - config.SPACING

        self.screen = pygame.display.set_mode(size=(self.width, self.height))
        pygame.display.set_caption('L-Game')

    def update(self, board: Board, player: Player):
        draw_grid(self.screen)

        for element in board.blocks + board.coins:
            draw_board_element(self.screen, element)

        if player.player_id != -1 and player.state == PlayerState.MOVE_BLOCK:
            draw_board_element(self.screen, board.blocks[player.player_id])

        if player.state == PlayerState.SELECT_COIN:
            draw_board_element(self.screen, board.coins[player.selected_coin], config.GREEN)

        pygame.display.flip()
