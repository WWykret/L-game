import pygame
import config
import block
from typing import List


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

    def update(self, blocks: List[block.Block], coins: List[block.Coin], curr_player: int):
        self.draw_grid()
        for player, l_block in enumerate(blocks):
            self.draw_block(l_block, player)
        for coin in coins:
            x, y = coin.get_pos()
            pygame.draw.rect(self.screen, config.YELLOW, get_rect(x, y))
        if 0 <= curr_player < len(blocks):
            self.draw_block(blocks[curr_player], curr_player)
        pygame.display.flip()

    def draw_grid(self):
        self.screen.fill(color=config.BLACK)
        for y in range(config.GRID_SIZE):
            for x in range(config.GRID_SIZE):
                pygame.draw.rect(self.screen, config.WHITE, get_rect(x, y))

    def draw_block(self, l_block, player):
        for (x, y) in l_block:
            pygame.draw.rect(self.screen, config.PLAYER_COLORS[player], get_rect(x, y))
