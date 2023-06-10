# TEE RATKAISUSI TÄHÄN:

class Maksukortti:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def lataa_rahaa(self, lisays: float):
        self.saldo += lisays

    def ota_rahaa(self, maara: float):
        pass
        # Toteuta metodi siten, että se ottaa kortilta rahaa vain, jos saldoa riittää
        # Onnistuessaan metodi palauttaa True ja muuten False

class Kassapaate:
    def __init__(self):
        # kassassa on aluksi 1000 euroa rahaa
        self.rahaa = 1000
        self.edulliset = 0
        self.maukkaat = 0

    def syo_edullisesti(self, maksu: float):
        # Edullinen lounas maksaa 2.50 euroa
        # Kasvatetaan kassan rahamäärää edullisen lounaan hinnalla ja palautetaan vaihtorahat
        # Jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan
        pass

    def syo_maukkaasti(self, maksu: float):
        # Maukas lounas maksaa 4.30 euroa
        # Kasvatetaan kassan rahamäärää maukkaan lounaan hinnalla ja palautetaan vaihtorahat
        # Jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan
        pass

    def syo_edullisesti_kortilla(self, kortti:Maksukortti):
        # Edullinen lounas maksaa 2.50 euroa
        # Jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
        # Muuten palautetaan False
        pass

    def syo_maukkaasti_kortilla(self, kortti:Maksukortti):
        # Maukas lounas maksaa 4.30 euroa
        # Jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
        # Muuten palautetaan False
        pass

    def lataa_rahaa_kortille(self, kortti: Maksukortti, summa: float):
        pass
