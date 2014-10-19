import os
import random
import pygame
from flappyturtle.objects.obstacle import Obstacle
from flappyturtle.player.turtle import Turtle

__author__ = 'neil@everymundo.com'

OBSTACLE_MIN_TIME = 2
OBSTACLE_MAX_TIME = 5


class World():
    def __init__(self, width, height):
        super().__init__()
        self.turtle = None
        self.obstacles = []
        self.width = width
        self.height = height
        self.background = pygame.image.load(os.path.join('sprites', 'background.png'))
        scale_x = self.width / self.background.get_width()
        scale_y = self.height / self.background.get_height()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.background_pos = 0
        self.sand_image = pygame.image.load(os.path.join('sprites', 'background_sand.png'))
        self.sand_image = pygame.transform.scale(self.sand_image,
                                                 (self.width, int(self.sand_image.get_height() * scale_x)))
        self.sand_pos = 0
        self.velocity = 300
        self.next_obstacle = 0

    def add_player(self, position):
        self.turtle = Turtle(position)
        return self.turtle

    def add_obstacle(self, obstacle_type):
        coral_x = self.width
        coral_y = self.height
        if obstacle_type == 'coral':
            self.obstacles.append(Obstacle('sprites/coral_tall.png', coral_x, coral_y))

    def update(self, time):
        turtle_bounds = self.turtle.bounds()
        if turtle_bounds[1] <= 0:
            self.turtle.too_high(0)
        if turtle_bounds[3] >= self.height:
            self.turtle.too_low(self.height)

        self.sand_pos -= self.velocity * time
        if self.sand_pos <= -self.width:
            self.sand_pos += self.width

        self.background_pos -= self.velocity * time * 0.3
        if self.background_pos <= -self.width:
            self.background_pos += self.width

        self.next_obstacle -= time

        if self.next_obstacle <= 0:
            self.next_obstacle = random.randint(OBSTACLE_MIN_TIME, OBSTACLE_MAX_TIME)
            self.add_obstacle('coral')

        for obstacle in self.obstacles:
            obstacle.pos_x -= self.velocity * time
