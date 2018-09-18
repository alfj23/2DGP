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

    if(i == 8 & j == 10):
        x2, y2 = Array_Coordinate[i-10:j-10:]
    else:
        x2, y2 = Array_Coordinate[i + 2:j + 2:]
    return x1, y1, x2, y2
def Swap(a, b):
    tmp = a
    a = b
    b = tmp
def Move(x, y):
    x1, y1, x2, y2 = Get_Coord_from_Array(i, j)
    X_Gap = x2 - x1
    Y_Gap = y2 - y1
    Inclination = Y_Gap / X_Gap

    frame = 0
    if (x1 > x2):
        Swap(x1, x2)
    while x1 < x2:

    pass

i = 0
j = i + 2
while True:
    Get_Coord_from_Array(i, j)
    Move()
    i += 2
    j += 2
    pass
    
close_canvas()
