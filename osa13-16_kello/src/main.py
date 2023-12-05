# TEE RATKAISUSI TÄHÄN:
import pygame
import time
import math

pygame.init()
leveys, korkeus = 640, 480

naytto = pygame.display.set_mode((leveys, korkeus))
kello = pygame.time.Clock()

keskikohta = (leveys/2, korkeus/2)
sade = 200

def rinkula(vari: int, sade: int, paksuus:int):
    pygame.draw.circle(naytto, vari, keskikohta, sade, paksuus)

def viisari(pituus: int, osuus: float):
    kulma = 2*math.pi*osuus-math.pi/2
    x = keskikohta[0]+math.cos(kulma)*pituus
    y = keskikohta[1]+math.sin(kulma)*pituus

    pygame.draw.line(naytto, (0,0,255),keskikohta,(x,y))

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    
    rinkula((255,0,0), 200, 2) #vari, koko, reunan paksuus
    
    aika = time.localtime()
    sekunnit = aika.tm_sec
    minuutit = aika.tm_min
    tunnit = aika.tm_hour

    pygame.display.set_caption(f"{tunnit:02d}:{minuutit:02d}:{sekunnit:02d}")

    viisari(185, sekunnit/60)
    viisari(180, (minuutit+sekunnit/60)/60)
    viisari(150, (tunnit+minuutit/60+sekunnit/3600)/12)
    
    pygame.display.flip()
    naytto.fill((0,0,0))
    kello.tick(1)

