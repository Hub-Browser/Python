import pygame
import random
pygame.init()

screen_width, screen_height=800,600
x_change, y_change=0,0

class sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [5,5]
    
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0:
            self.rect.left = 0
            self.velocity[0] = -self.velocity[0] 

        if self.rect.right >= screen_width:
            self.rect.right = screen_width
            self.velocity[0] = -self.velocity[0]

        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity[1] = -self.velocity[1] 

        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
            self.velocity[1] = -self.velocity[1]
    
    def move(self,x_change,y_change):
        self.rect.x=max(min(self.rect.x+x_change, screen_width-self.rect.width),0)
        self.rect.y=max(min(self.rect.y+y_change, screen_height-self.rect.height),0)

screen=pygame.display.set_mode((screen_width,screen_height))
clock=pygame.time.Clock()
all_sprites=pygame.sprite.Group()

sprite1=sprite(pygame.Color("black"),60,60)
sprite1.rect.x, sprite1.rect.y=random.randint(0, screen_width),random.randint(0,screen_height)

sprite2=sprite(pygame.Color("red"),80,80)
sprite2.rect.x, sprite2.rect.y=random.randint(0, screen_width),random.randint(0,screen_height)

all_sprites.add(sprite1)
all_sprites.add(sprite2)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_UP:
                y_change = -5
            if event.key == pygame.K_DOWN:
                y_change = 5
    
        if event.type==pygame.KEYUP:
            x_change, y_change=0,0

    sprite2.update()
    screen.fill(pygame.Color("white"))
    sprite1.move(x_change,y_change)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(90)
pygame.quit()          


