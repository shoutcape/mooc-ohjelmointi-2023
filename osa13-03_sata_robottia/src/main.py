# TEE RATKAISUSI TÄHÄN:
# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

naytto.fill((0, 0, 0))
leveys = 50
korkeus = 50
for i in range(10):
    leveys += 10
    korkeus += 20
    for i in range(10):     
        naytto.blit(robo, (leveys+40*i, korkeus))

pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
            
            