from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global Char_x1, Char_y1 , Char_x2, Char_y2

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            Char_x2, Char_y2 = event.x - 25, KPU_HEIGHT - 1 - event.y + 25


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
Char_x1, Char_y1 = KPU_WIDTH // 3, KPU_HEIGHT // 3
Char_x2, Char_y2 = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()
x_change = (Char_x1 - Char_x2)
y_change = (Char_y1 - Char_y2)
m = y_change / x_change
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_arrow.draw(x, y)

    if Char_x1 < Char_x2:  # 우측을 바라봄.
        character.clip_draw(frame * 100, 100 * 1, 100, 100, Char_x1, Char_y1)
        Char_x1 += (Char_x2 - Char_x1) / 10
        Char_y1 += (Char_y2 - Char_y1) / 10

    elif Char_x1 > Char_x2:  # 좌측을 바라봄.
        character.clip_draw(frame * 100, 0 * 1, 100, 100, Char_x1, Char_y1)
        Char_x1 += (Char_x2 - Char_x1) / 10
        Char_y1 += (Char_y2 - Char_y1) / 10

    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()

close_canvas()




