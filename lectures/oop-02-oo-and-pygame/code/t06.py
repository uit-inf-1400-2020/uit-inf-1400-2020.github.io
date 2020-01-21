#!/usr/bin/env python3

# This is an early example of using inheritance to simplify the code from t05.py.
# We rushed the example as we ran out of time, so we haven't fully explained this yet (we will continue in the next lecture).
#
# The main focus here was that inheritance lets us move common code to a common parent class (MovingObject) and that
# the child classes (Ball and Circle) only need to specifiy how they differ from the parent class.
# We have not explained the rest yet, so don't worry about the details until we cover it in the next lecture.


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


class MovingObject:
    def __init__(self):
        self.x = 42
        self.y = 200
        self.speed = [50 + 60 * random.random(),
                      50 + 60 * random.random()]
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
        print("Fyyy")


class Ball(MovingObject):
    def __init__(self):
        MovingObject.__init__(self)
        self.img = ball_img
        self.size = self.img.get_height()

    def draw(self):
        screen.blit(self.img, (self.x, self.y))


class Circle(MovingObject):
    def __init__(self):
        MovingObject.__init__(self)
        self.col = (255, 255, 0)

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

    for obj in objs:
        obj.move(time_passed)

    for obj in objs:
        obj.draw()

    pygame.display.update()
