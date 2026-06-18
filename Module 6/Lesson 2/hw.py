import pygame
pygame.init()

screen_w,screen_h=640,480
rect_w,rect_h=180,120
screen=pygame.display.set_mode((screen_w,screen_h))

pygame.display.set_caption("My first game screen")
font=pygame.font.Font(None,36)
text=font.render("Hello World",True,(255,255,255))


done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            pygame.quit()
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(0,0,255),((screen_w-rect_w)/2,(screen_h-rect_h)/2,rect_w,rect_h))
        screen.blit(text,((screen_w-rect_w)/2,(screen_h-rect_h)/2))
        pygame.display.flip()