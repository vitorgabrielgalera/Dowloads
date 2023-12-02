lista = ["Ameixa", "Abacaxi", "Caqui", "Banana", "Maçã"]
x = input("digite uma fruta: ")
if x in lista:
    lista.remove(x)
    print(lista)