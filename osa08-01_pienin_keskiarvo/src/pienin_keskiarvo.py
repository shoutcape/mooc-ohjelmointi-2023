def keskiarvo(henkilo: dict):
    summa = henkilo["tulos1"] + henkilo["tulos2"] + henkilo["tulos3"]
    return summa / 3


def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
    pienin = 0
    for henkilo in [henkilo1, henkilo2, henkilo3]:
        if keskiarvo(henkilo) < pienin or pienin == 0:
            pienin = keskiarvo(henkilo)
            henkilo_nimi = henkilo
            
    return henkilo_nimi

if __name__ == "__main__":
    henkilo1 = {"nimi": "Keijo", "tulos1": 4, "tulos2": 3, "tulos3": 4}
    henkilo2 = {"nimi": "Reijo", "tulos1": 4, "tulos2": 2, "tulos3": 4}
    henkilo3 = {"nimi": "Veijo", "tulos1": 4, "tulos2": 3, "tulos3": 4}

    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))