a = 0
a = int(a)
r = 0
r = float(a)
for i in range(1,7):
    x = float(int(input()))
    if x > 0:
        a += 1
        r += x
print(a, "valores positivos")
print(f"{r/a:.1f}")