# Tee ratkaisusi tähän:

class Kello:
    def __init__(self, tunnit: int, minuutit:int, sekunnit:int):
        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = sekunnit
        
    def tick(self):
        self.sekunnit += 1
        if self.sekunnit == 60:
            self.sekunnit = 0
            self.minuutit += 1
            if self.minuutit == 60:
                self.minuutit = 0
                self.tunnit += 1
                if self.tunnit == 24:
                    self.tunnit = 0
                    
    def aseta(self, tunnit: int, minuutit:int):
        self.tunnit = tunnit
        self.minuutit = minuutit
        self.sekunnit = 0
              
    def __str__(self):
        return f"{self.tunnit:02d}:{self.minuutit:02d}:{self.sekunnit:02d}"
                
                
if __name__ == "__main__":
    kello = Kello(23, 59, 55)
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)
    kello.tick()
    print(kello)

    kello.aseta(12, 5)
    print(kello)