x = int(input())
a,b,c = x.split(" ")
a = float(a)
b = float(b)
c = float(c)
tri = a*c/2
cir = c*c*3.14159
tra = (a+b)*c/2
qua = b*b
ret = a*b
tri = float(tri)
cir = float(cir)
tra = float(tra)
qua = float(qua)
ret = float(ret)
print(f"TRIANGULO: {tri:.3f}")
print(f"CIRCULO: {cir:.3f}")
print(f"TRAPEZIO: {tra:.3f}")
print(f"QUADRADO: {qua:.3f}")
print(f"RETANGULO: {ret:.3f}")