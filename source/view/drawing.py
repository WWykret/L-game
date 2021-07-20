import pygame
from source import config
from source.model.block import BoardElement
from typing import Tuple, Optional


def get_rect(x: int, y: int) -> pygame.Rect:
    rect = (
        x * config.RECT_SIZE + x * config.SPACING,
        y * config.RECT_SIZE + y * config.SPACING,
        config.RECT_SIZE,
        config.RECT_SIZE
    )
    return pygame.Rect(rect)


def draw_grid(screen: pygame.display) -> None:
    screen.fill(color=config.BLACK)
    for y in range(config.GRID_SIZE):
        for x in range(config.GRID_SIZE):
            pygame.draw.rect(screen, config.WHITE, get_rect(x, y))


def draw_board_element(screen: pygame.display, element: BoardElement,
                       color: Optional[Tuple[int, int, int]] = None) -> None:
    for (x, y) in element:
        if color is not None:
            pygame.draw.rect(screen, color, get_rect(x, y))
        else:
            pygame.draw.rect(screen, element.color, get_rect(x, y))
