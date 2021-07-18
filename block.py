from __future__ import annotations

import operator
import config
from typing import Tuple, Optional


class BoardElement:
    def __init__(self, x: int, y: int, rotation: Optional[int] = None, inverted: Optional[bool] = None) -> None:
        self.x = x
        self.y = y
        self.rotation = rotation if rotation is not None else 0
        self.inverted = inverted if inverted is not None else False

    def move(self, dx: int, dy: int) -> None:
        pass

    def rotate(self) -> None:
        pass

    def flip(self) -> None:
        pass

    def get_pos(self) -> Tuple[int, int, Optional[int], Optional[bool]]:
        pass

    def __iter__(self) -> BoardElement:
        return self

    def __next__(self) -> Tuple[int, int]:
        raise StopIteration

    def check_for_intersection(self, other: BoardElement) -> bool:
        if other == self:
            return False
        for (x1, y1) in self:
            for (x2, y2) in other:
                if (x1, y1) == (x2, y2):
                    return True
        return False


class Block(BoardElement):
    def __init__(self, x: int, y: int, rotation: int, inverted: bool) -> None:
        super().__init__(x, y, rotation, inverted)
        self.piece = 0
        self.curr_x = self.x
        self.curr_y = self.y

    def __str__(self) -> str:
        return f'{self.x}{self.y}{self.rotation}{1 if self.inverted else 0}'

    def __iter__(self) -> Block:
        self.piece = 0
        self.curr_x = self.x
        self.curr_y = self.y

        if self.rotation == 0:
            self.dir_vec = (0, -1)
        elif self.rotation == 1:
            self.dir_vec = (1, 0)
        elif self.rotation == 2:
            self.dir_vec = (0, 1)
        else:
            self.dir_vec = (-1, 0)

        (self.curr_x, self.curr_y) = tuple(map(operator.sub, (self.x, self.y), self.dir_vec))

        return self

    def __next__(self) -> Tuple[int, int]:
        if self.piece >= 4:
            raise StopIteration
        if self.piece == 3:
            if not self.inverted:
                if self.dir_vec[0] == 0:
                    self.dir_vec = (-self.dir_vec[1], 0)
                else:
                    self.dir_vec = (0, self.dir_vec[0])
            else:
                if self.dir_vec[0] == 0:
                    self.dir_vec = (self.dir_vec[1], 0)
                else:
                    self.dir_vec = (0, -self.dir_vec[0])

        (self.curr_x, self.curr_y) = tuple(map(operator.add, (self.curr_x, self.curr_y), self.dir_vec))

        self.piece += 1
        return self.curr_x, self.curr_y

    def move(self, dx: int, dy: int) -> None:
        prev_pos = (self.x, self.y)
        self.x += dx
        self.y += dy
        if self.is_out_of_bonds():
            (self.x, self.y) = prev_pos

    def rotate(self) -> None:
        prev_rotation = self.rotation
        self.rotation = (self.rotation + 1) % 4
        if self.is_out_of_bonds():
            self.rotation = prev_rotation

    def flip(self) -> None:
        self.inverted = not self.inverted
        if self.is_out_of_bonds():
            self.inverted = not self.inverted

    def is_out_of_bonds(self) -> bool:
        for (x, y) in self:
            if x >= config.GRID_SIZE or x < 0 or y >= config.GRID_SIZE or y < 0:
                return True
        return False

    def get_pos(self) -> Tuple[int, int, int, bool]:
        return self.x, self.y, self.rotation, self.inverted


class Coin(BoardElement):
    def __init__(self, pos: Tuple[int, int]) -> None:
        super().__init__(pos[0], pos[1], 0, False)

    def move(self, dx: int, dy: int) -> None:
        prev_x, prev_y = self.x, self.y
        self.x += dx
        self.y += dy
        if self.x >= config.GRID_SIZE or self.x < 0 or self.y >= config.GRID_SIZE or self.y < 0:
            self.x, self.y = prev_x, prev_y

    def get_pos(self) -> Tuple[int, int]:
        return self.x, self.y

    def __str__(self) -> str:
        return f'{self.x}{self.y}'
