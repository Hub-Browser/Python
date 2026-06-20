import pygame
import random
pygame.init()

screen_width, screen_height=800,600
movement_speed=5

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
            boundary_hit = True

        elif self.rect.right >= screen_width:
            self.rect.right = screen_width
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        elif self.rect.top <= 0:
            self.rect.top = 0
            self.velocity[1] = -self.velocity[1] 
            boundary_hit = True

        elif self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        #if boundary_hit:
        #    pygame.event.post(pygame.event.Event(pygame.USEREVENT+1))
    
    def move(self,x_change,y_change):
        self.rect.x=max(min(self.rect.x+x_change, screen_width-self.rect.width),0)
        self.rect.y=max(min(self.rect.y+y_change, screen_height-self.rect.height),0)

screen=pygame.display.set_mode((screen_width,screen_height))
clock=pygame.time.Clock()
all_sprites=pygame.sprite.Group()

sprite1=sprite(pygame.Color("black"),60,60)
sprite1.rect.x, sprite1.rect.y=random.randint(0, screen_width-50),random.randint(0,screen_height-50)

sprite2=sprite(pygame.Color("red"),80,80)
sprite2.rect.x, sprite2.rect.y=random.randint(0, screen_width-50),random.randint(0,screen_height-50)

all_sprites.add(sprite1)
all_sprites.add(sprite2)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    sprite2.update()
    keys=pygame.key.get_pressed()
    x_change=(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])*movement_speed
    y_change=(keys[pygame.K_DOWN] - keys[pygame.K_UP])*movement_speed

    screen.fill(pygame.Color("white"))
    sprite1.move(x_change,y_change)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(90)
pygame.quit()          


