# tee ratkaisusi tänne

class kurssit:
    def __init__(self, kurssi):
        self.__kurssi = kurssi
        self.__arvosana = None
        self.__opintopisteet = None

    def kurssi(self):
        return self.__kurssi
    def arvosana(self):
        return self.__arvosana
    def opintopisteet(self):
        return self.__opintopisteet
            
    def lisaa_arvosana(self, arvosana: int):
        if self.__arvosana == None or self.__arvosana <= arvosana:
            self.__arvosana = arvosana
        
    def lisaa_opintopisteet(self, opintopisteet: int):
        self.__opintopisteet = opintopisteet
        

class suoritukset:
    def __init__(self):
        self.kurssit = {}
        
    def lisaa_suoritus(self,kurssi:str, arvosana: int, opintopisteet:int):
        if not kurssi in self.kurssit:
            self.kurssit[kurssi] = kurssit(kurssi)
        self.kurssit[kurssi].lisaa_arvosana(arvosana)
        self.kurssit[kurssi].lisaa_opintopisteet(opintopisteet)
        
    def hae_suoritus(self, kurssi:str):
        if not kurssi in self.kurssit:
            return None
        return self.kurssit[kurssi]
    
    def hae_kaikki(self):
        return self.kurssit
    

class sovellus:
    def __init__(self):
        self.__suoritukset = suoritukset()

    def ohjeet(self):
        print("komennot: ")
        print("1 lisää suoritus")
        print("2 hae suoritus")
        print("3 tilastot")
        print("0 lopetus")
        
    def lisaa_suoritus(self):
        kurssi = input("kurssi: ")
        arvosana = int(input("arvosana: "))
        opintopisteet = int(input("opintopisteet: "))
        self.__suoritukset.lisaa_suoritus(kurssi, arvosana, opintopisteet)
        
        
    def haku(self):
        kurssi = input("kurssi: ")
        suoritus = self.__suoritukset.hae_suoritus(kurssi)
        if suoritus == None:
            print("ei suoritusta")
            return
        arvosana = suoritus.arvosana()
        opintopisteet = suoritus.opintopisteet()
        print(f"{kurssi} ({opintopisteet} op) arvosana {arvosana}")
            
    def tilastot(self):
        suoritukset = self.__suoritukset.hae_kaikki()
        suoritusten_maara = (len(suoritukset))
        yhtarvosanat = 0
        yhtopintopisteet = 0
        arvosanat = []
        arvosanalaskuri = {}
        
        for kurssi, tulokset in suoritukset.items():
            yhtarvosanat += tulokset.arvosana()
            arvosanat.append(tulokset.arvosana())
            if tulokset.arvosana() in arvosanalaskuri:
                arvosanalaskuri[tulokset.arvosana()] += 1
            else:
                arvosanalaskuri[tulokset.arvosana()] = 1
            yhtopintopisteet += tulokset.opintopisteet()
            
        keskiarvo = yhtarvosanat/suoritusten_maara
        
        print(f"suorituksia {suoritusten_maara} kurssilta, yhteensä {yhtopintopisteet} opintopistettä")
        print(f"keskiarvo {keskiarvo:.1f}")
        print("arvosanajakauma")
        
        
        for arvosana in range(5,0, -1):
            print(f"{arvosana}: {'x' * arvosanalaskuri.get(arvosana, 0)}")
            
        
    def main(self):
        self.ohjeet()
        while True:
            print(" ")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.lisaa_suoritus()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.tilastot()
            else:
                self.ohjeet()


ohjelma = sovellus()
ohjelma.main()
    
