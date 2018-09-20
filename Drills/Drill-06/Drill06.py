from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global Char_x, Char_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            Char_x, Char_y = event.x - 25, KPU_HEIGHT - 1 - event.y + 25


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
Char_x, Char_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_arrow.draw(x, y)
    # x_change = (Char_x - x)
    # y_change = (Char_y - y)
    # m = y_change / x_change
    if x < Char_x:  # 우측을 바라봄.
        character.clip_draw(frame * 100, 0 * 1, 100, 100, Char_x, Char_y)
    elif x > Char_x:  # 좌측을 바라봄.
        character.clip_draw(frame * 100, 100 * 1, 100, 100, Char_x, Char_y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()

close_canvas()
