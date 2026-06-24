import pygame
import random
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Add more sprites")
score_value=0
clock=pygame.time.Clock()
screen.fill((0,255,0))
x=250
y=250

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,width,height,x,y):
        super().__init__()
        self.image=pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, x, y):
        self.rect.topleft = (x, y)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image=pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width,height))
        self.rect=self.image.get_rect(topleft=(random.randint(0,500-width),random.randint(0,500-height)))


player=Sprite(pygame.Color('black'),30,20,x,y)
enemyx=pygame.sprite.Group()
for i in range(7):
    enemyx.add(Enemy(pygame.Color('red'), 30, 20))

font=pygame.font.Font('freesansbold.ttf', 32)

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3

    x=max(0,min(500-player.rect.width,x))
    y=max(0,min(500-player.rect.height,y))
    player.update(x, y)


    if pygame.sprite.collide_rect(player, enemyx):
      score_value+=1

    enemyx.draw(screen)
    screen.blit(player.image, player.rect)

    score_text = font.render("Score : "+str(score_value),True, (255, 255, 255))
    screen.blit(score_text,(10,10))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()