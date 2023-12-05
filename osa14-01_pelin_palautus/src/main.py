import pygame
from random import randint
class Peli:
    def __init__(self):
        pygame.init()

        self.ennatys = 0
        self.alusta_peli()
        self.aloita_peli()

    def alusta_peli(self):
        
        self.leveys = 1024
        self.korkeus = 768
        self.naytto = pygame.display.set_mode((self.leveys, self.korkeus))

        pygame.display.set_caption("Robotti ja hirviöt")
        self.robo = pygame.image.load("robo.png")
        self.kello = pygame.time.Clock()
        self.x = 0
        self.y = self.korkeus - self.robo.get_height()

        self.vasemmalle = False
        self.oikealle = False
        self.ylos = False
        self.alas = False

        self.pisteet = 0
        self.teksti = pygame.font.SysFont("Arial", 24)
        self.pistelaskuri = self.teksti.render("Pisteet: " + str(self.pisteet), True, (255, 255, 255))

        self.robotti = Robotti(self.leveys, self.korkeus, self.robo)
        self.kolikot = []
        self.kolikot.append(Kolikko(self.leveys, self.korkeus))
        
        hirvioiden_maara = 3
        self.hirviot = []
        for i in range(hirvioiden_maara):
            self.hirviot.append(Hirvio(self.leveys, self.korkeus))
    
    def aloita_peli(self):
        while True:
            self.kasittele_tapahtumat()
            self.paivita()
            self.piirra()
            self.kello.tick(60)

    def kasittele_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_ESCAPE:
                    exit()
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = True
                if tapahtuma.key == pygame.K_UP:
                    self.ylos = True
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = True

            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = False
                if tapahtuma.key == pygame.K_UP:
                    self.ylos = False
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = False
            if tapahtuma.type == pygame.QUIT:
                exit()
    
    def paivita(self):            
        self.robotti.liiku(self.vasemmalle, self.oikealle, self.ylos, self.alas)
        
        for kolikko in self.kolikot:
            if self.robotti.osuu(kolikko):
                self.kolikot.remove(kolikko)
                self.kolikot.append(Kolikko(self.leveys, self.korkeus))
                self.pisteet += 1
                self.pistelaskuri = self.teksti.render("Pisteet: " + str(self.pisteet), True, (255, 255, 255))
                if self.pisteet % 3 == 0:
                    self.hirviot.append(Hirvio(self.leveys, self.korkeus))
        
        for hirvio in self.hirviot:
            hirvio.liiku()
            if self.robotti.osuu(hirvio):
                self.loppu()

    def piirra(self):
        self.naytto.fill((0, 0, 200))
        self.naytto.blit(self.robo, (self.robotti.x, self.robotti.y))
        
        for kolikko in self.kolikot:
            self.naytto.blit(kolikko.kuva, (kolikko.x, kolikko.y))
        
        for hirvio in self.hirviot:
            self.naytto.blit(hirvio.kuva, (hirvio.x, hirvio.y))
        
        self.naytto.blit(self.pistelaskuri, (10, 10))
        pygame.display.flip()
    
    def loppu(self):

        if self.pisteet > self.ennatys:
            self.ennatys = self.pisteet

        while True:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_ESCAPE:
                        exit()
                    if tapahtuma.key == pygame.K_SPACE:
                        self.alusta_peli()
                        return

                if tapahtuma.type == pygame.QUIT:
                    exit()

                self.naytto.fill((0, 0, 0))
                self.naytto.blit(self.teksti.render("Peli loppui!", True, (255, 255, 255)), (self.leveys / 2 - 100, self.korkeus / 2 - 100))
                self.naytto.blit(self.teksti.render("Pisteet: " + str(self.pisteet), True, (255, 255, 255)), (self.leveys / 2 - 100, self.korkeus / 2 - 50))
                self.naytto.blit(self.teksti.render("Ennätys: " + str(self.ennatys), True, (255, 255, 255)), (self.leveys / 2 - 100, self.korkeus / 2 - 25))
                self.naytto.blit(self.teksti.render("Paina välilyöntiä aloittaaksesi uudelleen", True, (255, 255, 255)), (self.leveys / 2 - 100, self.korkeus / 2))
                pygame.display.flip()


class Robotti:
    def __init__(self, leveys, korkeus, kuva):
        self.x = leveys / 2 - kuva.get_width() / 2
        self.y = korkeus / 2 - kuva.get_height() / 2
        self.leveys = leveys
        self.korkeus = korkeus
        self.kuva = kuva
    
    def liiku(self, vasemmalle, oikealle, ylos, alas):
        if vasemmalle:
            self.x -= 10
        if oikealle:
            self.x += 10
        if ylos:
            self.y -= 10
        if alas:
            self.y += 10
        self.x = min(self.x, self.leveys - self.kuva.get_width())
        self.x = max(self.x, 0)
        self.y = max(self.y, 0)
        self.y = min(self.y, self.korkeus - self.kuva.get_height())
    
    def osuu(self, objekti):
        # virhemarginaali on olemassa, jotta pelaaja ei osu objektiin liian helposti
        virhemarginaali = 20

        oman_leveys = self.kuva.get_width() - virhemarginaali
        oman_korkeus = self.kuva.get_height() - virhemarginaali
        objektin_leveys = objekti.kuva.get_width() - virhemarginaali
        objektin_korkeus = objekti.kuva.get_height() - virhemarginaali

        x_osuu = self.x < objekti.x + objektin_leveys and self.x + oman_leveys > objekti.x
        y_osuu = self.y < objekti.y + objektin_korkeus and self.y + oman_korkeus > objekti.y
    
        if x_osuu and y_osuu:
            return True
        return False

class Kolikko:
    def __init__(self, leveys, korkeus):
        self.x = randint(0, leveys - 64)
        self.y = randint(0, korkeus - 64)
        self.kuva = pygame.image.load("kolikko.png")
    
class Hirvio:
    def __init__(self, leveys, korkeus):
        self.leveys = leveys
        self.korkeus = korkeus
        self.kuva = pygame.image.load("hirvio.png")
        
        self.reunavara = 64
        self.x = randint(0, leveys - self.reunavara)
        self.y = randint(0, korkeus - self.reunavara)

        # arvotaan suunta, johon hirviö syntyessään liikkuu
        self.dx = 3 if randint(0, 1) == 0 else -3
        self.dy = 3 if randint(0, 1) == 0 else -3

    def liiku(self):
        self.x += self.dx
        self.y += self.dy

        # tarkistetaan, osuuko hirviö seinään
        # jos osuu, vaihdetaan suuntaa
        # reunavara on mukana, jotta hirviö ei mene seinän sisään
        if self.x < 0 or self.x > self.leveys - self.reunavara:
            self.dx *= -1
            self.x = max(min(self.x, self.leveys - self.reunavara), 0)
        if self.y < 0 or self.y > self.korkeus - self.reunavara:
            self.dy *= -1
            self.y = max(min(self.y, self.korkeus - self.reunavara), 0)

if __name__ == "__main__":
    Peli()
