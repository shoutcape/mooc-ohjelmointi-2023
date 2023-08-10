# TEE RATKAISUSI TÄHÄN:
class Lahja:
    def __init__(self, nimi: str, paino: int):
        self.paino = paino
        self.nimi = nimi
    
    def __str__(self):
        return f"{self.nimi} ({self.paino} kg)"
    
class Pakkaus:
    def __init__(self):
        self.lahjat = []
        
    def lisaa_lahja(self, lahja: Lahja):
        self.lahjat.append(lahja)

    def yhteispaino(self):
        yhteispaino = sum(lahja.paino for lahja in self.lahjat)
        return yhteispaino
        
    def __str__(self):
        return f"{self.yhteispaino()}"

if __name__ == "__main__":
    kirja = Lahja("Aapiskukko", 2)
    pakkaus = Pakkaus()
    pakkaus.lisaa_lahja(kirja)
    print(pakkaus.yhteispaino())
    cd_levy = Lahja("Pink Floyd: Dark side of the moon", 1)
    pakkaus.lisaa_lahja(cd_levy)
    print(pakkaus.yhteispaino())