import pygame
pygame.init()

screen_width,screen_height=500,500
screen=pygame.display.set_mode((500,500))
screen.fill((58,58,58))

pygame.display.set_caption("My first game screen")

logo_img=pygame.transform.scale(
    pygame.image.load("/Users/apple/Desktop/Python/Module 6/Lesson 1/Unknown.png").convert_alpha(),(300,300)
)
logo_rect=logo_img.get_rect(center=(screen_width//2,screen_height//2))

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        screen.blit(logo_img,logo_rect)
        pygame.display.flip()
      