import os
import pygame


class Turtle(object):
    swim_speed = 175

    def __init__(self, position):
        super().__init__()
        self.image_path = 'sprites/turtle.png'
        self.image = pygame.image.load(os.path.join('sprites', 'turtle.png'))
        self.scale = 0.7
        self.image = pygame.transform.scale(self.image,
            (int(self.image.get_width() * self.scale), int(self.image.get_height() * self.scale)))

        self.pos_x = position[0] - (self.image.get_width() / 2)
        self.pos_y = position[1] - (self.image.get_height() / 2)

        self.vel_x = 0
        self.vel_y = 0

    def position(self):
        return [self.pos_x, self.pos_y]

    def bounds(self):
        return [self.pos_x, self.pos_y, self.pos_x + self.image.get_width(), self.pos_y + self.image.get_height()]

    def update(self, time):
        self.pos_y += self.vel_y * time

    def too_high(self, new_pos):  # Hehehe...
        self.vel_y = 0
        self.pos_y = new_pos

    def too_low(self, new_pos):
        self.vel_y = 0
        self.pos_y = new_pos - self.image.get_height()

    def swim(self, up):
        if up:
            self.vel_y = -Turtle.swim_speed
        else:
            self.vel_y = Turtle.swim_speed