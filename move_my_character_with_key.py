# from pico2d import *
#
# character = load_image("character.png")
# open_canvas()
# character.draw()

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image("character.png")


def handle_events():
    global running, dir, state, x, y, up

    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                state = 1
            elif event.key == SDLK_LEFT:
                dir -= 1
                state = -1
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_UP:
                up += 1
            elif event.key == SDLK_DOWN:
                up -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                up -= 1
            elif event.key == SDLK_DOWN:
                up += 1
        # fill here

sx, sy = TUK_WIDTH // 2, TUK_HEIGHT // 2
running = True
x = 800 // 2
y = 90
frame = 0
dir = 0
state = 1
up = 0

# fill here
while running:
    clear_canvas()
    tuk_ground.draw(sx, sy)
    if state == -1:
        if dir == -1 or up == -1 or up == 1:  # move_left
            character.clip_composite_draw(157, 22 + (frame + 1) * 42, 50, 42, 0, 'h', x, y, 150, 150)
        elif dir == 0:  # stop
            character.clip_composite_draw(95 + (frame + 1) * 4, 2 + (frame + 1) * 46, 50, 46, 0, 'h', x, y, 150, 150)

    elif state == 1:
        if dir == 1 or up == 1 or up == -1:  # move_left
            character.clip_draw(157, 22 + (frame + 1) * 42, 50, 42, x, y, 150, 150)
        elif dir == 0:  # stop
            character.clip_draw(95 + (frame + 1) * 4, 2 + (frame + 1) * 46, 50, 46, x, y, 150, 150)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 5

    x += dir * 10
    if x < 75 or x > TUK_WIDTH - 75:
        x -= dir * 10
    y += up * 5
    if y < 75 or y > TUK_HEIGHT - 75:
        y -= up * 5
    delay(0.05)

close_canvas()


