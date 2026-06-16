import pygame
import random

pygame.init()

# Custom events
sprite_color_change = pygame.USEREVENT + 1
bg_color_change = pygame.USEREVENT + 2

# Background colors
blue = pygame.Color('blue')
lightblue = pygame.Color('lightblue')
darkblue = pygame.Color('darkblue')

# Sprite colors
red = pygame.Color('red')
yellow = pygame.Color('yellow')
orange = pygame.Color('orange')
white = pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-3, 3]), random.choice([-3, 3])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0:
            self.rect.left = 0
            self.velocity[0] = -self.velocity[0] 
            boundary_hit = True
        elif self.rect.right >= 500:
            self.rect.right = 500
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity[1] = -self.velocity[1] 
            boundary_hit = True
        elif self.rect.bottom >= 400:
            self.rect.bottom = 400
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_color_change))
            pygame.event.post(pygame.event.Event(bg_color_change))

    def change_color(self):
        self.image.fill(random.choice([red, yellow, orange, white]))

def change_bg_color():
    global bg_color
    bg_color = random.choice([blue, lightblue, darkblue])

all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(white, 30, 20)
sp1.rect.x = random.randint(0, 470)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)

screen = pygame.display.set_mode([500, 400])
bg_color = blue
screen.fill(bg_color)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == sprite_color_change:
            sp1.change_color()
        elif event.type == bg_color_change:
            change_bg_color()

    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()