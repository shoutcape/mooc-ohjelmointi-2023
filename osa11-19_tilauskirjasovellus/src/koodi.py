# tee ratkaisusi tänne
# jos käytät edellisessä tehtävässä tekemiäsi luokkia, kopioi ne tänne
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
    
    def ohjeet(self):
        ohjeet = """
komennot:
0 lopetus
1 lisää tilaus
2 listaa valmiit
3 listaa ei valmiit
4 merkitse tehtävä valmiiksi
5 koodarit
6 koodarin status"""
        print(ohjeet)
       
    
      
    def suorita(self):
        self.ohjeet()
        while True:
            try:
                komento = input("komento: ")
                if komento == "0":
                    break
                
                elif komento == "1":
                    kuvaus = input("kuvaus: ")
                    koodari_ja_tyo = input("koodari ja työmääräarvio: ").split()
                    self.lisaa_tilaus(kuvaus, koodari_ja_tyo[0], int(koodari_ja_tyo[1]))
                    print("lisätty!")

                elif komento == "2":
                    if self.valmiit_tilaukset():
                        for kohta in self.valmiit_tilaukset():
                            print(kohta)
                    else:
                        print("ei valmiita")

                elif komento == "3":
                    if self.ei_valmiit_tilaukset():
                        for kohta in self.ei_valmiit_tilaukset():
                            print(kohta)

                elif komento == "4":
                    tunniste = int(input("tunniste: "))
                    self.merkkaa_valmiiksi(tunniste)
                    print("merkitty valmiiksi")

                elif komento == "5":
                    for koodari in self.koodarit():
                        print(koodari)

                elif komento == "6":
                    koodari = input("koodari:")
                    status = self.koodarin_status(koodari)
                    print(f"työt: valmiina {status[0]} ei valmiina {status[1]}, tunteja: tehty {status[2]} tekemättä {status[3]}")
            except:
                print("virheellinen syöte")
                    
def main():
    tk = Tilauskirja()
    tk.suorita()

main()
