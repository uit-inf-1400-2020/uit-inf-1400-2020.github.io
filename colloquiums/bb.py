import pygame as pg
from pygame import Vector2
from random import randint
pg.init()


size = (width, height) = 800, 600

black = (0,0,0)
blue = (0,0,200)


class Ball():
    def __init__(self):
        self.pos = Vector2(100, 100)
        self.r = 100
        self.vel = Vector2(randint(-5, 5), randint(-5, 5))
        self.acc = 0.5
        self.color = (randint(0,255), randint(0,255), randint(0,255))
        self.img = pg.image.load('testimg.jpg')
        self.img = pg.transform.scale(self.img, (self.r, self.r))

    def update(self):
        self.vel.y += self.acc
        self.pos += self.vel
        self.bounce_off_walls()
        self.movement()

    def bounce_off_walls(self):
        if (self.pos.x + self.vel.x < self.r+5) or (self.pos.x + self.r + 5> width):
            self.vel.x *= -0.9
        
        if (self.pos.y + self.vel.y < self.r+5) or (self.pos.y + self.r + 5> height):
            self.vel.y *= -0.9

    def movement(self):
        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.pos.x += 10
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.pos.x -= 10

    def draw(self, surface):
        surface.blit(self.img, self.pos)
        # pg.draw.circle(surface, self.color, self.pos, self.r)


class Game():
    def __init__(self):
        self.clock = pg.time.Clock()
        self.balls = []
        for _ in range(10):
            self.balls.append(Ball())

        self.screen = pg.display.set_mode(size, 0, 32)
        pg.display.set_caption('bouncing balls')
        self.background = pg.image.load('testimg.jpg')
        
    def game_loop(self):
        done = False
        while not done:
            for event in pg.event.get():
                if (event.type == pg.QUIT or 
                (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                    done = True


            self.screen.fill(black)
            self.screen.blit(self.background, (0,0))
            self.clock.tick(30)
            for ball in self.balls:
                ball.update()
                ball.draw(self.screen)

            pg.display.update()


if __name__ == "__main__":
    bb = Game()
    bb.game_loop()