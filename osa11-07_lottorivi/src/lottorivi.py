# TEE RATKAISUSI TÄHÄN:
class Lottorivi:
    def __init__(self,kierros: int, luvut: list):
        self.kierros = kierros
        self.luvut = luvut
        
    def osumat_paikoillaan(self, pelattu_rivi: list):
        return [osuma if osuma in self.luvut else -1 for osuma in pelattu_rivi]
        
    def osumien_maara(self, pelattu_rivi: list):
        return sum([1 for osuma in pelattu_rivi if osuma == osuma in self.luvut])
    
    
if __name__ == "__main__":
    oikea = Lottorivi(8, [1,2,3,10,20,30,33])
    oma_rivi = [1,4,7,10,11,20,30]
    print(oikea.osumien_maara(oma_rivi))
    print(oikea.osumat_paikoillaan(oma_rivi))
