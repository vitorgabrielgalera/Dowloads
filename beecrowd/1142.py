x = int(int(input()))
a = 1
for i in range(0,x):
    print(a, a+1, a+2,"PUM")
    a += 4

#outra forma de resolver

x = int(int(input()))
for i in range(1,x*4,4):
    for j in range(i,i+4):
        if j == i+3:
            print("PUM")
        else:
            print(j,end=" ")