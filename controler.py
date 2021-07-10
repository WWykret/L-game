import block
import pygame


def move_rotate_block(l_block: block.Block, key: int):
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

