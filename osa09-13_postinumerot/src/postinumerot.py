# Lisää allaolevaan luokkaan pyydetyt ominaisuudet:

class Kaupunki:
    def __init__(self, nimi: str, asukasluku: int):
        self.__nimi = nimi
        self.__asukasluku = asukasluku

    @property
    def nimi(self):
        return self.__nimi

    @property
    def asukasluku(self):
        return self.__asukasluku

    def __str__(self):
        return f"{self.__nimi} ({self.__asukasluku} as.)"
