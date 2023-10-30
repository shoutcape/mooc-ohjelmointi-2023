# TEE RATKAISUSI TÄHÄN:

def parilliset(alku: int, maksimi: int):
    if alku % 2 != 0:
        alku+= 1
    while alku <= maksimi:
        yield alku
        alku += 2


if __name__ == "__main__":
    luvut = parilliset(1, 10)
    for luku in luvut:
        print(luku)