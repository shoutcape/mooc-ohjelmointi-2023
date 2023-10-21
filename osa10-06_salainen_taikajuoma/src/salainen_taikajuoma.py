# TEE RATKAISUSI TÄHÄN:
class Taikajuoma:
    def __init__(self, nimi: str):
        self._nimi = nimi
        self._ainekset = []

    def lisaa_aines(self, ainesosa: str, maara: float):
        self._ainekset.append((ainesosa, maara))

    def tulosta_resepti(self):
        print(self._nimi + ":")
        for aines in self._ainekset:
            print(f"{aines[0]} {aines[1]} grammaa")
            
            
class SalainenTaikajuoma(Taikajuoma):
    def __init__(self, nimi: str, salasana: str):
        super().__init__(nimi)
        self.salasana = salasana
        
    def salasana_oikein(self, salasana: str):
        if self.salasana == salasana:
            return True
        else:
            raise(ValueError("Väärä salasana!"))
        
    def lisaa_aines(self, ainesosa: str, maara: float, salasana: str):
        if self.salasana_oikein(salasana):
            super().lisaa_aines(ainesosa, maara)

    def tulosta_resepti(self, salasana: str):
        if self.salasana_oikein(salasana):
            super().tulosta_resepti()
                
    

if __name__ == "__main__":
    kutistus = SalainenTaikajuoma("Kutistus maksimus", "hokkuspokkus")
    kutistus.lisaa_aines("Kärpässieni", 1.5, "hokkuspokkus")
    kutistus.lisaa_aines("Taikahiekka", 3.0, "hokkuspokkus")
    kutistus.lisaa_aines("Sammakonkutu", 4.0, "hokkuspokkus")
    kutistus.tulosta_resepti("hokkuspokkus")

    kutistus.tulosta_resepti("pokkushokkus") # VÄÄRÄ SALASANA!