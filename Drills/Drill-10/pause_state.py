import game_framework
from pico2d import *

import main_state

__name__ = "PauseState"
image = None
pause_time = 0.0
def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del(image)

def update():

    pass
def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
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
    pass

def pause():
    pass
def resume():
    pass
