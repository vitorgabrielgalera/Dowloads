#https://www.w3schools.com/python/python_for_loops.asp
#o comando while funciona como ou if, com o diferencial que ele irá repetir o que está identado até que a condição seja falsa
i = 0
while i < 6:
    print(i)
    i += 1
#OBS: sempre que utilizar o while cuidar para não criar um loop infinito 

#o comando break é utilizado para forçar uma parada no loop
i = 0
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# o comando continue faz com que o loop volte do inicio
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#o else efetuará o comando quando a condição for falsa
i = 0
while i < 6:
    print(i)
    i += 1
else:
    print("o número não é menor que 6")

#https://www.w3schools.com/python/python_for_loops.asp
#o comando for irá repetir um comando o número de vezes de itens que eu tenho em uma lista
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

#o for também funciona em strings
for x in "banana":
  print(x)

#o break funciona da mesma maneira no for
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#o continue funciona da mesma maneira no for
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#A função range() retorna uma sequência de números, começando em 0 por padrão e incrementando em 1
for x in range(2, 6):
  print(x)

#é possível especificar o valor do incremento adicionando um terceiro parâmetro
for x in range(2, 30, 3):
  print(x)

