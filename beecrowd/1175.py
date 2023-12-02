lista = []
for i in range(20):
    a = int(input())
    lista.append(a)
lista = list(reversed(lista))
for i in range(20):
    print(f"N[{i}] = {lista[i]}")