import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import main_state

from boy import Boy
from zombie import Zombie


boy = None


name = "WorldBuildState"

menu = None

def enter():
    global menu
    menu = load_image('menu.png')
    hide_cursor()
    hide_lattice()

def exit():
    global menu
    del menu

def pause():
    pass

def resume():
    pass

def get_boy():
    return boy

def create_new_world():
    global boy, zombie
    boy = Boy()
    game_world.add_object(boy, 1)

    with open('zombie_data.json', 'r') as f:
        zombie_data_list = json.load(f)  # f라는 파일을 역직렬화 해서 리스트로

    for data in zombie_data_list:  # json 파일을 바꿈으로 내가 원하는 레벨을 설계할 수 있다.
        zombie = Zombie(data['name'], data['x'], data['y'], data['size'])
        game_world.add_object(zombie, 1)


def load_saved_world():
    global boy, zombie

    game_world.load() # 바깥에 저장된 데이터를 가져옴. 근데 보이가 누구냐?
    for o in game_world.all_objects():
        if isinstance(o, Boy): # isinstance(a,b) 어떤 객체(a)가 어떤 클래스(b)로부터 만들어졌는지 알려줄 수 있음.
            boy = o
            break  # 소년 객체는 하나 밖에 없기때문에 찾아서 저장하면 반복문에서 빠져나가줌.
    for o in game_world.all_objects(o, Zombie):
        if isinstance(o, Zombie):
            zombie = o
            break



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_n:
            create_new_world()
            game_framework.change_state(main_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_l:
            load_saved_world()
            game_framework.change_state(main_state)

def update():
    pass

def draw():
    clear_canvas()
    menu.draw(get_canvas_width()//2, get_canvas_height()//2)
    update_canvas()






