x = int(int(input()))
a = x//365
x = x%365
print(f"{a} ano(s)")
b = x//30
x = x%365
print(f"{b} mes(es)")
c = x%30
print(f"{c} dia(s)")