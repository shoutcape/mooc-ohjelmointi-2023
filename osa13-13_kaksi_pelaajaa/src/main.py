# TEE RATKAISUSI TÄHÄN:
# TEE RATKAISUSI TÄHÄN:
import pygame 

pygame.init()

leveys = 640
korkeus = 480

naytto= pygame.display.set_mode((leveys,korkeus))
robo = pygame.image.load("robo.png")
kello = pygame.time.Clock()
#      [0] = pelaaja1                 [1] = pelaaja2
kohdat = [[0,0],[leveys-robo.get_width(), korkeus-robo.get_height()]]

napit = []
#nappi, pelaaja, x arvo, y arvo.
napit.append((pygame.K_LEFT, 0, -2, 0))
napit.append((pygame.K_RIGHT, 0, 2, 0))
napit.append((pygame.K_UP, 0, 0, -2))
napit.append((pygame.K_DOWN, 0, 0, 2))
napit.append((pygame.K_a, 1, -2, 0))
napit.append((pygame.K_d, 1, 2, 0))
napit.append((pygame.K_w, 1, 0, -2))
napit.append((pygame.K_s, 1, 0, 2))

painettu = {}

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            painettu[tapahtuma.key] = True
        
        if tapahtuma.type == pygame.KEYUP:
            del painettu[tapahtuma.key]
        if tapahtuma.type==pygame.QUIT:
            exit()
    
    for nappi in napit:
        if nappi[0] in painettu:

            #pelaaja, x vai y, lisätään x tai y napista
            kohdat[nappi[1]][0] += nappi[2]
            kohdat[nappi[1]][1] += nappi[3]

    naytto.fill((0,0,0))
    print(painettu)
    for i in range(2):
        naytto.blit(robo, (kohdat[i][0], kohdat[i][1]))
    pygame.display.flip()
    kello.tick(60)