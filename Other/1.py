import pygame
import math
import random
import sys

BG = (0, 0, 139)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

BALL_RADIUS = 50
PADDLE_W = 200
PADDLE_H = 10
PADDLE_SPEED = 200
BOTTOM_GAP = 95

START_WAIT = 1.0

pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
pygame.display.set_caption("Dotted Ball Bouncer")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 42)

difficulty = 1
speed_map = {1: 100, 2: 200, 3: 400}
score_map = {1: 1, 2: 2, 3: 4}

state = "MENU"

def reset_round():
    global ball_x, ball_y, ball_vx, ball_vy, launch_timer
    w, h = screen.get_size()
    ball_x = w / 2
    ball_y = 100
    ball_vx = 0
    ball_vy = 0
    launch_timer = 0.0

def start_game(diff):
    global difficulty, score, state, paddle_x
    difficulty = diff
    score = 0
    paddle_x = (screen.get_width() - PADDLE_W) / 2
    reset_round()
    state = "PLAYING"

def draw_dotted_circle(surface, center, radius):
    cx, cy = center
    circumference = 2 * math.pi * radius
    angle = -math.pi / 2
    travelled = 0.0
    draw = True

    while travelled < circumference:
        if draw:
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            ix, iy = int(round(x)), int(round(y))
            if 0 <= ix < surface.get_width() and 0 <= iy < surface.get_height():
                surface.set_at((ix, iy), WHITE)

        angle += 1.0 / radius
        travelled += 1.0
        draw = not draw

score = 0
paddle_x = 0
reset_round()

running = True
while running:
    dt = clock.tick(120) / 1000.0

    w, h = screen.get_size()
    paddle_y = h - BOTTOM_GAP - PADDLE_H

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_1:
                start_game(1)

            elif event.key == pygame.K_2:
                start_game(2)

            elif event.key == pygame.K_3:
                start_game(3)

            elif event.key == pygame.K_SPACE:
                if state == "WIN_WAIT":
                    score = 0
                    reset_round()
                    state = "PLAYING"

    keys = pygame.key.get_pressed()

    if state == "PLAYING":
        if keys[pygame.K_a]:
            paddle_x -= PADDLE_SPEED * dt
        if keys[pygame.K_d]:
            paddle_x += PADDLE_SPEED * dt

        paddle_x = max(0, min(w - PADDLE_W, paddle_x))

        launch_timer += dt

        if ball_vx == 0 and ball_vy == 0 and launch_timer >= START_WAIT:
            speed = speed_map[difficulty]
            ang = random.uniform(math.radians(20), math.radians(160))
            ball_vx = math.cos(ang) * speed
            ball_vy = abs(math.sin(ang)) * speed

        ball_x += ball_vx * dt
        ball_y += ball_vy * dt

        if ball_x - BALL_RADIUS <= 0:
            ball_x = BALL_RADIUS
            ball_vx *= -1

        if ball_x + BALL_RADIUS >= w:
            ball_x = w - BALL_RADIUS
            ball_vx *= -1

        if ball_y - BALL_RADIUS <= 0:
            ball_y = BALL_RADIUS
            ball_vy *= -1

        if ball_y + BALL_RADIUS >= h:
            state = "GAME_OVER"

        closest_x = max(paddle_x, min(ball_x, paddle_x + PADDLE_W))
        closest_y = max(paddle_y, min(ball_y, paddle_y + PADDLE_H))

        dx = ball_x - closest_x
        dy = ball_y - closest_y

        if dx * dx + dy * dy < BALL_RADIUS * BALL_RADIUS:
            bottom_clearance = h - (ball_y + BALL_RADIUS)
            paddle_motion_room = max(0, (paddle_y + PADDLE_H) - (ball_y - BALL_RADIUS))

            crushed = bottom_clearance < paddle_motion_room and ball_y > h * 0.65

            if crushed:
                state = "WIN_WAIT"
                reset_round()
            else:
                ball_y = paddle_y - BALL_RADIUS - 1
                ball_vy = -abs(ball_vy)

                score += score_map[difficulty]

                if score >= 100:
                    state = "WIN_WAIT"
                    reset_round()

    screen.fill(BG)

    pygame.draw.rect(
        screen,
        YELLOW,
        (int(paddle_x), int(paddle_y), PADDLE_W, PADDLE_H)
    )

    draw_dotted_circle(screen, (int(ball_x), int(ball_y)), BALL_RADIUS)

    txt = font.render(f"Score: {score}", True, WHITE)
    screen.blit(txt, (15, 15))

    if state == "MENU":
        m = font.render("Press 1, 2 or 3 to start", True, WHITE)
        screen.blit(m, (w//2 - m.get_width()//2, h//2))

    elif state == "GAME_OVER":
        m = font.render("GAME OVER - Press 1,2,3", True, WHITE)
        screen.blit(m, (w//2 - m.get_width()//2, h//2))

    elif state == "WIN_WAIT":
        m = font.render("YOU WIN - Press SPACE for next game", True, WHITE)
        screen.blit(m, (w//2 - m.get_width()//2, h//2))

    pygame.display.flip()

pygame.quit()
sys.exit()
