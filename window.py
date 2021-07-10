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

    def update(self, blocks: List[block.Block]):
        self.draw_grid()
        for l_block in blocks:
            self.draw_block(l_block)
        pygame.display.flip()

    def draw_grid(self):
        self.screen.fill(color=config.BLACK)
        for y in range(config.GRID_SIZE):
            for x in range(config.GRID_SIZE):
                pygame.draw.rect(self.screen, config.WHITE, get_rect(x, y))

    def draw_block(self, l_block):
        for (x, y) in l_block:
            pygame.draw.rect(self.screen, config.RED, get_rect(x, y))
