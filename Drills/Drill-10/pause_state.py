import game_framework
from pico2d import *

import main_state

__name__ = "PauseState"
image = None
def enter():
    global image
    image = load_image('pause.png')

def exit():
    pass
def update():
    pass
def draw():
    pass
def handle_events():
    pass
def pause():
    pass
def resume():
    pass
