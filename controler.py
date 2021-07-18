from board import Board
import pygame
from typing import Union, Tuple


def react_to_key_press(element: Union[Tuple[Board, str, int], int], key: int, curr_state: int) -> \
        Union[int, Tuple[int, int]]:
    if not isinstance(element, int):
        moved_element = getattr(element[0], element[1])
        if key == pygame.K_LEFT:
            moved_element[element[2]].move(-1, 0)
        elif key == pygame.K_RIGHT:
            moved_element[element[2]].move(1, 0)
        elif key == pygame.K_UP:
            moved_element[element[2]].move(0, -1)
        elif key == pygame.K_DOWN:
            moved_element[element[2]].move(0, 1)
        elif key == pygame.K_r:
            moved_element[element[2]].rotate()
        elif key == pygame.K_f:
            moved_element[element[2]].flip()
    elif key == pygame.K_r:
        return curr_state, (1 - element)

    if key == pygame.K_SPACE:
        if curr_state == 0:
            if element[0].check_board_state():
                return 4
            else:
                return 0
        elif curr_state == 4:
            return 5, element
        elif curr_state == 5:
            if element[0].check_board_state():
                return 1
            else:
                return 5
    if curr_state == 4:
        return curr_state, element
    else:
        return curr_state
