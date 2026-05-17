import pygame
pygame.init()

Back=pygame.display.set_mode((500,500))
pygame.display.set_caption("Lets add sprites!!")
clock=pygame.time.Clock()
x,y=250,250
SPRITE_COLOUR_CHANGE_EVENT=pygame.USEREVENT+1
Back.fill((58,58,58))
class Sprite(pygame.sprite.Sprite):

    def __init__(self,color,height,width):

        super().__init__()

        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def colour_change(self):
        self.image.fill(pygame.Color("red"))
sp1 = Sprite(pygame.Color("darkgreen"), 60, 60)
sp2=Sprite(pygame.Color("darkblue"),60, 60)
sp1.rect.topleft = (x, y)

done = False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        elif event.type==SPRITE_COLOUR_CHANGE_EVENT:
            sp1.colour_change()

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x -= 10
    if pressed[pygame.K_RIGHT]: x+= 10
    if pressed[pygame.K_UP]: y -= 10
    if pressed[pygame.K_DOWN]: y += 10

    x = min(max(0, x), 440)
    y = min(max(0, y), 440)
    sp1.rect.topleft = (x, y)

    if sp1.rect.bottom>=500 or sp1.rect.top<0 or sp1.rect.right>=500 or sp1.rect.left<0:
        pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))
    pygame.display.flip()
clock.tick(90)

pygame.quit()