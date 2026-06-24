import pygame
pygame.init()
clock=pygame.time.Clock()
screen_width,screen_height=500,500
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('My first game screen')
screen.fill((255,255,255))
pygame.draw.rect(screen,(58,58,58),(250,250,50,50))
x=250
pressed=pygame.key.get_pressed()
if pressed[pygame.K_LEFT]: x -= 3
if pressed[pygame.K_RIGHT]: x += 3
if pressed[pygame.K_UP]: x -= 3
if pressed[pygame.K_DOWN]: x += 3

done=False

while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done=True
pygame.display.flip
clock.tick(90)
pygame.quit()
