import pygame


pygame.init()
screen_width,screen_height=500,500
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('My first game screen')
screen.fill((58,58,58))

img=pygame.image.load("pickleball.jpg")
img=pygame.transform.scale(img,(300,300))
done=False
pygame.display.flip()

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()