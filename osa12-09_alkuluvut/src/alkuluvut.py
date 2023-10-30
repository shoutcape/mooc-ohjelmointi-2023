# TEE RATKAISUSI TÄHÄN:

def alkuluvut():
    x = 2
    while True:
        if on_alkuluku(x):
            yield x
        x += 1
        
def on_alkuluku(luku: int):
    for y in range(2, luku):
        if luku % y == 0:
            return False
        return True
    
    
if __name__ == "__main__":
    luvut = alkuluvut()
    for i in range(8):
        print(next(luvut))