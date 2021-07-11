import block
import pygame


def react_to_key_press(l_block: block.Block, key: int) -> bool:
    if key == pygame.K_LEFT:
        l_block.move(-1, 0)
    elif key == pygame.K_RIGHT:
        l_block.move(1, 0)
    elif key == pygame.K_UP:
        l_block.move(0, -1)
    elif key == pygame.K_DOWN:
        l_block.move(0, 1)
    elif key == pygame.K_r:
        l_block.rotate()
    elif key == pygame.K_f:
        l_block.flip()
    elif key == pygame.K_SPACE:
        return True
    return False
