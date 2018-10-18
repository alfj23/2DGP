from pico2d import *
import random

global running
global dir
global Current_direction

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(800//2, 30)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 70
        self.frame = random.randint(0, 7)
        self.image = load_image('Idle+moving.png')

    def moving(self):
        self.frame = (self.frame + 1) % 3

    def idle(self):
        self.frame = (self.frame + 1) % 3

    def draw(self):
        self.image.clip_draw(self.frame * 80, 80, 80-3, 80, self.x, self.y)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:  # 우측화살표 키
                dir = 1
                slug.x += 15 * dir
            elif event.key == SDLK_LEFT:  # 좌측화살표 키
                dir = -1
                slug.x += 15 * dir
            elif event.key == SDLK_ESCAPE:  # ESC 키
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir = 0
                slug.image.clip_draw(slug.frame * 80, 80, 80, 80, slug.x, slug.y)
                #Current_direction = 1
            elif event.key == SDLK_LEFT:
                dir = 0
                slug.image.clip_draw(slug.frame * 80, 80, 80, 80, slug.x, slug.y)
                #Current_direction = 0

# initialization code

running = True
open_canvas()
dir = 0
slug = Boy()
grass = Grass()

# game main loop code

while True:
    handle_events()


    clear_canvas()
    get_events()
    slug.moving()
    grass.draw()
    slug.draw()
    update_canvas()

    delay(0.02)


# finalization code

close_canvas()
