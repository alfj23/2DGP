from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')



x1,x2 = 0, 0
y1,y2 = 0, 0
def Get_Coord_from_Array(i, j):
    Array_Coordinate = [203, 535, 132, 243, 535, 470, 477, 203, 715, 136,
                        316, 225, 510, 92, 692, 518, 682, 336, 712, 349]
    x1, y1 = Array_Coordinate[i:j:]

    if(i == 18 & j == 19):
        x2, y2 = Array_Coordinate[(i-18):(j-20):]
    else:
        x2, y2 = Array_Coordinate[(i + 2):(j + 2):]

    return x1, y1, x2, y2
def Swap(a, b):
    tmp = a
    a = b
    b = tmp
def Move():
    x1, y1, x2, y2 = Get_Coord_from_Array(i, j)
    X_Gap = x2 - x1
    Y_Gap = y2 - y1
    Inclination = Y_Gap / X_Gap # 기울기

    frame = 0
    if (x1 > x2): # 현재 x 값이 다음 x 값 보다 클때
       # Swap(x1, x2)
        while x1 > x2: #방향 왼쪽
            clear_canvas_now()
            grass.draw(400, 30)
            character.clip_draw(frame * 0, 0, 100, 100, x1, y1)
            update_canvas()
            frame = (frame + 1) % 8
            x1 -= 3
            if(y1 < y2):
                y1 += 3 * Inclination
            else:
                y1 -= 3 * Inclination
            delay(0.01)
            get_events()

    else:
        while x1 < x2:
            clear_canvas_now()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
            update_canvas()
            frame = (frame + 1) % 8
            x1 += 3
            if (y1 < y2):
                y1 += 3 * Inclination
            else:
                y1 -= 3 * Inclination
            delay(0.01)
            get_events()
i = 0
j = i + 2
while True:
    Get_Coord_from_Array(i, j)
    Move()
    i += 2
    j += 2
    if(i == 18 & i == 20):
        i = 0
        j = i + 2
    
close_canvas()
