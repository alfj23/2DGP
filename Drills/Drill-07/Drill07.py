from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
character = load_image('animation_sheet.png')
Map = load_image('KPU_GROUND.png')


def Move_character(p1, p2):
    frame = 0
    for i in range(0, 100 + 1, 20):
        clear_canvas()
        Map.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]


        if (p1 < p2):  # See Right
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif (p1 > p2):  # See Left
            character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

size = 20
Random_Coordinates = [(random.randint(0+25, 800-25), random.randint(0+50, 600-50)) for i in range(size)]
i = 1
while True:
    Move_character(Random_Coordinates[i-1], Random_Coordinates[i])
    i = (i + 1) % size