import operator
import config


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
        return f'(x, y) = ({self.x},{self.y}) --- rot = {90 * self.rotation} --- inverted = {self.inverted}'

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
