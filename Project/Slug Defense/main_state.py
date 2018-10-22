from pico2d import *

#name ="MainState"


class Grass():
    def __init__(self):
        self.image = load_image('map1.png')

    def draw(self):
        self.image.draw(400, 300)


class Player():
    def __init__(self):
        self.x, self. y = 50, 90
        self.frame = 0
        self.image = load_image('.png')

    def update(self):
        self.frame = (self.frame +1) % 28
        self.x += 4

    def draw(self):
        self.image.clip_draw(self.frame * 10, 0, 50, 50, self.x, self.y)


open_canvas(1093,500)
#global Slug
global grass
grass = Grass()
#Slug = Player()


while True:
    clear_canvas()
    grass.draw()
    #Slug.update()
    #Slug.draw()

close_canvas()



def enter():
   pass


def exit():
   pass

def pause():
    pass


def resume():
    pass


def handle_events():
    pass


def update():
    pass


def draw():
    pass




