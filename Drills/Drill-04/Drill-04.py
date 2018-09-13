from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
frame = 0
direction = 0
while (1):
    if direction == 0:
        if(x < 800):
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 100, 100, 100, x, 90)  #left, bottom, width, height
            update_canvas()
            frame = (frame + 1) % 8
            x += 10
            delay(0.05)
            get_events()
            if(x >= 790):
                direction = 1
    if direction == 1:
        if(x > 0):
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 0, 100, 100, x, 90)  # left, bottom, width, height
            update_canvas()
            frame = (frame + 1) % 8
            x -= 10
            delay(0.05)
            get_events()
            if(x <= 1):
                direction = 0


close_canvas()
