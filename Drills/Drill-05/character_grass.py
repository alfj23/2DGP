from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


x = 399
y = 90
radian = math.pi    
while(1):
    
    while(x < 750):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 6
        delay(0.01)

    while(y < 550):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(750, y)
        y= y+6
        delay(0.01)

    while(x >= 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 550)
        x = x-6
        delay(0.01)

    while(y >=90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(50, y)
        y = y-6
        delay(0.01)
        
    while(x < 399):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 6
        delay(0.01)

    x += -40 * math.cos(radian/180)
    y += 40 * math.sin(radian/180)
   
close_canvas()
