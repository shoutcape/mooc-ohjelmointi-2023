# TEE RATKAISUSI TÄHÄN:
import pygame
import math

pygame.init()
leveys = 640
korkeus = 480
naytto = pygame.display.set_mode((leveys, korkeus))

x = 100
y = 100


pallo = pygame.image.load("pallo.png")

kello = pygame.time.Clock()
leveysnopeus = 1
korkeusnopeus = 1

pallow = pallo.get_width()
palloh = pallo.get_height()


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    if x <= 0 or x + pallow >= leveys:
        leveysnopeus = -leveysnopeus        
        
    if y <= 0 or y + palloh >= korkeus:
        korkeusnopeus = -korkeusnopeus
    
                
    x += leveysnopeus
    y += korkeusnopeus
    
    naytto.blit(pallo,(x,y))
    pygame.display.flip()
    naytto.fill((0,0,0))
    kello.tick(60)
    
    
        
        