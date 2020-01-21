#!/usr/bin/env python3

# This one expands on t01.py by loading a background image that we draw (using screen.blit).
# Screen.blit only renders to a background buffer. To see that buffer, we need to use pygame.display.update().
# See PyGame introductoin and documentation for more information.

import pygame

SCREEN_X = 640
SCREEN_Y = 480
BG_FNAME = "Chapter03/sushiplate.jpg"

pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
background = pygame.image.load(BG_FNAME)

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit()

    screen.blit(background, (0, 0))
    pygame.display.update()
