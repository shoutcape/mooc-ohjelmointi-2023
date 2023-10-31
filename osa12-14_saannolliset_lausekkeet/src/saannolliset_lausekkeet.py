# TEE RATKAISUSI TÄHÄN:
import re

def on_viikonpaiva(merkkijono: str):
    return re.search("ma|ti|ke|to|pe|la|su", merkkijono) is not None

def kaikki_vokaaleja(merkkijono: str):
    return re.search("^[aeiouyäöå]*$",merkkijono) is not None

def kellonaika(merkkijono: str):
    return re.search("^([0-1][0-9]|2[0-3])\:[0-5][0-9]\:[0-5][0-9]$",merkkijono) is not None
 

if __name__ == "__main__":
    print(kellonaika("12:43:01"))
    print(kellonaika("AB:01:CD"))
    print(kellonaika("17:59:59"))
    print(kellonaika("29:36:49"))