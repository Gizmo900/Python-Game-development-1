
import pygame
pygame.init()
import time
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Birthday Card")
font = pygame.font.SysFont("Arial ",70)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    img1 = pygame.image.load("C:\\Users\\Bahadori-jahromia\\Desktop\\Jetlearn coding\\Pyhton game development\\images\\baloons.jpg")
    screen.blit(img1,(0,0))
    text = font.render("Happy Birthday",True,"blue") 
    screen.blit(text,(115,100))
    pygame.display.update()

    time. sleep(2)



    img2= pygame.image.load("C:\\Users\\Bahadori-jahromia\\Desktop\\Jetlearn coding\\Pyhton game development\\images\\present.jpg")
    screen.blit(img2,(0,0))
    text = font.render("Good day",True,"blue") 
    screen.blit(text,(115,200))
    pygame.display.update()

    time. sleep(2)



    img3 = pygame.image.load("C:\\Users\\Bahadori-jahromia\\Desktop\\Jetlearn coding\\Pyhton game development\\images\\cake.jpg")
    screen.blit(img3,(0,0))
    text = font.render("be good",True,"blue") 
    screen.blit(text,(115,50))
    pygame.display.update()

    time. sleep(2)
































 
    pygame.display.update()
















































