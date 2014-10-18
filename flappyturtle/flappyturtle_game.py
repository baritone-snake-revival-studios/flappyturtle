import pygame
import re
import os
from pygame.locals import *
import sys
import random

from flappyturtle.window import Window

__author__ = 'neil@everymundo.com'


def run_game():
    pygame.init()
    window = Window(800, 600)
    DISPLAY_SURFACE = pygame.display.set_mode(window.dimensions)
    pygame.display.set_caption("Flappy Turtle")

    FPS = 60
    FpsClock = pygame.time.Clock()

    while True:
    # Check the keyboard & mouse
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FpsClock.tick(FPS)


if __name__ == '__main__':
    run_game()