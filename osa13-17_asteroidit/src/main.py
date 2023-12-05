# TEE RATKAISUSI TÄHÄN:
import pygame
from random import randint

pygame.init()
leveys, korkeus = 640, 480

naytto = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("Asteroidit")
robo = pygame.image.load("robo.png")
font = pygame.font.SysFont(None, 24)


robokorkeus = robo.get_height()
roboleveys = robo.get_width()

kivi = pygame.image.load("kivi.png")
kivileveys = kivi.get_width()
kivikorkeus = kivi.get_height()

maara = 20
pistelaskuri = 0

kivet = []
for i in range(maara):
    kivet.append([randint(0,leveys-kivileveys), -randint(100,1000)])

kello = pygame.time.Clock()

robo_x = 100
oikealle = False
vasemmalle = False

while True:
    naytto.fill((0,0,0))
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_a:
                vasemmalle = True
            if tapahtuma.key == pygame.K_d:
                oikealle = True
            
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_a:
                vasemmalle= False
            if tapahtuma.key == pygame.K_d:
                oikealle = False
    
    for i in range(maara):
        kivi_x, kivi_y = kivet[i][0], kivet[i][1]
        kivi_pohja = kivi_y + kivikorkeus
        kivi_oikea = kivi_x + kivileveys
        robo_oikea_reuna = robo_x + roboleveys

        robotin_korkeudella = (kivi_pohja > korkeus-robokorkeus)
        robotin_sisalla = (robo_x <= kivi_x < robo_oikea_reuna) or (robo_x <= kivi_oikea < robo_oikea_reuna)

        if robotin_korkeudella and robotin_sisalla: # jos osuu robottiin kivi valitsee uuden aloituspaikan
            kivet[i][0] = randint(0,leveys-kivileveys)
            kivet[i][1] = -randint(100,1000)
            pistelaskuri += 1
                
        if kivet[i][1]+kivikorkeus == korkeus:
            exit()

        kivet[i][1] += 1
    
    if oikealle:
        robo_x += 10
    if vasemmalle:
        robo_x -= 10

    for i in range(maara):
        naytto.blit(kivi, (kivet[i][0], kivet[i][1]))

    piste_teksti = font.render(f"Pisteet: {pistelaskuri}", True, (0,0,255))

    naytto.blit(piste_teksti,(leveys-piste_teksti.get_width()-10,piste_teksti.get_height()))
    naytto.blit(robo,(robo_x, korkeus-robokorkeus))
    pygame.display.flip()
    kello.tick(60)