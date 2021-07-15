import block
import pygame
from typing import Union


def react_to_key_press(element: Union[block.Block, block.Coin], key: int, curr_state: int) -> int:
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
    elif key == pygame.K_SPACE:
        if curr_state == 0:
            return 4
        elif curr_state == 4:
            return 5
        elif curr_state == 5:
            return 1
    return curr_state

