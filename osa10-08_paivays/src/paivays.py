# TEE RATKAISUSI TÄHÄN:

class Paivays:
    def __init__(self, pv: int, kk: int, v: int):
        self.pv = pv
        self.kk = kk
        self.v = v
        
    def __str__(self):
        return f"{self.pv}.{self.kk}.{self.v}"

        
    def paiviksi(self):
        return self.pv + self.kk*30 + self.v*360
    
    def takaisin(self, paivat):
        kk = paivat//30
        vuodet = kk //12
        paivat -= kk * 30
        kk -= vuodet * 12
        return Paivays(paivat, kk, vuodet)
        
        
    def __lt__(self, toinen):
        return self.paiviksi() < toinen.paiviksi()
        
    def __gt__(self, toinen):
        return self.paiviksi() > toinen.paiviksi()
    
    def __eq__(self, toinen):
        return self.paiviksi() == toinen.paiviksi()
    
    def __ne__(self, toinen):
        return self.paiviksi() != toinen.paiviksi()
        
    def __add__(self, lisays):
        return self.takaisin(self.paiviksi() + lisays)
    
    def __sub__(self, vahennys):
        erotus = abs(self.paiviksi() - vahennys.paiviksi())
        return erotus
    
if __name__ == "__main__":
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(2, 11, 2020)
    p3 = Paivays(30, 12, 1985)

    print(p2-p1)
    print(p1-p2)
    print(p1-p3)
    