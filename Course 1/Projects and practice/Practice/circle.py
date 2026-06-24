import pygame

pygame.init()
screen_width,screen_height=500,500
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Circle')
screen.fill((0,0,0))

clock=pygame.time.Clock()

done=False

while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()

    pygame.draw.circle(screen,(255,255,255),(250,250),60,60)
    pygame.display.flip()
    clock.tick(90)