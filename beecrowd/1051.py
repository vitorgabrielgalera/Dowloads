a = float(int(input()))
if a > 4500:
    a = (a-4500)/100*28+270+80
    print(f"R$ {a:.2f}")
elif a > 3000 and a <= 4500:
    a = (a-3000)/100*18+80
    print(f"R$ {a:.2f}")
elif a > 2000 and a <= 3000:
    a = (a-2000)/100*8
    print(f"R$ {a:.2f}")
elif a <=2000:  
    print("Isento")