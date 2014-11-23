import os
import unittest
import pygame
import sys
from flappyturtle.display.window import Window
from flappyturtle.objects.collision import pixel_perfect_check_collision
from flappyturtle.objects.obstacle import Obstacle
from flappyturtle.player.turtle import Turtle
from flappyturtle.world import World

__author__ = 'Neil'


class CollisionTestCase(unittest.TestCase):
    if not os.getcwd().endswith('flappyturtle'):
        os.chdir('../../flappyturtle')

    def test_non_collision_rect(self):
        obstacle = Obstacle('sprites/coral_tall.png', 0, 0, 0)
        turtle = Turtle([800, 600])
        if pixel_perfect_check_collision(obstacle, turtle):
            self.fail('Should not collide when distance is too far')

    def test_non_collision_pixel(self):
        obstacle = Obstacle('sprites/coral_tall.png', 300, 300, 0)
        obstacle2 = Obstacle('sprites/coral_tall.png', 435, 400, 0)

        if pixel_perfect_check_collision(obstacle, obstacle2):
            self.fail()


    def test_rect_collion(self):
        raise NotImplementedError

    def test_pixel_collision(self):
        obstacle = Obstacle('sprites/coral_tall.png', 300, 300, 0)
        obstacle2 = Obstacle('sprites/coral_tall.png', 400, 400, 0)

        if not pixel_perfect_check_collision(obstacle, obstacle2):
            self.fail()

    def test_pixel_collision_player(self):
        obstacle = Obstacle('sprites/coral_tall.png', 300, 300, 0)
        turtle = Turtle([300, 300])

        if not pixel_perfect_check_collision(obstacle, turtle):
            self.fail()

        pygame.init()
        window = Window(800, 600)
        DISPLAY_SURFACE = pygame.display.set_mode(window.dimensions)
        pygame.display.set_caption("Flappy Turtle")

        FPS = 60
        FpsClock = pygame.time.Clock()

        while True:
            time = FpsClock.get_time()
            # Check the keyboard & mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            DISPLAY_SURFACE.fill((55, 180, 200))
            DISPLAY_SURFACE.blit(obstacle.image, (obstacle.pos_x, obstacle.pos_y))
            DISPLAY_SURFACE.blit(turtle.image, turtle.position())
            pygame.display.update()
            FpsClock.tick(FPS)
