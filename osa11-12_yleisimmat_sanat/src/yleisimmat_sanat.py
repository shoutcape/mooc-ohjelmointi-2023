# TEE RATKAISUSI TÄHÄN:
from string import punctuation

def yleisimmat_sanat(tiedoston_nimi: str, raja: int):
    with open(tiedoston_nimi) as f:
        sanat = f.read()
        
        sanat = sanat.replace("\n", " ")
        for erikoismerkki in punctuation:
            sanat = sanat.replace(erikoismerkki, "")
    
        sanat = sanat.split()
        return{sana: sanat.count(sana) for sana in sanat if sanat.count(sana) >= raja}
    
    



if __name__ == "__main__":
    print(yleisimmat_sanat("comprehensions.txt", 3))