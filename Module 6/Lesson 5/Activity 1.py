import math
import random
import pygame

screen_width=800
screen_height=600
player_start_x=370
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x=5
enemy_speed_y=40
bullet_speed_y=10
collision_threshhold=27

pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Space Invaders")
bg=pygame.image.load("/Users/apple/Desktop/Python/Module 6/Lesson 5/space_bg.jpg")

player_img=pygame.image.load("/Users/apple/Desktop/Python/Module 6/Lesson 5/player.png")
player_x=player_start_x
player_y=player_start_y
player_x_change=0

enemy_img=[]
enemy_x=[]
enemy_y=[]
enemy_x_change=[]
enemy_y_change=[]
num_of_enemies=[]

for i in range(num_of_enemies):
    enemy_img=pygame.image.load("/Users/apple/Desktop/Python/Module 6/Lesson 5/enemy.png")
    enemy_x.append(random.randint(0,screen_width-64))
    enemy_y.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

bullet_img=pygame.image.load("/Users/apple/Desktop/Python/Module 6/Lesson 5/bullet.png")
bullet_x=0
bullet_y=player_start_y
bullet_x_change=0
bullet_y_change=bullet_speed_y
bullet_state="ready"

score=0
font=pygame.font.Font("freesansbold.ttf",32)
text_x=10
text_y=10

game_over_font=pygame.font.Font("freesansbold.ttf",64)

def show_score(x,y):
    score_value=font.render("Score:"+str(score),True,(255,255,255))
    screen.blit(score_value,(x,y))

def game_over_text():
    over_text=game_over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,200))

def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet_img,(x+16,y+10))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance=math.sqrt((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2)
    return distance<collision_threshhold
