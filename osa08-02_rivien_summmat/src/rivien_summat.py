# tee ratkaisu tänne
def rivien_summat(matriisi: list):
    for lista1 in matriisi:
        lista1.append(sum(lista1))
    
if __name__ == "__main__":
    
    matriisi = [[1,2],[3,4]]
    rivien_summat(matriisi)
    print(matriisi)