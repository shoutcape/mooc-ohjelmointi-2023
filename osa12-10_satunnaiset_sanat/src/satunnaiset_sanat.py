# TEE RATKAISUSI TÄHÄN:

def sanageneraattori(kirjaimet: str, pituus: int, maara: int):
    return (kirjaimet[i:i+pituus] for i in range(maara))


if __name__ == "__main__":
    sanagen = sanageneraattori("abcdefg", 2, 5)
    for sana in sanagen:
        print(sana)