import time
import random

y = 0

def adcionar(fila):
    fila.append(random.randint(1,100000))
    return fila

def remover(fila):
    fila.pop(0)
    return fila

def buscar(fila):
    valor = random.randint(1,10000) #prof, aqui deixei o aleatorio entre esses valores menores pois se o intervalo fosse muito grande o tempo de execucao ficava muito longo

    print("Buscar valor = ", valor)
    for i in range(len(fila)):
        if fila[i] == valor:
            print("O valor esta em ", "'fila[", i, "]'")
            i = i + 1
            if fila[-1] == valor:
                    print("O valor tambem esta em ", "fila[", 999999 , "]'")
            break
        if valor not in fila:
            print("o valor", valor, "nao se encontra na fila")
            break
    return fila

contador = 0
tempo = 0
tempo1 = 0
while contador < 50:
    start = time.time()
    fila = []
    i = 0

    while i <= 999999:  # adciona a fila os valores e soma os mesmos
        i = i + 1
        fila.append(i)
        y = y + i

    z = 999999
    while z < 999999:  # percorre a fila no sentido contrario
        z = z - 1
        fila[z]
    
    end = time.time()

    adcionar(fila)
    remover(fila)
    buscar(fila)
   
    end = time.time()

    print("Tempo usado na operacao = ", end - start, " segundos")

    tempo = end - start
    tempo1 = tempo1 + tempo
    contador = contador + 1
    print(contador)

    print("------------------------------")

media = (tempo1)/50
print("Tempo total ", tempo1, " segundos")
print("Tempo medio = ", media)
