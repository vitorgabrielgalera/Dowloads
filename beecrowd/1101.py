while True:
    a,b = int(input()).split(" ")
    a = int(a)
    b = int(b)
    if a <= 0 or b <= 0:
        break
    c = sorted([a,b])[0]
    b = sorted([a,b])[1]
    soma = 0
    for i in range(c,b+1):
        print(i, end=" ")
        soma += i
    print(f"Sum={soma}")