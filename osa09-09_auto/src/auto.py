# TEE RATKAISUSI TÄHÄN:
class Auto:
    
    def __init__(self):
        self.__tankki = 0
        self.__ajettu = 0
        
    def tankkaa(self):
        self.__tankki = 60
    
    def aja(self, km: int):
        if km <= self.__tankki:
            self.__tankki -= km   
            self.__ajettu += km
        
        else:
            self.__ajettu += self.__tankki    
            self.__tankki = 0
    
    def __str__(self):
        return f"Auto: ajettu {self.__ajettu} km, bensaa {self.__tankki} litraa"
    
    
    
    
    
if __name__ == "__main__":
    
    auto = Auto()
    print(auto)
    auto.tankkaa()
    print(auto)
    auto.aja(20)
    print(auto)
    auto.aja(50)
    print(auto)
    auto.aja(10)
    print(auto)
    auto.tankkaa()
    auto.tankkaa()
    print(auto)