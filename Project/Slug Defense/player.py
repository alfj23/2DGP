from pico2d import *
from ball import Cannon

import game_world

# Player Slug Drive Speed

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Player Slug Action Speed

TIME_PER_ACTION = 0.5  # 액션 당 시간
ACTION_PER_TIME = 1.0  # 액션 마다 달라서 따로 빼놓음?
FRAMES_PER_ACTION = 8


# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, X= range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_x): X
}

# Player Slug States

class IdleState:

    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += 1
        elif event == LEFT_DOWN:
            player.velocity -= 1
        elif event == RIGHT_UP:
            player.velocity -= 1
        elif event == LEFT_UP:
            player.velocity += 1
        pass

    @staticmethod
    def exit(player, event):
        if event == X:
           # player.fire_cannon()
            print('fire!!!')
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 3
        pass

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 80, 160, 80 - 3, 80, player.x, player.y)
        pass


class DriveState:

    @staticmethod
    def enter(player, event):
       pass

    @staticmethod
    def exit(player, event): # 왜 나가는지 event를 통해서 알려줄 수 있음.
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        pass


next_state_table = {
    IdleState: {RIGHT_UP: DriveState, LEFT_UP: DriveState,
                RIGHT_DOWN: DriveState, LEFT_DOWN: DriveState,
               },
    DriveState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
                LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               }
}


class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('finaltest.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def fire_ball(self):
        ball = Cannon(self.x, self.y, self.dir*3)
        game_world.add_object(ball, 1)




    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

class Player:
    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('finaltest.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def fire_cannon(self):
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)
        pass

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        pass

    def draw(self):
        self.cur_state.draw(self)
        pass

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass