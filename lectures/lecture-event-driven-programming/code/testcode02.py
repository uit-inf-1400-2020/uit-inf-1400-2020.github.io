#!/usr/bin/env python3

"""Base code before using dispatcher.

This is similar in structure to the source code from the PyGame lecture, but without using images for graphics.
"""

import pygame
import time
import math
from pygame.locals import MOUSEMOTION, QUIT, USEREVENT
import random
from collections import defaultdict

pygame.init()

SCREEN_RES_X = 640
SCREEN_RES_Y = 480
screen = pygame.display.set_mode((SCREEN_RES_X, SCREEN_RES_Y), 0, 32)


# ------------------------------------------------------------
#
# Some objects to display
#
# ------------------------------------------------------------

class Ball:
    BASE_BALL_SPEED = 120  # hvor mange pixels per sekund

    def __init__(self):
        self.x = random.random() * SCREEN_RES_X
        self.y = random.random() * SCREEN_RES_Y
        self.dir_x = 1
        self.dir_y = 1
        self.speed = self.BASE_BALL_SPEED
        self.col = (255, 255, 0)
        self.size = 10

    def move(self, time_passed_seconds):
        dist = time_passed_seconds * self.speed

        self.x = self.x + dist * self.dir_x
        self.y = self.y + dist * self.dir_y

        if self.x < 0:
            self.dir_x = 1
        if self.y < 0:
            self.dir_y = 1
        if self.x > screen.get_width():
            self.dir_x = -1
        if self.y > screen.get_height():
            self.dir_y = -1

    def draw(self):
        pygame.draw.circle(screen, self.col, (round(self.x), round(self.y)), round(self.size / 2))


class SuperBall(Ball):
    def __init__(self):
        Ball.__init__(self)
        self.speed = 50 + random.random() * self.BASE_BALL_SPEED
        self.col = (255, 0, 0)

    def change_speed(self, new_speed):
        self.speed = new_speed
        self.speed = min(50, self.speed)
        self.speed = max(500, self.speed)

    def move(self, time_passed_seconds):
        self.change_speed(math.sin(time.time()) * 500)
        super().move(time_passed_seconds)


class Cursor:
    def __init__(self):
        self.col = (255, 255, 255)
        self.x = 0
        self.y = 0
        self.cursor_size = 15

    def move(self, _):
        #self.x, self.y = pygame.mouse.get_pos()
        pass

    def handler(self, event):
        self.x, self.y = event.pos

    def draw(self):
        x, y = round(self.x), round(self.y)
        cs = self.cursor_size
        pygame.draw.line(screen, self.col, (x - cs, y - cs), (x + cs, y + cs), 2)
        pygame.draw.line(screen, self.col, (x - cs, y + cs), (x + cs, y - cs), 2)


def mouse_handler(event):
    print("Mouse move:", event.pos, event.rel, event)


def my_handler(event):
    print(f"My event at {time.time()}")
    v = random.randrange(0, 30)
    if v > 20:
        print("---- tester post")
        e1 = pygame.event.Event(MY_EVENT, attr1='attr1')
        pygame.event.post(e1)
    #if v > 23:
    #    print("---- ugh")
    #    e1 = pygame.event.Event(QUIT)
    #    pygame.event.post(e1)


def simple_handler(event):
    print("simples")


class Foo:
    def handler(self, event):
        print("this is the foo handler", event)

def quit_handler(event):
    global finished
    finished = True

class QuitHandler:
    def __init__(self):
        self.finished = False

    def handler(self, event):
        self.finished = True
    

class Dispatcher:
    def __init__(self):
        self.__handlers = defaultdict(list)

    def register_handler(self, etype, handler):
        self.__handlers[etype].append(handler)

    def dispatch(self, event):
        if event.type in self.__handlers:
            for ehandler in self.__handlers[event.type]:
                ehandler(event)
        else:
            print("Du glemte å registrere en handler for", event.type, pygame.event.event_name(event.type))


MY_EVENT = USEREVENT + 1
pygame.time.set_timer(MY_EVENT, 2000)

# ------------------------------------------------------------
#
# Main loop
#
# ------------------------------------------------------------

clock = pygame.time.Clock()

cursor = Cursor()

objects = [
    Ball(),
    Ball(),
    SuperBall(),
    cursor,
]

foo = Foo()


dispatcher = Dispatcher()
#dispatcher.register_handler(MOUSEMOTION, mouse_handler)
dispatcher.register_handler(MOUSEMOTION, cursor.handler)
dispatcher.register_handler(MY_EVENT, my_handler)
dispatcher.register_handler(MY_EVENT, simple_handler)
dispatcher.register_handler(MY_EVENT, foo.handler)
#dispatcher.register_handler(QUIT, quit_handler)
quit = QuitHandler()
dispatcher.register_handler(QUIT, quit.handler)


while not quit.finished:
    for event in pygame.event.get():
        dispatcher.dispatch(event)

    time_passed = clock.tick(1000)
    time_passed_seconds = time_passed / 1000.0

    for obj in objects:
        obj.move(time_passed_seconds)

    screen.fill((0, 0, 0))

    for obj in objects:
        obj.draw()

    pygame.display.update()

pygame.quit()
