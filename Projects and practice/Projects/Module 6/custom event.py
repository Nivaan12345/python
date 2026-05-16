import pygame

pygame.init()
scwi,sche=500,500
screen=pygame.display.set_mode((scwi,sche))
pygame.display.set_caption('custom event')
SPRITE_COLOUR_CHANGE_EVENT=pygame.USEREVENT+2
x,y=250,250
spwi,sphe=60,60
clock=pygame.time.Clock()
done=False
class sprite(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

    screen.fill((255,0,0))
def change_color(self):
    self.fill(pygame.Color("red"))

sp1=pygame.draw.rect(screen,pygame.Color('darkgreen'),
                         (x,y,spwi,sphe))
sp2=pygame.draw.rect(screen,pygame.Color('green'),
                         (400,400,spwi,sphe))


    
if sp1.bottom >=500 or sp1.top <0 or sp1.right >=500 or sp1.left <0:
        pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))


while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done=True
        elif event.type==SPRITE_COLOUR_CHANGE_EVENT:
            sp1.change_color()
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3

        x=min(max(0,x),scwi - spwi)
        y=min(max(0,y),sche - sphe)
        pygame.display.flip()
clock.tick(90)
pygame.quit()