import pygame
import random
pygame.init()

screen_width, screen_height = 800,600
x_change, y_change = 5, 5
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [5, 5]
    
    def update(self):
        self.rect.move_ip(self.velocity)

        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.velocity[0] = -self.velocity[0] 

        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.velocity[1] = -self.velocity[1]
    
    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, screen_width - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, screen_height - self.rect.height), 0)

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()

player = Sprite(pygame.Color("blue"), 80, 80)
player.rect.x, player.rect.y = random.randint(0, screen_width - 80), random.randint(0, screen_height - 80)
all_sprites.add(player)

for i in range(7):
    enemy = Sprite(pygame.Color("red"), 60, 60)
    enemy.rect.x = random.randint(0, screen_width - 60)
    enemy.rect.y = random.randint(0, screen_height - 60)
    all_sprites.add(enemy)
    enemies_group.add(enemy)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    all_sprites.update() 
    player.move(x_change, y_change)
    
    hit_enemies = pygame.sprite.spritecollide(player, enemies_group, False)
    
    for hit_enemy in hit_enemies:
        player.velocity[0] = -player.velocity[0]
        player.velocity[1] = -player.velocity[1]

        hit_enemy.velocity[0] = -hit_enemy.velocity[0]
        hit_enemy.velocity[1] = -hit_enemy.velocity[1]

    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(90)

pygame.quit()