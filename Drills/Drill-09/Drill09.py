from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0+25, 500), 85
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.size = random.randint(0, 1)
        self.speed = random.randint(5, 20)
        if self.size == 0:
            self.image = load_image('ball41x41.png')
        else:
            self.image = load_image('ball21x21.png')

    def fall(self):
        if self.size == 0:
            if self.y <= 50 + (41/2):
                self.y = 50+(41/2)
            else:
                self.y -= self.speed
        elif self.size == 1:
            if self.y <= 50 + (21/2):
                self.y = 50 + (21/2)
            else:
                self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():

    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code


open_canvas()

team = [Boy() for i in range(11)]
grass = Grass()
balls = [Ball() for i in range(20)]
running = True

# game main loop code

while running:
    handle_events()

    for boy in team:
        boy.update()
    for ball in balls:
        ball.fall()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

    delay(0.05)


# finalization code

close_canvas()
