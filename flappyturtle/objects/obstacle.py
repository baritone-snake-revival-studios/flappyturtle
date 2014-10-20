import pygame
import sys
from flappyturtle.objects.collision import pixel_perfect_check_collision
from flappyturtle.player.turtle import Turtle

__author__ = 'neil@everymundo.com'


class Obstacle(object):
    def __init__(self, image_path, x, y, initial_velocity):
        super().__init__()
        self.image = pygame.image.load(image_path)

        self.pos_x = x
        self.pos_y = y - self.image.get_height()
        self.velocity = initial_velocity
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.scored = False

    def update(self, time):
        speed = self.velocity * time
        self.move_position(-speed, 0)

    def move_position(self, offset_x, offset_y):
        self.rect.move_ip(offset_x, offset_y)
        self.pos_x += offset_x
        self.pos_y += offset_y

    def check_collision(self, collider):
        # Do basic rectangular collision first, cheaper on the CPU
        if self.rect.colliderect(collider.rect):
            print('rectangle')
            # If the rectangles collide, test per-pixel
            if pixel_perfect_check_collision(self, collider):
                pygame.quit()
                sys.exit()

        # The player gains a point if they pass us
        if isinstance(collider, Turtle):
            if collider.rect.left > self.rect.right:
                if not self.scored:
                    self.scored = True
                    return True
                return False


