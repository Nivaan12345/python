import pygame
pygame.init()

Back=pygame.display.set_mode((500,500))
pygame.display.set_caption("Lets add sprites!!")
clock=pygame.time.Clock()
x,y=250,250




Back.fill((58,58,58))
pygame.draw.rect(Back,(pygame.Color("darkgreen")),
                 (x,y,60,60))
pygame.draw.rect(Back,(pygame.Color("darkblue")),
                 (320,320,60,60))
pygame.display.flip()

done=False
while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
           done=True
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3

clock.tick(90)

pygame.quit()