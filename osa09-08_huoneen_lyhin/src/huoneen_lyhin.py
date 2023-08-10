# TEE RATKAISUSI TÄHÄN:
class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return self.nimi
class Huone: 
    def __init__(self):
        self.henkilöt = []
    

    def lisaa(self, henkilo: Henkilo):
        self.henkilöt.append(henkilo)

    def on_tyhja(self):
        return len(self.henkilöt) == 0
        
    def tulosta_tiedot(self):
        yhteispituus = sum(henkilo.pituus for henkilo in self.henkilöt)
        print(f"Huoneessa {len(self.henkilöt)} henkilöä, yhteispituus {yhteispituus} cm")
        for henkilo in self.henkilöt:
            print(f'{henkilo.nimi} ({henkilo.pituus} cm)')
            
    def lyhin(self):
        if self.henkilöt == []:
            return None
        
        lyhin = self.henkilöt[0]
        for henkilo in self.henkilöt:
            if henkilo.pituus < lyhin.pituus:
                lyhin = henkilo
        return lyhin
    
    def poista_lyhin(self):
        
        lyhin = self.lyhin()
        if lyhin:
            self.henkilöt.remove(lyhin)
        return lyhin
    
    
if __name__ == "__main__":
    
    huone = Huone()

    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Auli", 186))
    huone.tulosta_tiedot()

    print()

    poistettu = huone.poista_lyhin()
    print(f"Otettiin huoneesta {poistettu.nimi}")

    print()

    huone.tulosta_tiedot()