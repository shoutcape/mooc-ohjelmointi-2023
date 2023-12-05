# TEE RATKAISUSI TÄHÄN:
import pygame
from random import randint

pygame.init()

leveys = 640
korkeus = 480

naytto = pygame.display.set_mode((leveys,korkeus))
kello = pygame.time.Clock()
robo = pygame.image.load("robo.png")

roboleveys = robo.get_width()
robokorkeus = robo.get_height()

x = randint(0,leveys-roboleveys)
y = randint(0,korkeus-robokorkeus)

click_x = None
click_y = None

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            click_x = tapahtuma.pos[0]
            click_y = tapahtuma.pos[1]
            if click_x in range(x, x+roboleveys) and click_y in range(y, y+robokorkeus):
                x = randint(0,leveys-roboleveys)
                y = randint(0,korkeus-robokorkeus)

        if tapahtuma.type == pygame.QUIT:
            exit()
        
    naytto.fill((0,0,0))
    naytto.blit(robo,(x,y))
    pygame.display.flip()
    
    kello.tick(60)