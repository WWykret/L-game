import pygame
import config
from board import Board
from player import Player, PlayerState


def get_rect(x: int, y: int) -> pygame.Rect:
    rect = (
        x * config.RECT_SIZE + x * config.SPACING, y * config.RECT_SIZE + y * config.SPACING,
        config.RECT_SIZE,
        config.RECT_SIZE
    )
    return pygame.Rect(rect)


class Window:
    def __init__(self):
        self.width = config.GRID_SIZE * (config.RECT_SIZE + config.SPACING) - config.SPACING
        self.height = config.GRID_SIZE * (config.RECT_SIZE + config.SPACING) - config.SPACING

        self.screen = pygame.display.set_mode(size=(self.width, self.height))
        pygame.display.set_caption('L-Game')

    def update(self, board: Board, player: Player):
        self.draw_grid()
        for player_id, l_block in enumerate(board.blocks):
            self.draw_block(l_block, config.PLAYER_COLORS[player_id])
        for coin in board.coins:
            x, y = coin.get_pos()
            pygame.draw.rect(self.screen, config.YELLOW, get_rect(x, y))
        if player.player_id != -1 and player.state == PlayerState.MOVE_BLOCK:
            self.draw_block(board.blocks[player.player_id], player.color)
        if player.state == PlayerState.SELECT_COIN:
            x, y = board.coins[player.selected_coin].get_pos()
            pygame.draw.rect(self.screen, config.GREEN, get_rect(x, y))
        pygame.display.flip()

    def draw_grid(self):
        self.screen.fill(color=config.BLACK)
        for y in range(config.GRID_SIZE):
            for x in range(config.GRID_SIZE):
                pygame.draw.rect(self.screen, config.WHITE, get_rect(x, y))

    def draw_block(self, l_block, color):
        for (x, y) in l_block:
            pygame.draw.rect(self.screen, color, get_rect(x, y))
