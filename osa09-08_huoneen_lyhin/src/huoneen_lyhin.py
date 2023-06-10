# TEE RATKAISUSI TÄHÄN:
class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return self.nimi
