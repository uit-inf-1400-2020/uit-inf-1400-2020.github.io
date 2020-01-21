#!/usr/bin/env python3

# This is a very basic PyGame program importing and initializing the pygame library.
# It also opens a PyGame window, but doesn't draw anything there yet.

import pygame

SCREEN_X = 640
SCREEN_Y = 480

pygame.init()
pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit()
