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
        delay(0.02)
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
        x1 += 3
        y1 += 3 * Inclination
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
    pass
def Move_5to6():
    pass
def Move_6to7():
    pass
def Move_7to8():
    pass
def Move_8to9():
    pass
def Move_9to10():
    pass
def Move_10to1():
    pass
while True:
   # Move_1to2()
   # Move_2to3()
    Move_3to4()
    Move_4to5()
    Move_5to6()
    Move_6to7()
    Move_7to8()
    Move_8to9()
    Move_9to10()
    Move_10to1()
    
close_canvas()
