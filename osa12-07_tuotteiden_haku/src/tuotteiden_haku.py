# TEE RATKAISUSI TÄHÄN:

def hae(tuotteet: list, kriteeri: callable):
    return [tuote for tuote in tuotteet if kriteeri(tuote)]
    

if __name__ == "__main__":
    tuotteet = [("banaani", 5.95, 12), ("omena", 3.95, 3), ("appelsiini", 4.50, 2), ("vesimeloni", 4.95, 22), ("Kaali", 0.99, 1)]
    for tuote in hae(tuotteet, lambda t: t[1]<4):
        print(tuote)