# Tee ratkaisusi tähän:
class Tavara:
    def __init__(self, nimi: str, paino: int):
        self.__nimi = nimi
        self.__paino = paino
        
    def nimi(self):
        return self.__nimi

    def paino(self):
        return self.__paino
    
    def __str__(self):
        return f"{self.__nimi} ({self.__paino} kg)"
    
    
class Matkalaukku:
    def __init__(self, maksimipaino: int):
        self.__maksimipaino = maksimipaino
        self.__tavarat = [] #Lista, jotta voidaan varastoida eri arvot jotka tavarat sisältävät
        self.__yhteispaino = 0
        
    def paino(self):
        return self.__yhteispaino
    
    def lisaa_tavara(self, tavara: Tavara):
        if self.__yhteispaino + tavara.paino() <= self.__maksimipaino:
            self.__tavarat.append(tavara)  # Lisätään tavara listalle
            self.__yhteispaino += tavara.paino()  # Päivitetään yhteispaino
            
    def tulosta_tavarat(self):
        for tavara in self.__tavarat:
            print(f"{tavara.nimi()} ({tavara.paino()} kg)")
            
    
    def raskain_tavara(self):
        raskain = None
        for tavara in self.__tavarat:
            if raskain == None or tavara.paino() > raskain.paino():
                raskain = tavara
        return raskain
        
            
    def __str__(self):
        if len(self.__tavarat) == 1:
            return f"{len(self.__tavarat)} tavara ({self.__yhteispaino} kg)"
        return f"{len(self.__tavarat)} tavaraa ({self.__yhteispaino} kg)"

class Lastiruuma:
    def __init__(self, maksimipaino: int):
        self.__maksimipaino = maksimipaino
        self.__matkalaukut = []
        self.__yhteispaino = 0

    
    def lisaa_matkalaukku(self, matkalaukku: Matkalaukku):
        if self.__yhteispaino + matkalaukku.paino() <= self.__maksimipaino:
            self.__matkalaukut.append(matkalaukku)  # Lisätään matkalaukku listalle
            self.__yhteispaino += matkalaukku.paino()  # Päivitetään yhteispaino
            
    def tulosta_tavarat(self):
        for matkalaukku in self.__matkalaukut:
            matkalaukku.tulosta_tavarat()
            
    def __str__(self):
        sana = "matkalaukkua"
        if len(self.__matkalaukut) == 1:
            sana = "matkalaukku"
        return f"{len(self.__matkalaukut)} {sana}, tilaa {self.__maksimipaino - self.__yhteispaino} kg"
        

if __name__ == "__main__":
    
    ruuma = Lastiruuma(100)
    laukku = Matkalaukku(25)
    tavara = Tavara("Aapiskukko", 2)
    laukku.lisaa_tavara(tavara)
    ruuma.lisaa_matkalaukku(laukku)




