# TEE RATKAISUSI TÄHÄN:
import random

class Sanapeli():
    def __init__(self, kierrokset: int):
        self.voitot1 = 0
        self.voitot2 = 0
        self.kierrokset = kierrokset

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # arvotaan voittaja
        return random.randint(1, 2)

    def pelaa(self):
        print("Sanapeli:")
        for i in range(1, self.kierrokset+1):
            print(f"kierros {i}")
            vastaus1 = input("pelaaja1: ")
            vastaus2 = input("pelaaja2: ")

            if self.kierroksen_voittaja(vastaus1, vastaus2) == 1:
                self.voitot1 += 1
                print("pelaaja 1 voitti")
            elif self.kierroksen_voittaja(vastaus1, vastaus2) == 2:
                self.voitot2 += 1
                print("pelaaja 2 voitti")
            else:
                pass # tasapeli

        print("peli päättyi, voitot:")
        print(f"pelaaja 1: {self.voitot1}")
        print(f"pelaaja 2: {self.voitot2}")
        
class PisinSana(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)
        
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        if len(pelaaja1_sana) > len(pelaaja2_sana):
            return 1
        if len(pelaaja1_sana) < len(pelaaja2_sana):
            return 2        
        
class EnitenVokaaleja(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)
        
        
    def laske_vokaalit(self, sana: str):
        vokaalit = "aeiouyäöå"
        vokaaleja = 0
        for char in sana:
            if char in vokaalit:
                vokaaleja += 1
        return vokaaleja
        
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        
        if self.laske_vokaalit(pelaaja1_sana) > self.laske_vokaalit(pelaaja2_sana):
                return 1
                 
        if self.laske_vokaalit(pelaaja2_sana) > self.laske_vokaalit(pelaaja1_sana):
                return 2
                 
class KiviPaperiSakset(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        valinnat = {"kivi":0, "paperi":1, "sakset":2}

        if pelaaja1_sana not in valinnat.keys() and pelaaja2_sana not in valinnat.keys():
            return 0
        if pelaaja1_sana not in valinnat.keys():
            return 2
        if pelaaja2_sana not in valinnat.keys():
            return 1
        
        suhde = valinnat[pelaaja1_sana] - valinnat[pelaaja2_sana]
        
        if suhde == 0:
            return 0
        if suhde == 1 or suhde == -2:
            return 1
        return 2
        
if __name__ == "__main__":
    p = Sanapeli(3)
    p.pelaa()