a = float(input())
print("NOTAS:")
nota_100 = a//100
nota_100 = int(nota_100)
a = a % 100
nota_50 = a//50
nota_50 = int(nota_50)
a = a % 50
nota_20 = a//20
nota_20 = int(nota_20)
a = a % 20
nota_10 = a//10
nota_10 = int(nota_10)
a = a % 10
nota_5 = a//5
nota_5 = int(nota_5)
a = a % 5
nota_2 = a//2
nota_2 = int(nota_2)
a = a % 2
nota_01 = a//1
nota_01 = int(nota_01)
a = a % 1
nota_050 = a//0.5
nota_050 = int(nota_050)
a = a % 0.5
nota_025 = a//0.25
nota_025 = int(nota_025)
a = a % 0.25
nota_010 = a//0.10
nota_010 = int(nota_010)
a = a % 0.10
nota_05 = a//0.05
nota_05 = int(nota_05)
a = a % 0.05
nota_001 = a//0.01
nota_001 = int(nota_001)
print(nota_100,"nota(s) de R$ 100.00")
print(nota_50,"nota(s) de R$ 50.00")
print(nota_20,"nota(s) de R$ 20.00")
print(nota_10,"nota(s) de R$ 10.00")
print(nota_5,"nota(s) de R$ 5.00")
print(nota_2,"nota(s) de R$ 2.00")
print("MOEDAS:")
print(nota_01,"moeda(s) de R$ 1.00")
print(nota_050,"moeda(s) de R$ 0.50")
print(nota_025,"moeda(s) de R$ 0.25")
print(nota_010,"moeda(s) de R$ 0.10")
print(nota_05,"moeda(s) de R$ 0.05")
print(nota_001,"moeda(s) de R$ 0.01")