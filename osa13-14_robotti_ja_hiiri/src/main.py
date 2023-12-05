# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
leveys = 640
korkeus = 480

kello = pygame.time.Clock()
naytto = pygame.display.set_mode((leveys,korkeus))
robo = pygame.image.load("robo.png")

x = 0
y = 0

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEMOTION:
            x = tapahtuma.pos[0]-robo.get_width()/2
            y = tapahtuma.pos[1]-robo.get_height()/2
            naytto.fill((0,0,0))
            naytto.blit(robo,(x,y))
            pygame.display.flip()

        if tapahtuma.type == pygame.QUIT:
            exit()




    kello.tick(60)
