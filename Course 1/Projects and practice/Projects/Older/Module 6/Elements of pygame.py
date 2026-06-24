import pygame

pygame.init()
screen_width,screen_height=640,480
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('My first game screen')
screen.fill((255,255,255))
pygame.draw.rect(screen,(pygame.Color('blue')),(30,30,60,60))

# took help for next 4 lines
clock= pygame.time.Clock()
font = pygame.font.SysFont(None, 50)
text_surface = font.render("Hello Pygame!", True, (0, 0, 0))
screen.blit(text_surface, (100, 150))
done=False
pygame.display.flip()
while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done=True
pygame.quit()