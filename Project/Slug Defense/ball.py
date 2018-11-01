from pico2d import *
import game_world

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1): #파라미터를 넣을때 값을 넣으면 default 값임.
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self) # 범위를 벗어나면 자기 자신을 제거함 (게임월드 모듈 리무브 함수에서 메모리 반환까지 해줌.)
class Cannon:
    image = None

    def __init__(self, x=400, y=300, velocity = 1):
        self.x, self.y = x, y, velocity
        self.frame = 0
        if Cannon.image == None:
            self.image = load_image('cannon_ball.png')
        self.shot = False

    def shoot(self):
        self.x += 10
        self.frame = (self.frame + 1) % 4
        if self.x >= 799-10:
            self.shot = False
            self.x += 40
            self.frame = 0
        print(self.x)

    def draw(self):
        if self.shot:
            self.image.clip_draw(self.frame * 40, 0, 40, 30, self.x, self.y)
