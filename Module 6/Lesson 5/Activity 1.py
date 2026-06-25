import math
import random
import pygame

screen_width = 800
screen_height = 600
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 4 
enemy_speed_y = 40
bullet_speed_y = 10
collision_threshold = 27
num_of_enemies = 6  

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

path_prefix = "/Users/apple/Desktop/Python/Module 6/Lesson 5/"

bg = pygame.image.load(path_prefix + "space_bg.jpg")

raw_player_img = pygame.image.load(path_prefix + "player.png")
player_img = pygame.transform.scale(raw_player_img, (64, 64))

raw_bullet_img = pygame.image.load(path_prefix + "bullet.png")
bullet_img = pygame.transform.scale(raw_bullet_img, (16, 32))

pygame.mixer.music.load(path_prefix + "tokyorifft-interstellar-374344.mp3")
pygame.mixer.music.set_volume(1.0) 
pygame.mixer.music.play(-1)

shoot_sound = pygame.mixer.Sound(path_prefix + "cannon.mp3")
shoot_sound.set_volume(0.45)

hit_sound = pygame.mixer.Sound(path_prefix + "vine-boom.mp3")
hit_sound.set_volume(1.0)

game_over_sound = pygame.mixer.Sound(path_prefix + "super-mario-bros_2.mp3")

game_over_sound_played = False

player_x = player_start_x
player_y = player_start_y
player_x_change = 0

enemy_images = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

for i in range(num_of_enemies):
    enemy_images.append(pygame.transform.scale(pygame.image.load(path_prefix + "enemy.png"), (48, 48)))
    enemy_x.append(random.randint(0, screen_width - 64))
    enemy_y.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

bullet_x = 0
bullet_y = player_start_y
bullet_y_change = bullet_speed_y
bullet_state = "ready"

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10
game_over_font = pygame.font.Font("freesansbold.ttf", 64)

def show_score(x, y):
    score_value = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x, y))

def game_over_text():
    over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def enemy(x, y, i):
    screen.blit(enemy_images[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 24, y - 10)) 

def player(x, y):
    screen.blit(player_img, (x, y))

def is_collision(ex, ey, bx, by):
    distance = math.sqrt((ex - bx) ** 2 + (ey - by) ** 2)
    return distance < collision_threshold


running = True
clock = pygame.time.Clock() 
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
                    shoot_sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change
    player_x = max(0, min(player_x, screen_width - 64))

    for i in range(num_of_enemies):
        if enemy_y[i] > 340:  
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            
            if not game_over_sound_played:
                pygame.mixer.music.stop()
                game_over_sound.play()
                game_over_sound_played = True
                
            game_over_text()
            break

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = enemy_speed_x
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= screen_width - 48:
            enemy_x_change[i] = -enemy_speed_x
            enemy_y[i] += enemy_y_change[i]

        if bullet_state == "fire":
            if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
                hit_sound.play()
                bullet_y = player_start_y
                bullet_state = "ready"
                score += 1
                enemy_x[i] = random.randint(0, screen_width - 64)
                enemy_y[i] = random.randint(enemy_start_y_min, enemy_start_y_max)

        enemy(enemy_x[i], enemy_y[i], i)

    if bullet_y < 0:
        bullet_y = player_start_y
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()
    clock.tick(60) 

pygame.quit()