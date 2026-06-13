import pygame
import random as r

class randomColor:
    def rando(self):
        self.a=r.randint(0,255)
        self.b=r.randint(0,255)
        self.c=r.randint(0,255)
        return (self.a,self.b,self.c)
    def comma(self,num):
        return f"{num:,}"
random=randomColor()
"""
pygame.init()

screen=pygame.display.set_mode((800,600))
screen.fill(random.rando())
pygame.display.set_caption(f"{random.rando()}")
"""
"""
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        pygame.display.flip()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                current=random.rando()
                pygame.display.set_caption(f"{current}")
                screen.fill(current)
"""
running=True
count=0
"""
while running:
    current=random.rando()
    for event in pygame.event.get():    
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        pygame.display.flip()
    if current!=(30,50,30):
        print(current)
        pygame.display.set_caption(f"{current} {count}")
        screen.fill(current)
        count+=1
        pygame.display.flip()
    else:
        pygame.quit()
"""
listt=[]
oCount=1
while running:
    for co in range(1,2):
        count = 0
        searching = True
        while searching:
            current = random.rando()
            example1 = (10,10,10)
            example2 = (20,40,40)
            if all(current[i]>example1[i] for i in range(3)) and all(current[i]<example2[i] for i in range(3)):
                listt.append(count)
                searching = False
            else:
                count += 1   
    if min(listt)<2: 
        running = False
    else:
        oCount+=1
x=0
# FIXED: Outputs the big numbers vertically formatted with commas
print(*(random.comma(i) for i in listt), sep="\n")
print("Other count:",oCount)
print(f"Average: {sum(listt)/oCount:.2f}")

