from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
character = load_image('animation_sheet.png')
Map = load_image('KPU_GROUND.png')


def Move_character(p1, p2, p3, p4):
    frame = 0
    # draw p1-p2
    for i in range(0, 50, 2):
        clear_canvas()
        Map.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        if (p1 < p2):  # See Right
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif (p1 > p2):  # See Left
            character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

    # draw p2-p3
    for i in range(0, 100, 2):
        clear_canvas()
        Map.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        if (p2 < p3):  # See Right
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif (p2 > p3):  # See Left
            character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
    # draw p3-p4
    for i in range(50, 100, 2):
        clear_canvas()
        Map.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p2[0] + (-4 * t ** 2 + 4 * t) * p3[0] + (2 * t ** 2 - t) * p4[0]
        y = (2 * t ** 2 - 3 * t + 1) * p2[1] + (-4 * t ** 2 + 4 * t) * p3[1] + (2 * t ** 2 - t) * p4[1]
    if (p3 < p4):  # See Right
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif (p3 > p4):  # See Left
        character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)


size = 10
Random_Coordinates = [(random.randint(200+25, 800-25), random.randint(100+50, 600-50)) for i in range(size)]
i = 1
while True:
   # Move_character((200,200),(400,400),(600,200),(700,400))
    Move_character(Random_Coordinates[0], Random_Coordinates[1], Random_Coordinates[2],Random_Coordinates[3])
    Move_character(Random_Coordinates[3], Random_Coordinates[4], Random_Coordinates[5], Random_Coordinates[6])
    Move_character(Random_Coordinates[6], Random_Coordinates[7], Random_Coordinates[8], Random_Coordinates[9])
    i = (i + 4) % size