import pygame

pygame.init()

screen=pygame.display.set_mode((400,500))
img=pygame.image.load("picture.jpg")
img=pygame.transform.scale(img,(300,300))
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    pygame.display.flip()
#end