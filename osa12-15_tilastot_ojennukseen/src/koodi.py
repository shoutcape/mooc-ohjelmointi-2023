# tee ratkaisusi tänne
import json

class Pelaaja:
    def __init__(self, name:str, nationality:str, assists:int, goals:int, penalties: int, team:str, games:int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.team = team
        self.games = games
        
    def __str__(self):
        return f"{self.name:<20}{self.team:>4}{self.goals:>4} +{self.assists:>3} = {self.goals + self.assists:>3}"



class ohjelma:
    def __init__(self):
        self.pelaajat = []
        self.name = "name"
        self.nationality = "nationality"
        self.assists = "assists"
        self.goals = "goals"
        self.team = "team"
        self.games = "games"
        
        
    
    def syota_tiedosto(self):
        tiedosto = input("tiedosto: ")
        with open (tiedosto, "r") as file:
            self.data  = file.read()
        self.pelaajatiedot = json.loads(self.data)
        print(f"luettiin {len(self.pelaajatiedot)} pelaajan tiedot")
        self.pelaajat_objektiksi()
        
    def lisaa_pelaaja(self, pelaaja):
        self.pelaajat.append(pelaaja)
        
    def pelaajat_objektiksi(self):
        for pelaaja in self.pelaajatiedot:
            self.lisaa_pelaaja(Pelaaja(pelaaja["name"],pelaaja["nationality"], pelaaja["assists"], pelaaja["goals"], pelaaja["penalties"], pelaaja["team"], pelaaja["games"]))
            
        
    def hae_pelaaja(self):
        self.nimi = input("nimi: ")
        # self.nimi = "Travis Zajac"
        for pelaaja in self.pelaajat:
            if pelaaja.name == self.nimi:
                print(pelaaja)
    
    def joukkueet(self):
        joukkue_lista = set([pelaaja.team for pelaaja in self.pelaajat])
        for joukkue in sorted(joukkue_lista):
            print(joukkue)
            
    def maat(self):
        maa_lista = set([pelaaja.nationality for pelaaja in self.pelaajat])
        for maa in sorted(maa_lista):
            print(maa)
            
    def pisteet_yht(self, pelaaja:tuple):
        return pelaaja.goals+pelaaja.assists
       
                        
    def joukkueen_pelaajat(self):
        joukkue = input("joukkue: ")
        jpelaajat = [pelaaja for pelaaja in self.pelaajat if pelaaja.team == joukkue]
        
        jpelaajat_jarjestyksessa = sorted(jpelaajat, key=self.pisteet_yht, reverse=True)
        
        for pelaaja in jpelaajat_jarjestyksessa:
            print(pelaaja)
            
            
    def maan_pelaajat(self):
        maa = input("maa: ")
        mpelaajat = [pelaaja for pelaaja in self.pelaajat if pelaaja.nationality == maa]
        mpelaajat_jarjestyksessa = sorted(mpelaajat, key=self.pisteet_yht, reverse=True)

        for pelaaja in mpelaajat_jarjestyksessa:
            print(pelaaja)
    
    def eniten_pisteita(self):
        maara = int(input("kuinka monta: "))
        pistejarjestyksessa = sorted(self.pelaajat, key=self.pisteet_yht, reverse=True)
        for i in range(maara):
            print(pistejarjestyksessa[i])
        
    def eniten_maaleja(self):
        maara= int(input("kuinka monta: "))
        maalijarjestyksessa = list(sorted(self.pelaajat, key=lambda pelaaja: (pelaaja.goals,-pelaaja.games), reverse=True))
        for i in range(maara):
            print(maalijarjestyksessa[i])
        
    def ohjeet(self):
        print('''
komennot:
0 lopeta
1 hae pelaaja
2 joukkueet
3 maat
4 joukkueen pelaajat
5 maan pelaajat
6 eniten pisteitä
7 eniten maaleja''')
        

        
        


    def suorita(self):
        self.syota_tiedosto()
        self.ohjeet()
        while True:
        
            komento = input("komento: ")
            if komento == "0":
                break
            if komento == "1":
                self.hae_pelaaja()
            if komento == "2":
                self.joukkueet()
            if komento == "3":
                self.maat()
            if komento == "4":
                self.joukkueen_pelaajat()
            if komento == "5":
                self.maan_pelaajat()
            if komento == "6":
                self.eniten_pisteita()
            if komento == "7":
                self.eniten_maaleja()
    
    
ohjelma().suorita()