from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024



open_canvas(KPU_WIDTH, KPU_HEIGHT)
character = load_image('animation_sheet.png')
Map = load_image('KPU_GROUND.png')

global frame

def Move(p1, p2):
    frame = 0
    for i in range(0, 100 + 1, 5):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]

    clear_canvas()
    Map.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if(p1[0] < p2[0]): # See Right
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    elif(p1[0] > p2[0]): # See Left
         character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) & 8

    delay(0.02)

Random_Coordinates = [(random.randint(0+25, KPU_WIDTH-25), random.randint(0 + 50, KPU_HEIGHT - 50)) for n in range(20)]
n = 1
frame = 0

while True:

    Move(Random_Coordinates[n-1], Random_Coordinates[n])
    n = (n + 1) & 20

close_canvas()