class Block:
    def __init__(self, start_x: int, start_y: int, start_rotation: int, inverted: bool):
        self.x = start_x
        self.y = start_y
        self.rotation = start_rotation
        self.inverted = inverted

    def __str__(self):
        return f'(x, y) = ({self.x},{self.y}) --- rot = {90 * self.rotation} --- inverted = {self.inverted}'
