a = float(int(input()))
if a <= 25 and a >= 0:
    print("Intervalo [0,25]")
elif a <= 50 and a > 25:
    print("Intervalo (25,50]")
elif a <= 75 and a > 50:
    print("Intervalo (50,75]")
elif a <= 100 and a > 75:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")