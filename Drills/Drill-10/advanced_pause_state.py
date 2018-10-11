import game_framework
from pico2d import *

import main_state

__name__ = "AdvancedPauseState"
icon = None


class Pause:
    def __init__(self):
        self.image = load_image('pause.png')
        self.time = 0
        self.blinkering = True

    def update(self):
        self.time = (self.time + 1) % 2

    def draw(self):
        if self.time == 0:
            self.image.draw(400, 300)

def enter():
    global icon
    icon = Pause()

def exit():
    global icon
    del icon

def update():
    icon.update()
    delay(0.25)


def draw():
    clear_canvas()
    main_state.draw()
    icon.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def pause():
    pass


def resume():
    pass
