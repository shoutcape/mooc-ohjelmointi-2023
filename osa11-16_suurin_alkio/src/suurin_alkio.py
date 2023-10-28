# TEE RATKAISUSI TÄHÄN:
class Alkio:
    """ Luokka mallintaa yhtä alkiota binääripuussa """
    def __init__(self, arvo, vasen_lapsi:'Alkio' = None, oikea_lapsi:'Alkio' = None):
        self.arvo = arvo
        self.vasen_lapsi = vasen_lapsi
        self.oikea_lapsi = oikea_lapsi
        


def suurin_alkio(juuri: Alkio):
    
    arvo = juuri.arvo
    
    if juuri.vasen_lapsi:
        vasen_arvo = suurin_alkio(juuri.vasen_lapsi)
        # aina kun uusi metodi kutsutaan, niin se suorittaa itseään niin kauan
        # kunnes tulee if juuri.vasen_lapsi == None
        # jolloin kyseinen suoritus loppuu ja palataan takaisin edelliseen suoritukseen
        # jokainen suoritus palauttaa oman arvonsa sitä kutsuneelle suoritukselle.
    else:
        vasen_arvo = arvo
        
    if juuri.oikea_lapsi:
        oikea_arvo = suurin_alkio(juuri.oikea_lapsi)
    else:
        oikea_arvo = arvo


    return max(juuri.arvo, vasen_arvo, oikea_arvo)

if __name__ == "__main__":
    puu = Alkio(2)

    puu.vasen_lapsi = Alkio(3)
    puu.vasen_lapsi.vasen_lapsi = Alkio(5)
    puu.vasen_lapsi.oikea_lapsi = Alkio(8)

    puu.oikea_lapsi = Alkio(4)
    puu.oikea_lapsi.oikea_lapsi = Alkio(11)

    print(suurin_alkio(puu))