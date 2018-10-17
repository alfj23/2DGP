from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(800//2, 30)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 70
        self.frame = random.randint(0, 7)
        self.image = load_image('SlugGunner.png')

    def update(self):
        self.frame = (self.frame + 1) % 28
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 85, 420, 85, 85, self.x, self.y)

def handle_events():
    pass

# initialization code


open_canvas()

slug = Boy()
grass = Grass()

# game main loop code

while True:
    handle_events()


    clear_canvas()
    slug.update()
    grass.draw()
    slug.draw()
    update_canvas()

    delay(0.08)


# finalization code

close_canvas()
