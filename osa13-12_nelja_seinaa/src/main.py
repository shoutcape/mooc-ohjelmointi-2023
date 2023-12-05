# TEE RATKAISUSI TÄHÄN:
import pygame 

pygame.init()

leveys = 640
korkeus = 480

naytto= pygame.display.set_mode((leveys,korkeus))
robo = pygame.image.load("robo.png")
kello = pygame.time.Clock()

x = 0
y = korkeus - robo.get_height()

vasemmalle = False
oikealle = False
ylos = False
alas = False

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_a:
                vasemmalle = True
            if tapahtuma.key == pygame.K_d:
                oikealle = True
            if tapahtuma.key == pygame.K_w:
                ylos = True
            if tapahtuma.key == pygame.K_s:
                alas = True
                
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_a:
                vasemmalle= False
            if tapahtuma.key == pygame.K_d:
                oikealle = False
            if tapahtuma.key == pygame.K_w:
                ylos = False
            if tapahtuma.key == pygame.K_s:
                alas = False
                
                
        if tapahtuma.type==pygame.QUIT:
            exit()
            
    if vasemmalle:
        x -= 10
    elif oikealle:
        x += 10
    elif ylos: #jos 0, yläreuna menee ruudun ulkopuolelle.
        y -= 10
    elif alas:
        y += 10

    x = min(x,leveys-robo.get_width())
    x = max(x,0)
    y = max(y,0)
    y = min(y,korkeus-robo.get_height())

    naytto.fill((0,0,0))
    naytto.blit(robo,(x,y))
    pygame.display.flip()
    kello.tick(60)