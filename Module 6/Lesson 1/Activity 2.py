import pygame
pygame.init()
screen_width,screen_height=500,500
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Adding a background image and codingal logo")

bg_img=pygame.transform.scale(
    pygame.image.load("/Users/apple/Desktop/Python/Module 6/Lesson 1/images.jpeg").convert(),(screen_width,screen_height)
)
logo_img=pygame.transform.scale(
    pygame.image.load("/Users/apple/Desktop/Python/Module 6/Lesson 1/Unknown.png").convert_alpha(),(200,200)
)
logo_rect=logo_img.get_rect(center=(screen_width//2,screen_height//2))
text=pygame.font.Font(None,36).render("Welcome to Codingal",True,pygame.Color("white"))
text_rect=text.get_rect(center=(screen_width//2,screen_height-50))

def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.quit:
                running=False
        screen.blit(bg_img,(0,0))
        screen.blit(logo_img,logo_rect)
        screen.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__=="__main__":
    game_loop()
