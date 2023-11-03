# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
leveys = 640
korkeus = 480
naytto = pygame.display.set_mode((leveys, korkeus))

robo = pygame.image.load("robo.png")

nopeus = 1
nopeus2 = 2
x = 0
y = 100

x2 = 0
y2 = 200
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    naytto.fill((0,0,0))
    naytto.blit(robo,(x,y))
    naytto.blit(robo,(x2,y2))
    pygame.display.flip()
    
    x += nopeus
    x2 += nopeus2
    if x+robo.get_width() >= leveys:
        nopeus = -nopeus
    
    if x2+robo.get_width() >= leveys:
        nopeus2 = -nopeus2
    
    if x2 <= 0:
        nopeus2 = -nopeus2
    if x <= 0:
        nopeus = -nopeus
        
    
    kello.tick(400)