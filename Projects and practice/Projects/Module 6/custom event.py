import pygame
pygame.init()

Back=pygame.display.set_mode((500,500))
pygame.display.set_caption("Lets add sprites!!")
clock=pygame.time.Clock()
x,y=250,250
SPRITE_COLOUR_CHANGE_EVENT=pygame.USEREVENT+1

class Sprite(pygame.sprite.Sprite):

    def __init__(self,color,height,width):

        super().__init__()

        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.image = pygame.Surface((50, 50)) 
def colour_chaange(self):
    self.fill(pygame.Color("red"))
done=False
while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
               done=True
        elif event.type==SPRITE_COLOUR_CHANGE_EVENT:
             sp1.colour_change()
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 10
        if pressed[pygame.K_RIGHT]: x += 10
        if pressed[pygame.K_UP]: y -= 10
        if pressed[pygame.K_DOWN]: y += 10
        Back.fill((58,58,58))       
        sp1=pygame.draw.rect(Back,(pygame.Color("darkgreen")),
                 (x,y,60,60))
        pygame.draw.rect(Back,(pygame.Color("darkblue")),
                 (320,320,60,60))
        if sp1.bottom >=500 or sp1.top <0 or sp1.right >=500 or sp1.left <0:
           pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))
        x=min(max(0,x),440)
        y=min(max(0,y),440)
        pygame.display.flip()
clock.tick(90)

pygame.quit()