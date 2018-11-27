from pico2d import *
import main_state
import world_build_state
import json
import game_framework


'''
뭘 저장해야 하나??? 랭킹 이니까 시간이 일단 저장되어야 함.
'''
__name__ = 'ranking_state'

global time
def enter():
    global time
    time = main_state.boy.start_time
    pass


def exit():
   pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(world_build_state)
    pass


def update():
    pass


def draw():
    clear_canvas()
    pass