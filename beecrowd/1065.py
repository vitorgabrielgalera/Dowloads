pares = 0
pares = int(pares)
lista = []
lista.append(int(int(input())))
lista.append(int(int(input())))
lista.append(int(int(input())))
lista.append(int(int(input())))
lista.append(int(int(input())))
if lista[0]%2 == 0:
    pares = pares+1
if lista[1]%2 == 0:
    pares = pares+1
if lista[2]%2 == 0:
    pares = pares+1
if lista[3]%2 == 0:
    pares = pares+1
if lista[4]%2 == 0:
    pares = pares+1
print(f"{pares} valores pares")