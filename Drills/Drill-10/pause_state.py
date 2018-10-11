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
    global pause_time
    if pause_time % 2 == 1:
        del(image)
    pause_time += 0.01
    pass
def draw():
    
    pass
def handle_events():
    pass
def pause():
    pass
def resume():
    pass
