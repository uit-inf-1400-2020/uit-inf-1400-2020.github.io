#!/usr/bin/env python3

# This version adds a new type of moving objects: Circle.
# The interface of the Ball and Circle objects are the same, while the implementation differs.
# This allows us to call move() and draw() on any ball or circle object, ignoring which type of object is
# (see the objs list and the move and draw loops towards the end of the file).
# We will expand on this concept later, introducing Polymorphy.

import pygame
import random

SCREEN_X = 640
SCREEN_Y = 480
BG_FNAME = "Chapter03/sushiplate.jpg"
MOUSE_FNAME = "Chapter03/fugu.png"
BALL_FNAME = "ball.png"

pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
background = pygame.image.load(BG_FNAME)
background = background.convert()

mouse_img  = pygame.image.load(MOUSE_FNAME).convert_alpha()
mouse_size_x = mouse_img.get_width()
mouse_size_y = mouse_img.get_height()

ball_img = pygame.image.load(BALL_FNAME).convert_alpha()


class Ball:
    def __init__(self):
        self.x = 42
        self.y = 200
        self.speed = [50 + 60 * random.random(),
                      50 + 60 * random.random()]
        self.img = ball_img
        self.size = self.img.get_height()  # litt juks.

    def move(self, time_passed):
        self.x += self.speed[0] * time_passed
        self.y += self.speed[1] * time_passed

        if self.x < 0:
            self.speed[0] = abs(self.speed[0])
        if self.y < 0:
            self.speed[1] = abs(self.speed[1])

        if self.x > SCREEN_X - self.size:
            self.speed[0] = -abs(self.speed[0])
        if self.y > SCREEN_Y - self.size:
            self.speed[1] = -abs(self.speed[1])

    def draw(self):
        screen.blit(self.img, (self.x, self.y))


class Circle:
    def __init__(self):
        self.x = 42
        self.y = 200
        self.speed = [50 + 60 * random.random(),
                      50 + 60 * random.random()]
        self.col = (255, 255, 0)
        self.size = 30

    def move(self, time_passed):
        self.x += self.speed[0] * time_passed
        self.y += self.speed[1] * time_passed

        if self.x < 0:
            self.speed[0] = abs(self.speed[0])
        if self.y < 0:
            self.speed[1] = abs(self.speed[1])

        if self.x > SCREEN_X - self.size:
            self.speed[0] = -abs(self.speed[0])
        if self.y > SCREEN_Y - self.size:
            self.speed[1] = -abs(self.speed[1])

    def draw(self):
        pygame.draw.circle(screen, self.col, (round(self.x), round(self.y)),
                           round(self.size / 2))


ball1 = Ball()
objs = [
    Ball(),
    Ball(),
    Circle(),
    Circle(),
    Ball(),
]


clock = pygame.time.Clock()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    time_passed = clock.tick(30) / 1000.0

    # t = pygame.mouse.get_pos()
    # x = t[0]
    # y = t[1]
    x, y = pygame.mouse.get_pos()

    mx = x - mouse_size_x / 2
    my = y - mouse_size_y / 2

    screen.blit(background, (0, 0))
    screen.blit(mouse_img, (mx, my))

    ball1.move(time_passed)
    ball1.draw()

    # NOTE: we don't have to worry about whether an object is a circle or a ball as they have the same interface.
    for obj in objs:
        obj.move(time_passed)

    for obj in objs:
        obj.draw()

    pygame.display.update()
