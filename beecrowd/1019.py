a = int(int(input()))
horas = a//3600
a = a%3600
minutos = a//60
a = a%60
print(f"{horas}:{minutos}:{a}")