import os
import pygame


class Turtle(object):
    def __init__(self):
        super().__init__()
        self.image_path = 'sprites/turtle.png'
        self.image = pygame.image.load(os.path.join('sprites', 'turtle.png'))

        self.pos_x = 0
        self.pos_y = 0

        self.x_vel = 0
        self.y_vel = 0

    def position(self):
        return [self.pos_x, self.pos_y]
