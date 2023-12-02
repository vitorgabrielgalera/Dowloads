a = int(int(input()))
print (int(a))
nota_100 = a//100
a = a % 100
nota_50 = a//50
a = a % 50
nota_20 = a//20
a = a % 20
nota_10 = a//10
a = a % 10
nota_5 = a//5
a = a % 5
nota_2 = a//2
nota_1 = a % 2
print(nota_100,"nota(s) de R$ 100,00")
print(nota_50,"nota(s) de R$ 50,00")
print(nota_20,"nota(s) de R$ 20,00")
print(nota_10,"nota(s) de R$ 10,00")
print(nota_5,"nota(s) de R$ 5,00")
print(nota_2,"nota(s) de R$ 2,00")
print(nota_1,"nota(s) de R$ 1,00")