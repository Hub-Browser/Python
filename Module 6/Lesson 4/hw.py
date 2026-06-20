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

        if self.rect.left<=0 or self.rect.right>=screen_width:
            self.velocity[0]=-self.velocity[0] 

        if self.rect.top<=0 or self.rect.bottom>=screen_height:
            self.velocity[1]=-self.velocity[1]
    
    def move(self,x_change,y_change):
        self.rect.x=max(min(self.rect.x+x_change, screen_width-self.rect.width),0)
        self.rect.y=max(min(self.rect.y+y_change, screen_height-self.rect.height),0)

screen=pygame.display.set_mode((screen_width,screen_height))
clock=pygame.time.Clock()
all_sprites=pygame.sprite.Group()

sprite1=sprite(pygame.Color("red"),50,50)
sprite1.rect.x=random.randint(0, screen_width-25)
sprite1.rect.y=random.randint(0,screen_height-25)

sprite2=sprite(pygame.Color("blue"),50,50)
sprite2.rect.x=random.randint(0, screen_width-25)
sprite2.rect.y=random.randint(0,screen_height-25)

all_sprites.add(sprite1)
all_sprites.add(sprite2)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    


    sprite1.update()
    sprite2.update()
    screen.fill(pygame.Color("white"))
    sprite1.move(x_change,y_change)
    all_sprites.draw(screen)

    if sprite1.rect.left <= 0:
        sprite1.rect.left = 0  
        sprite1.image.fill(pygame.Color("red"))

    if sprite1.rect.right >= screen_width:
        sprite1.rect.right = screen_width 
        sprite1.image.fill(pygame.Color("blue"))

    if sprite1.rect.top <= 0:
        sprite1.rect.top = 0
        sprite1.image.fill(pygame.Color("green"))

    if sprite1.rect.bottom >= screen_height:
        sprite1.rect.bottom = screen_height
        sprite1.image.fill(pygame.Color("purple"))

    if sprite2.rect.left <= 0:
        sprite2.rect.left = 0  
        sprite2.image.fill(pygame.Color("orange"))

    if sprite2.rect.right >= screen_width:
        sprite2.rect.right = screen_width 
        sprite2.image.fill(pygame.Color("lightblue"))

    if sprite2.rect.top <= 0:
        sprite2.rect.top = 0  
        sprite2.image.fill(pygame.Color("yellow"))

    if sprite2.rect.bottom >= screen_height:
        sprite2.rect.bottom = screen_height 
        sprite2.image.fill(pygame.Color("pink"))

    pygame.display.flip()
    clock.tick(90)
pygame.quit()          


