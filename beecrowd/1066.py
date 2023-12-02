negativos = 0
negativos = int(negativos)
positivos = 0
positivos = int(positivos)
impar = 0
impar = int(impar)
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
else:
    impar = impar+1
if lista[1]%2 == 0:
    pares = pares+1
else:
    impar = impar+1
if lista[2]%2 == 0:
    pares = pares+1
else:
    impar = impar+1
if lista[3]%2 == 0:
    pares = pares+1
else:
    impar = impar+1
if lista[4]%2 == 0:
    pares = pares+1
else:
    impar = impar+1
if lista[0]>0:
    positivos = positivos+1
if lista[0]<0:
    negativos = negativos+1
if lista[1]>0:
    positivos = positivos+1
if lista[1]<0:
    negativos = negativos+1
if lista[2]>0:
    positivos = positivos+1
if lista[2]<0:
    negativos = negativos+1
if lista[3]>0:
    positivos = positivos+1
if lista[3]<0:
    negativos = negativos+1
if lista[4]>0:
    positivos = positivos+1
if lista[4]<0:
    negativos = negativos+1
print(f"{pares} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")