# TEE RATKAISUSI TÄHÄN:
class Raha:
    def __init__(self, eurot: int, sentit: int):
        self.eurot = eurot
        self.sentit = sentit

    def __str__(self):
        return f"{self.eurot}.{self.sentit}"
