from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

Array_Coordinate = [203, 535, 132, 243, 535, 470, 477, 203, 715, 136, 316, 225, 510, 92, 692, 518, 682, 336, 712, 349]

def Move_1to2():
    x1, y1 = 203, 535
    x2, y2 = 132, 243
    X_Gap = x2 - x1
    Y_Gap = y2 - y1
    Inclination = Y_Gap / X_Gap # 기울기

    frame = 0
    while x1 > x2:
        clear_canvas_now()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 3
        y1 -= 3 * Inclination
        delay(0.033)
        get_events()

def Move_2to3():
    x1, y1 = 132, 243
    x2, y2 = 535, 470
    X_Gap = x2 - x1
    Y_Gap = y2 - y1
    Inclination = Y_Gap / X_Gap  # 기울기

    frame = 0
    while x1 < x2:
        clear_canvas_now()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 5
        y1 += 5 * Inclination
        delay(0.02)
        get_events()
def Move_3to4():
    x1, y1 = 535, 470
    x2, y2 = 477, 203
    X_Gap = x2 - x1
    Y_Gap = y2 - y1
    Inclination = Y_Gap / X_Gap  # 기울기

    frame = 0
    while x1 > x2:
        clear_canvas_now()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 3
        y1 -= 3 * Inclination
        delay(0.02)
        get_events()
def Move_4to5():
    x1, y1 = 477, 203
    x2, y2 = 715, 136
    X_Gap = x2 - x1
    Y_Gap = y2 - y1
    Inclination = Y_Gap / X_Gap  # 기울기

    frame = 0
    while x1 < x2:
        clear_canvas_now()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 3
        y1 += 3 * Inclination
        delay(0.02)
        get_events()
def Move_5to6():
    x1, y1 = 715, 136
    x2, y2 = 316, 225
    X_Gap = x2 - x1
    Y_Gap = y2 - y1
    Inclination = Y_Gap / X_Gap  # 기울기

    frame = 0
    while x1 > x2:
        clear_canvas_now()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 3
        y1 -= 3 * Inclination
        delay(0.02)
        get_events()
def Move_6to7():
    x1, y1 = 316, 225
    x2, y2 = 510, 92
    X_Gap = x2 - x1
    Y_Gap = y2 - y1
    Inclination = Y_Gap / X_Gap  # 기울기

    frame = 0
    while x1 < x2:
        clear_canvas_now()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 3
        y1 += 3 * Inclination
        delay(0.02)
        get_events()
def Move_7to8():
    x1, y1 = 510, 92
    x2, y2 = 692, 518
    X_Gap = x2 - x1
    Y_Gap = y2 - y1
    Inclination = Y_Gap / X_Gap  # 기울기

    frame = 0
    while x1 < x2:
        clear_canvas_now()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 3
        y1 += 3 * Inclination
        delay(0.02)
        get_events()
def Move_8to9():
    x1, y1 = 692, 518
    x2, y2 = 682, 336
    X_Gap = x2 - x1
    Y_Gap = y2 - y1
    Inclination = Y_Gap / X_Gap  # 기울기

    frame = 0
    while x1 > x2:
        clear_canvas_now()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 1
        y1 -= 1 * Inclination
        delay(0.07)
        get_events()
def Move_9to10():
    x1, y1 = 682, 336
    x2, y2 = 712, 349
    X_Gap = x2 - x1
    Y_Gap = y2 - y1
    Inclination = Y_Gap / X_Gap  # 기울기

    frame = 0
    while x1 < x2:
        clear_canvas_now()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 2
        y1 -= 3 * Inclination
        delay(0.1)
        get_events()
def Move_10to1():
    x1, y1 = 712, 349
    x2, y2 = 203, 535
    X_Gap = x2 - x1
    Y_Gap = y2 - y1
    Inclination = Y_Gap / X_Gap  # 기울기

    frame = 0
    while x1 > x2:
        clear_canvas_now()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 5
        y1 -= 5 * Inclination
        delay(0.04)
        get_events()
while True:
    Move_1to2()
    Move_2to3()
    Move_3to4()
    Move_4to5()
    Move_5to6()
    Move_6to7()
    Move_7to8()
    Move_8to9()
    Move_9to10()
    Move_10to1()
    
close_canvas()
