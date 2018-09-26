from pico2d import *


def handle_events():
    global running
    global dir
    global Current_direction
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:#우측화살표 키
                dir += 1
            elif event.key == SDLK_LEFT:#좌측화살표 키
                dir -= 1
            elif event.key == SDLK_ESCAPE:#ESC 키
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -=1
                #Current_direction = 1
            elif event.key == SDLK_LEFT:
                dir +=1
                #Current_direction = 0
                
    


open_canvas()
grass = load_image('grass.png')
character = load_image('tankmoving.png')
running = True
x = 800 // 2
frame = 0
dir = 0
hide_lattice()
while running:
    clear_canvas()
    grass.draw(400, 30)
    if(dir <= 0):
        character.clip_draw(frame * 140 , 0, 140, 100, x, 90)
    elif dir >= 0 :
        character.clip_draw(frame * 140, 0, 140, 100, x, 90)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 4
    if x < (800 - 70) and x > (0 + 70):
        x += dir*5
    elif(x <= 0 + 70):
        x = 800 - 70
    elif(x >= 800 - 70):
        x = 0 + 70
    delay(0.05)

close_canvas()

