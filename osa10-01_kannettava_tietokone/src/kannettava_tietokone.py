# TEE RATKAISUSI TÄHÄN:
class Tietokone:
    def __init__(self, malli: str, nopeus: int):
        self.__malli = malli
        self.__nopeus = nopeus

    @property
    def malli(self):
        return self.__malli

    @property
    def nopeus(self):
        return self.__nopeus
