import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
screen.fill((255,255,255))
pygame.draw.circle(screen,(0,255,0),(300,300),50)
pygame.draw.circle(screen,(0,255,0),(200,200),50,3)
pygame.display.update()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit
        pygame.display.flip