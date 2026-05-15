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

x=min(max(0,x),scwi - spwi)
y=min(max(0,y),sche - sphe)

def colour_change(self):
    self.image.fill(pygame.Color('orange'))


screen.fill((255,0,0))

sp1=pygame.draw.rect(screen,pygame.Color('darkgreen'),
                         (x,y,spwi,sphe))
sp2=pygame.draw.rect(screen,pygame.Color('darkblue'),
                         (x,y,spwi,sphe))

pygame.display.flip()
while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done=True
        elif event.type==SPRITE_COLOUR_CHANGE_EVENT:
            sp1.change_color()

clock.tick(90)
pygame.quit()