# TEE RATKAISUSI TÄHÄN:
import pygame
import math

pygame.init()
leveys = 640
korkeus = 480

naytto = pygame.display.set_mode((leveys, korkeus))

robo = pygame.image.load("robo.png")
maara = 10
kulma = 0
sade = 150
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    for i in range(maara):
        x = leveys/2+math.cos(kulma+2*math.pi*i/maara)*sade-robo.get_width()/2
        y = 240+math.sin(kulma+i*120)*140-robo.get_height()/2
        y = korkeus/2+math.sin(kulma+2*math.pi*i/maara)*sade-robo.get_height()/2

        naytto.blit(robo, (x, y))

    pygame.display.flip()
    kulma += 0.1
    
    naytto.fill((0, 0, 0))
    kello.tick(60)