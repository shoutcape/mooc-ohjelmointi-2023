# TEE RATKAISUSI TÄHÄN:
class Raha:
    def __init__(self, eurot: int, sentit: int):
        self.__eurot = eurot
        self.__sentit = sentit

    def __str__(self):
        return f"{self.__eurot}.{self.__sentit:02d} eur"

    
    def __arvo(self):
        #muunnetaan eurot senteiksi.
        return self.__eurot * 100 + self.__sentit
    
    def __aseta_arvo(self, sentteja:int):
        self.__eurot = sentteja // 100
        self.__sentit = sentteja - self.__eurot * 100
        
    def __eq__(self, toinen: int):
        return self.__arvo() == toinen.__arvo()
    
    def __gt__(self, toinen:int):
        return self.__arvo() > toinen.__arvo()
    
    def __lt__(self, toinen:int):
        return self.__arvo() < toinen.__arvo()
        
    
    def __ne__(self, toinen:int):
        return self.__arvo() != toinen.__arvo()
        
        

    def __add__(self, toinen:int):
        summa = Raha(0,0)
        summa.__aseta_arvo(self.__arvo() + toinen.__arvo())
        return summa
        
            
    def __sub__(self,toinen:int):
        erotus = self.__arvo() - toinen.__arvo()
        if erotus < 0:
            raise ValueError
        erotus = Raha(0,0)
        erotus.__aseta_arvo(self.__arvo() - toinen.__arvo())
        return erotus
        

if __name__ == "__main__":
    e1 = Raha(4, 5)
    e2 = Raha(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

