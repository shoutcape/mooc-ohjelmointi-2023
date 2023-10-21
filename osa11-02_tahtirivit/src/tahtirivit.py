# TEE RATKAISUSI TÄHÄN:
def tahtirivit(luvut: list):
    return [luku * "*" for luku in luvut]
    
    
if __name__ == "__main__":
    rivit = tahtirivit([1,2,3,4])
    for rivi in rivit:
        print(rivi)

    print()

    rivit = tahtirivit([4, 3, 2, 1, 10])
    for rivi in rivit:
        print(rivi)