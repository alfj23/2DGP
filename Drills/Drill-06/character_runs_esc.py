from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True
x = 0
frame = 0


def handle_events():
   global running
   events = get_events() # 이벤트들이 담긴 리스트가 넘어옴.
   for event in events: # 이벤트를 하나씩 꺼내서 확인함.
       if event.type == SDL_QUIT:  # SDL_QUIT : 윈도우 종료 버튼 눌렀을시 발생
            running = False
       elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            # SDL_KEYDOWN(KEYUP):키가 눌리거나 떼어질 때 발생
            # event.key에 key 값이 넘어옴
            running = False

while x < 800 and running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)

close_canvas()

