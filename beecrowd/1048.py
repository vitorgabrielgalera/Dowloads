a = float(int(input()))
if a >= 0 and a <= 400:
    a = a//100*15
    c = 15
    d = a+a
elif a > 400 and a <= 800:
    a = a//100*12
    c = 12
    d = a+a
elif a > 800 and a <= 1200:
    a = a//100*10
    c = 10
    d = a+a
elif a > 1200 and a <= 2000:
    a = a//100*7
    c = 7
    d = a+a
else:
    a = a//100*4
    c = 4
    d = a+a
print(f"Novo salario: {d:.2f}")
print(f"Reajuste ganho: {a:.2f}")
print(f"Em percentual: {c:.0f} %")