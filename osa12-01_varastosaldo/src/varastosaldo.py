# TEE RATKAISUSI TÄHÄN:
def jarjesta_varastosaldon_mukaan(alkiot: list):
    def palauta_arvo(arvo: int):
        return arvo[2]
    
    return sorted(alkiot, key= palauta_arvo)




if __name__ == "__main__":
    tuotteet = [("banaani", 5.95, 12), ("omena", 3.95, 3), ("appelsiini", 4.50, 2), ("vesimeloni", 4.95, 22)]

    for tuote in jarjesta_varastosaldon_mukaan(tuotteet):
        print(f"{tuote[0]} {tuote[2]} kpl")