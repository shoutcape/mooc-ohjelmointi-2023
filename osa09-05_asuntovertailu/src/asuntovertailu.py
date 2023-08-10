# TEE RATKAISUSI TÄHÄN:

class Asunto:
    def __init__(self, huoneita: int, nelioita: int, neliohinta: int):
        self.huoneita = huoneita
        self.nelioita = nelioita
        self.neliohinta = neliohinta
        
    def suurempi(self, verrattava):
        if self.nelioita >= verrattava.nelioita:
            return True
        return False
    
    def hintaero(self, verrattava):
        ero = abs(self.neliohinta*self.nelioita - verrattava.neliohinta*verrattava.nelioita)
        return ero
    
    def kalliimpi(self, verrattava):
        ero = self.neliohinta*self.nelioita > verrattava.neliohinta * verrattava.nelioita
        return ero > 0
        
        
if __name__ == "__main__":
    eira_yksio = Asunto(1, 16, 5500)
    kallio_kaksio = Asunto(2, 38, 4200)
    jakomaki_kolmio = Asunto(3, 78, 2500)

    print(eira_yksio.kalliimpi(kallio_kaksio))
    print(jakomaki_kolmio.kalliimpi(kallio_kaksio))