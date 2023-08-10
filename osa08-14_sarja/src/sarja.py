# Tee ratkaisusi tähän:
class Sarja:
    def __init__(self, nimi: str, kaudet: int, genret: list):
        self.nimi = nimi
        self.kaudet = kaudet
        self.genret = genret
        self.arvostelut = []
        self.arvosana = 0
        
    def arvostele(self, arvosana:int):
        self.arvostelut.append(arvosana)
        self.arvostelu_keskiarvo = sum(self.arvostelut)/len(self.arvostelut)
        
            
    def __str__(self):
        lista = self.genret
        merkkijono = ", ".join(lista)
        if len(self.arvostelut) > 0:
            return f"{self.nimi} ({self.kaudet} esityskautta)\ngenret: {merkkijono}\narvosteluja {len(self.arvostelut)}, keskiarvo {self.arvostelu_keskiarvo:.1f} pistettä"
        return f"{self.nimi} ({self.kaudet} esityskautta)\ngenret: {merkkijono}\nei arvosteluja"
    
    
    
def arvosana_vahintaan(arvosana: float, sarjat: list):
    nimet = []
    for sarja in sarjat:
        if sarja.arvostelu_keskiarvo >= arvosana:
            nimet.append(sarja)
    return nimet
    

def sisaltaa_genren(genre: str, sarjat: list):
    nimet = []
    for sarja in sarjat:
        if genre in sarja.genret:
            nimet.append(sarja)
    return nimet


if __name__ == "__main__":
    s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.arvostele(5)

    s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
    s2.arvostele(3)

    s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
    s3.arvostele(2)

    sarjat = [s1, s2, s3]

    print("arvosana vähintään 4.5:")
    for sarja in arvosana_vahintaan(4.5, sarjat):
        print(sarja)

    print("genre Comedy:")
    for sarja in sisaltaa_genren("Comedy", sarjat):
        print(sarja)