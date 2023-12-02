a = int(int(input()))
0 <= a <= 100
if a == 0:
    print("E")
elif a > 0 and a < 36:
    print("D")
elif a > 35 and a < 61:
    print("C")
elif a > 60 and a < 86:
    print("a")
elif a > 85 and a <= 100:
    print("A")