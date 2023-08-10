# TEE RATKAISUSI TÄHÄN:


class Aanite:
    
    def __init__(self, pituus: int):
        if pituus >= 0:
            self.__pituus = pituus
        else:
            raise ValueError()

    @property
    def pituus(self):
        return self.__pituus
        
        
    @pituus.setter
    def pituus(self, pituus):
        if pituus >= 0:
            self.__pituus = pituus
        else:
            raise ValueError()
    
if __name__ == "__main__":
    the_wall = Aanite(-1)
    print(the_wall.pituus)
    the_wall.pituus = 44
    print(the_wall.pituus)