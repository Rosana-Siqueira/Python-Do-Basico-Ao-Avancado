contP = 0
contI = 0

def contaPares(lista):
    global contP
    for num in lista:
        if num % 2 == 0:
            contP += 1
        return contP
    
def contaImpares(lista):
    global contI
    for num in lista:
        if num % 2 == 1:
            contI += 1
        return contI



