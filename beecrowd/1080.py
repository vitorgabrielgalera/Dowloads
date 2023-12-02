c = 0
a = 1
for i in range(1,101):
    b = int(int(input()))
    if b > c:
        a = i
        c = b
print(c)
print(a)