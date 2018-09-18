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
    x2, y2 = Array_Coordinate[i+2:j+2:]
    return x1, y1, x2, y2

def Move(x, y):
    pass
while True:
    Get_Coord_from_Array(i, j)
    Move()
    pass
    
close_canvas()
