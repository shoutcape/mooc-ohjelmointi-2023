# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        self.lukuja = 0
        self.yhteensa = 0

    def lisaa_luku(self, luku:int):
        self.lukuja += 1
        self.yhteensa += luku
        
    def lukujen_maara(self):
        return self.lukuja
    
    def summa(self):
        return self.yhteensa

    def keskiarvo(self):
        if self.lukuja == 0:
            pass
        else:
            return self.yhteensa/self.lukuja

tilasto = Lukutilasto()
parilliset = Lukutilasto()
parittomat = Lukutilasto()
while True:
    luku = int(input("Anna lukuja: \n"))
    if luku == -1:
        break
    if luku % 2 == 0:
        parilliset.lisaa_luku(luku)
    else:
        parittomat.lisaa_luku(luku)
    tilasto.lisaa_luku(luku)
    
print("Lukujen määrä:", tilasto.lukujen_maara())
print("Summa:", tilasto.summa())
print("Keskiarvo:", tilasto.keskiarvo())
print("Parillisten summa:", parilliset.summa())
print("Parittomien summa:", parittomat.summa())

