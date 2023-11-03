# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
leveys = 640
korkeus = 480
naytto = pygame.display.set_mode((leveys, korkeus))

robo = pygame.image.load("robo.png")

nopeus = 1
x = 0
y = 0
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    naytto.fill((0,0,0))
    naytto.blit(robo,(x,y))
    pygame.display.flip()
    
    if x+robo.get_width() >= leveys and y+robo.get_height() <= korkeus: #oikea ylä
        y += nopeus
    
    elif y+robo.get_height() >= korkeus and x >= 0: #oikea ala
        x -= nopeus
        
    elif x <= 0 and y >= 0: #vasen ala
        y -= nopeus
        
    else: #vasen ylä
        x += nopeus
        
    
    kello.tick(400)