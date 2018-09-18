from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

Array_Coordinate = [203, 535, 132, 243, 535, 470, 477, 203, 715, 136, 316, 225, 510, 92, 692, 518, 682, 336, 712, 349]

def Move_1():
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
        delay(0.01)
        get_events()

while True:
    pass
    
close_canvas()
