from pico2d import *
import math
open_canvas()


grass = load_image('grass.png')
character = load_image('character.png')


x = 400
y = 91
angle = 0

direction = 1
shape = 1
change_shape = 0

while(1):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

    
    if(shape == 1):
        if direction == 1:
            x= x+8
            if change_shape == 1 and x > 400:
                shape = 2
                
        if direction == 2:
            y = y+8
            
        if direction == 3:
            x = x-8
            
        if direction == 4:
            y = y-8


        
        if x > 750:
            direction = 2
            
        if y > 550:
            direction = 3
            
        if x < 50:
            direction = 4
            
        if y < 91:
            direction = 1
            change_shape = 1
            

    if(shape == 2):
        direction = 0
        if(direction == 0 and angle < 360):
            x = -210 * math.sin(3.141592 / 180 * angle) + 400
            y = -210 * math.cos(3.141592 / 180 * angle) + 300
            angle = angle + 1

        if angle == 360:
            x = 400
            y = 91
            angle = 0
            shape = 1
            change_shape = 0
            direction = 1
           
                            
   
   
    delay(0.01)
        
        
   
close_canvas()
