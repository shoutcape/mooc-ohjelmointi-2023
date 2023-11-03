# TEE RATKAISUSI TÄHÄN:
import pygame
from random import randint, choice


pygame.init()
leveys = 640
korkeus = 480

ruutu = pygame.display.set_mode((leveys, korkeus))
robo = pygame.image.load("robo.png")
kello = pygame.time.Clock()


robotit = []
maara = 200
for robotti in range(maara):
    x = randint(0,leveys-robo.get_width())
    y = -randint(robo.get_height(),robo.get_height()+150*maara)
    nopeus_y = 3
    nopeus_x = 2 if x > (leveys-robo.get_width())/2 else -2
    robotit.append([x,y,nopeus_x,nopeus_y])
        
while True:    
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    
    for robotti in robotit:
        if robotti[1]+robo.get_height() >= korkeus:
            robotti[0] += robotti[2]
        else:
            robotti[1] += 3 
            
    
    ruutu.fill((0,0,0))
    
    for robotti in robotit:        
        ruutu.blit(robo,(robotti[0],robotti[1]))
    
    pygame.display.flip()
    kello.tick(60)
    
