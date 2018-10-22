from pico2d import *
import random

global running

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(800//2, 30)


class Player:
    def __init__(self):
        self.x, self.y = 0, 70
        self.frame = 0
        self.image = load_image('TEST.png')
        self.dir = 0
        self.cannon = 0
        self.cannonframe = 0

    def moving(self):
        if self.dir == 1 or self.dir == -1:
            self.frame = (self.frame + 1) % 18
            self.x += self.dir * 7
        elif self.dir == 0:
            self.frame = (self.frame + 1) % 3
            self.x = self.x - 0
        elif self.cannon == 1:
            self.cannonframe = (self.cannonframe + 1) % 21

    def draw(self):
        if self.dir == 0:
            self.image.clip_draw(self.frame * 80, 320, 80-3, 80, self.x, self.y)
        elif self.dir == 1 or self.dir == -1:
            self.image.clip_draw(self.frame * 80, 240, 80-3, 80, self.x, self.y)
        if self.cannon == 1:
            if self.cannonframe <= 5:
                self.image.clip_draw(self.cannonframe * 140, 160, 140, 80, self.x+25, self.y)
            elif 5 < self.cannonframe <= 13:
                self.image.clip_draw(self.cannonframe * 140, 80, 140, 80, self.x+25, self.y)
            elif self.cannonframe > 13:
                self.image.clip_draw(self.cannonframe * 80, 0, 80, 80, self.x, self.y)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:  # 우측화살표 키
                slug.dir = 1
            elif event.key == SDLK_LEFT:  # 좌측화살표 키
                slug.dir = -1
            elif event.key == SDLK_ESCAPE:  # ESC 키
                running = False
            elif event.key == SDLK_x: # x키 공격
                slug.cannon = 1
                slug.dir = -2

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                slug.dir = 0
            elif event.key == SDLK_LEFT:
                slug.dir = 0
            elif event.key == SDLK_x:
                slug.cannon = 0
                slug.dir = 0

# initialization code

running = True
open_canvas()
slug = Player()
grass = Grass()

# game main loop code

while running:
    handle_events()

    clear_canvas()
    get_events()
    slug.moving()
    grass.draw()
    slug.draw()
    update_canvas()

    delay(0.04)


# finalization code

close_canvas()
