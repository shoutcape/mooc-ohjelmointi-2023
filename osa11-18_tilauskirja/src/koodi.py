# Tee ratkaisusi tähän:

class Tehtava:
    laskuri = 1
    def __init__(self, kuvaus: str, koodari: str, tyomaara: int):
        self.kuvaus = kuvaus
        self.koodari = koodari
        self.tyomaara = tyomaara
        self.id = Tehtava.laskuri
        Tehtava.laskuri += 1
        self.valmis = False
        
    def __str__(self):
        if self.valmis:
            return f"{self.id}: {self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} VALMIS"
        return f"{self.id}: {self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} EI VALMIS"
    
        
    def on_valmis(self):
        return self.valmis
    
    def merkkaa_valmiiksi(self):
        self.valmis = True
        
        
        
class Tilauskirja:
    def __init__(self):
        self.tilaukset = []
        
    def lisaa_tilaus(self, kuvaus: str, koodari: str, tyomaara: int):
        tilaus = Tehtava(kuvaus, koodari, tyomaara)
        self.tilaukset.append(tilaus)
        
    def kaikki_tilaukset(self):
        return self.tilaukset
    
    def koodarit(self):
        return list(set([tilaus.koodari for tilaus in self.tilaukset]))
    
    def merkkaa_valmiiksi(self, id: int):
        for tilaus in self.tilaukset:
            if tilaus.id == id:
                Tehtava.merkkaa_valmiiksi(tilaus)
                return
        raise ValueError
    def ei_valmiit_tilaukset(self):
        tilaukset = []
        for tilaus in self.tilaukset:
            if not tilaus.valmis:
                tilaukset.append(tilaus)
        return tilaukset
    
    def valmiit_tilaukset(self):
        tilaukset = []
        for tilaus in self.tilaukset:
            if tilaus.valmis:
                tilaukset.append(tilaus)
        return tilaukset
    
    def koodarin_status(self, koodari: str):
        if koodari not in [tilaus.koodari for tilaus in self.tilaukset]:
            raise ValueError
        valmiit = 0
        valmiit_tunnit = 0
        ei_valmiit = 0
        ei_valmiit_tunnit = 0
        for tilaus in self.tilaukset:
            if tilaus.koodari == koodari and tilaus.valmis:
                valmiit += 1
                valmiit_tunnit += tilaus.tyomaara
            if tilaus.koodari == koodari and not tilaus.valmis:
                ei_valmiit += 1
                ei_valmiit_tunnit += tilaus.tyomaara

        return (valmiit, ei_valmiit, valmiit_tunnit, ei_valmiit_tunnit)

if __name__ == "__main__":

    t = Tilauskirja()
    t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    t.lisaa_tilaus("tee mobiilipeli", "Erkki", 5)
    t.lisaa_tilaus("koodaa parempi facebook", "joona", 5000)
    t.merkkaa_valmiiksi(1)
    t.merkkaa_valmiiksi(2)
    for kohta in t.ei_valmiit_tilaukset():
        print(kohta)
    