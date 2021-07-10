import pygame
import config


class Window:
    def __init__(self):
        self.width = config.GRID_SIZE * (config.RECT_SIZE + config.SPACING) - config.SPACING
        self.height = config.GRID_SIZE * (config.RECT_SIZE + config.SPACING) - config.SPACING

        self.screen = pygame.display.set_mode(size=(self.width, self.height))

    def update(self):
        self.draw_grid()
        pygame.display.flip()

    def draw_grid(self):
        self.screen.fill(color=config.BLACK)
        for y in range(config.GRID_SIZE):
            for x in range(config.GRID_SIZE):
                rect_to_draw = (x * config.RECT_SIZE + x * config.SPACING, y * config.RECT_SIZE + y * config.SPACING, config.RECT_SIZE, config.RECT_SIZE)
                pygame.draw.rect(self.screen, config.WHITE, rect_to_draw)
