#https://www.w3schools.com/python/python_lists.asp
#toda lista começa e termina com colchetes
#crio uma lista vazia
lista = []
print(lista)

#coloco valores dentro da lista
lista = ["O carro", "abacaxi", 123, 5.5]
print(lista)

#coloco uma lista dentro da outra
nova_lista = ["turing", lista]
print(nova_lista)

#acesso um determinado índice(valor) da lista OBS:o primeiro índice é 0
print(lista[2])

#acessar uma lista dentro de outra lista
print(nova_lista[1][2])
#1 -> acessa o índice 1(lista) 2 -> acessa o índice 2 de lista(abacaxi) 
#OBS: caso o primeiro índice seja uma string será acessado o respectivo caractere

#juntar duas listas em uma só
lista_2 = [1, 4, -7]
listao = lista + lista_2
print(listao)

#multiplicar uma lista por um valor
listao = lista * 3
print(listao)

#mostro quantos itens tem na lista
print(len(lista))

#verificar se determinado item está na lista
print("abacaxi" in lista)

#verificar se determinado item não está na lista
print("banana" in lista)

#adiciona um item a lista
lista.append("item")
print(lista)

#remove um item da lista
lista.remove("item")
print(lista)

#acessa uma sequência de itens da lista
print(lista[0:3])
#nesse caso será acessa do índice zero até o índice 2

#mudo o formato de um item específico
lista[2] = int(lista[2])

#ordena a lista em ordem crescente
sorted(lista)

#reverte a lista
print(reversed(lista))