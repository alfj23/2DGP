from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

Character = load_image('animation_sheet.png')
Map = load_image('KPU_GROUND.png')

open_canvas(KPU_WIDTH, KPU_HEIGHT)

def Move(p1, p2):
    pass


Random_Coordinates = [(random.randint(0+25, 1280-25), random.randin(-350, 350)) for i in range(20)]
i = 1
while True:
    Move(Random_Coordinates[n-1], Random_Coordinates[n])
    n = (n + 1) & 20

close_canvas()