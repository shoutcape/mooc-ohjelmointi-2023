# TEE RATKAISUSI TÄHÄN:
class ListaApuri:

    @classmethod
    def suurin_frekvenssi(cls, lista: list):
        if not lista:
            return None
        
        # Count the frequency of each element in the list
        sanakirja = {}
        for elementti in lista:
            if elementti in sanakirja:
                sanakirja[elementti] += 1
            else:
                sanakirja[elementti] = 1
        
        # Find the element(s) with the highest frequency
        esiintyvyys = max(sanakirja.values())
        esiintyva_numero = [elementti for elementti, luku in sanakirja.items() if luku == esiintyvyys]
        
        # Return the element(s) with the highest frequency
        
        return esiintyva_numero[0]
                    
        
    @classmethod
    def tuplia(cls, lista:list):
        esiintyvyys = {}
        for numero in lista:
            if numero in esiintyvyys:
                esiintyvyys[numero] += 1
            else:
                esiintyvyys[numero] = 1
            
        parit = 0
        for numero in esiintyvyys:
            if esiintyvyys[numero] >= 2:
                parit += 1
                
        return parit

    
if __name__ == "__main__":
    luvut = [1, 1, 1, 2, 2, 3]
    print(ListaApuri.suurin_frekvenssi(luvut))
    print(ListaApuri.tuplia(luvut))