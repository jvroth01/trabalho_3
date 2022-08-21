import time

i = 0
y = 0
fila = []
start = time.time()

while i <= 9999999:       # adciona a fila os valores e soma os mesmos
    i = i + 1
    fila.append(i)
    y = y + i

z = 999999
while z < 999999:        # percorre a fila no sentido contrario
    z = z - 1
    fila[z]

end = time.time()

print("Soma dos valores = ",y)
print(end - start, "segundos")

def adcionar(fila):
    print("Qual valor deseja adcionar a fila? ")
    valor = int(input())
    fila.append(valor)
    print(fila)

def remover(fila):
    print("Qual valor deseja remover da fila? ")
    valor = int(input())
    for i in range(len(fila)):
        if fila[i] == valor:
            while len(fila) > i:
                fila.pop()
            break
        else:
            i = i - 1
    print(fila)

def buscar(fila):
    print("Qual valor deseja buscar na lista?")
    valor = int(input())
    for i in range(len(fila)):
        i = i + 1
        if fila[i] == valor:
            print("O valor esta em ", "fila[", i, "]")
            break
        else:
            i = i + 1

fila1 = fila[]

