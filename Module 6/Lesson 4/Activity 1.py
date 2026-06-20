import pygame
import random

pygame.init()
screen_width,screen_height=800,600
movement_speed=5
font_size=72

try:
    bg_img=pygame.transform.scale(pygame.image.load("/Users/apple/Desktop/Python/Module 6/Lesson 4/bg.png"),(screen_width,screen_height))
except:
        bg_img=pygame.surface.Surface((screen_width,screen_height))
        bg_img.fill(pygame.Color("white"))

font=pygame.font.SysFont("Times new roman",font_size)

class sprite(pygame.sprite.Sprite):
      
    def __init__(self, color, width, height) -> None:
            super().__init__()
            self.image=pygame.Surface([width,height])
            self.image.fill(color)
            self.rect=self.image.get_rect()
        
    def move(self,x_change,y_change):
        self.rect.x=max(min(self.rect.x+x_change, screen_width-self.rect.width),0)
        self.rect.y=max(min(self.rect.y+y_change, screen_height-self.rect.height),0)

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite collision game")
all_sprites=pygame.sprite.Group()

sprite1=sprite(pygame.Color("black"),50,50)
sprite1.rect.x, sprite1.rect.y=random.randint(0, screen_width-50),random.randint(0,screen_height-50)
all_sprites.add(sprite1)

sprite2=sprite(pygame.Color("red"),50,50)
sprite2.rect.x, sprite2.rect.y=random.randint(0, screen_width-50),random.randint(0,screen_height-50)
all_sprites.add(sprite2)

running, won=True, False
clock=pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    if not won:
        keys=pygame.key.get_pressed()
        x_change=(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])*movement_speed
        y_change=(keys[pygame.K_DOWN] - keys[pygame.K_UP])*movement_speed
        sprite1.move(x_change,y_change)
        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove()
            won=True
    screen.blit(bg_img,(0,0))
    all_sprites.draw(screen)

    if won:
         win_text=font.render("You win",True,pygame.Color("black"))
         screen.blit(win_text, ((screen_width-win_text.get_width())//2,(screen_height-win_text.get_height())//2))   
    pygame.display.flip()
    clock.tick(90)
pygame.quit()          
