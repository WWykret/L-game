import operator
import config
from typing import Tuple


class Block:
    def __init__(self, start_x: int, start_y: int, start_rotation: int, inverted: bool):
        self.x = start_x
        self.y = start_y
        self.rotation = start_rotation
        self.inverted = inverted
        self.piece = 0
        self.curr_x = self.x
        self.curr_y = self.y

    def __str__(self):
        return f'{self.x}{self.y}{self.rotation}{1 if self.inverted else 0}'

    def __iter__(self):
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

    def __next__(self):
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

    def move(self, dx: int, dy: int):
        prev_pos = (self.x, self.y)
        self.x += dx
        self.y += dy
        if self.is_out_of_bonds():
            (self.x, self.y) = prev_pos

    def rotate(self):
        prev_rotation = self.rotation
        self.rotation = (self.rotation + 1) % 4
        if self.is_out_of_bonds():
            self.rotation = prev_rotation

    def flip(self):
        self.inverted = not self.inverted
        if self.is_out_of_bonds():
            self.inverted = not self.inverted

    def is_out_of_bonds(self) -> bool:
        for (x, y) in self:
            if x >= config.GRID_SIZE or x < 0 or y >= config.GRID_SIZE or y < 0:
                return True
        return False


class Coin:
    def __init__(self, pos: Tuple[int, int]) -> None:
        self.x = pos[0]
        self.y = pos[1]

    def move(self, dx: int, dy: int) -> None:
        prev_x, prev_y = self.x, self.y
        self.x += dx
        self.y += dy
        if self.x >= config.GRID_SIZE or self.x < 0 or self.y >= config.GRID_SIZE or self.y < 0:
            self.x, self.y = prev_x, prev_y

    def get_pos(self) -> Tuple[int, int]:
        return self.x, self.y

    def rotate(self):
        pass

    def flip(self):
        pass

    def __str__(self):
        return f'{self.x}{self.y}'
