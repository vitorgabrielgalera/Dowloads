x = int(int(input()))
if x % 2 == 1:
    for i in range(x,x+12,2):
        print(i)
if x % 2 == 0:
    for i in range(x+1,x+13,2):
        print(i)

x = int(int(input()))
for i in range(x,x+12):
    if i%2==1:
        print(i)
    else:
        print(i+1)