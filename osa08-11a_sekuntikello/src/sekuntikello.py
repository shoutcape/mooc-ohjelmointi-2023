# Tee ratkaisusi tähän:
class Sekuntikello:
    def __init__(self):
        self.sekunnit = 0
        self.minuutit = 0

    def tick(self):
        self.sekunnit += 1
        
        if self.sekunnit == 60:
            self.sekunnit = 0
            self.minuutit += 1
            if self.minuutit == 60:
                self.minuutit = 0
        
    def __str__(self):
        return f"{self.minuutit:02d}:{self.sekunnit:02d}"

            


if __name__ == "__main__":
    kello = Sekuntikello()
    for i in range(61):
        print(kello)
        kello.tick()