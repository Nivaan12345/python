import pygame
import random
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Add more sprites")
score_value=0
clock=pygame.time.Clock()
screen.fill((58,58,58))
x=250
y=250
class Sprite(pygame.sprite.Sprite):

    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width, height])
        self.image.fill(
            pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image,color,pygame.Rect(x,y,width,height))
        self.rect=self.image.get_rect()
sprite1= Sprite(pygame.Color('black'),20, 30)
class enemy(pygame.sprite.Sprite):

    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width, height])
        self.image.fill(
            pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image,color,pygame.Rect((random.randint(1,500)),(random.randint(1,500)),width,height))
        self.rect=self.image.get_rect()
for i in range(7):
    enemyx= enemy(pygame.Color('red'),20, 30)

def show_score(x,y):
    font=pygame.font.Font('freesansbold.ttf',32)
    score=font.render("Score :"+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
done=False
pygame.display.flip()
while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done=True
        
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3

        if sprite1.rect.colliderect(enemyx.rect):
            score_value+=1

    clock.tick(240)
pygame.quit()