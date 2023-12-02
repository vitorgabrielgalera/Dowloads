#importo uma biblioteca que me desponibiliza limpar o terminal
import os
número = 0
número = float(número)
sinal = "+"
resultado = 0
while True:
    print("Escolha a operação que deseja realizar pelo número")
    print()
    print("""0 - sair
1 - adição
2 - subtração
3 - multiplicação
4 - divisão
5 - expressão""")
    operação = input()
#limpo o terminal usando o comando importado
    os.system("cls")
    if operação == "0":
        break
    elif operação == "1":
        print("Escolha os números que deseja somar")
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print("O resultado é:", a + b)
    elif operação == "2":
        print("Escolha os números que deseja subtrair")
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print("O resultado é:", a - b)
    elif operação == "3":
        print("Escolha os números que deseja multiplicar")
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print("O resultado é:", a * b)
    elif operação == "4":
        print("Escolha os números que deseja dividir")
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print("O resultado é:", a / b)
    elif operação == "5":
        print("escreva a expressão (separe sinais e números por espaço)")
        expressão_lista = []
        a = input()
        expressão_lista = a.split(" ")
        for i in range(len(expressão_lista)):
            if "0" in expressão_lista[i]:
                expressão_lista[i] = float(expressão_lista[i])
            elif "1" in expressão_lista[i]:
                expressão_lista[i] = float(expressão_lista[i])
            elif "2" in expressão_lista[i]:
                expressão_lista[i] = float(expressão_lista[i])
            elif "3" in expressão_lista[i]:
                expressão_lista[i] = float(expressão_lista[i])
            elif "4" in expressão_lista[i]:
                expressão_lista[i] = float(expressão_lista[i])
            elif "5" in expressão_lista[i]:
                expressão_lista[i] = float(expressão_lista[i])
            elif "6" in expressão_lista[i]:
                expressão_lista[i] = float(expressão_lista[i])
            elif "7" in expressão_lista[i]:
                expressão_lista[i] = float(expressão_lista[i])
            elif "8" in expressão_lista[i]:
                expressão_lista[i] = float(expressão_lista[i])
            elif "9" in expressão_lista[i]:
                expressão_lista[i] = float(expressão_lista[i])
        for i in range(len(expressão_lista)):
            if type(expressão_lista[i]) == str:
                if "*" in expressão_lista[i]:
                    multiplicação = expressão_lista[i-1] * expressão_lista[i+1]
                    expressão_lista[i] = " "
                    expressão_lista[i+1] = " "
                    expressão_lista[i-1] = multiplicação
        contagem = len(expressão_lista)
        while True:
            contagem -= 1
            if type(expressão_lista[contagem]) == str:
                if " " in expressão_lista[contagem]:
                    expressão_lista.remove(" ")
            if contagem <= 0:
                break
        for i in range(len(expressão_lista)):
            if type(expressão_lista[i]) == str:
                if "/" in expressão_lista[i]:
                    divisao = expressão_lista[i-1] / expressão_lista[i+1]
                    expressão_lista[i] = " "
                    expressão_lista[i+1] = " "
                    expressão_lista[i-1] = divisao
        contagem = len(expressão_lista)
        while True:
            contagem -= 1
            if type(expressão_lista[contagem]) == str:
               if " " in expressão_lista[contagem]:
                    expressão_lista.remove(" ")
            if contagem <= 0:
                break
        for i in range (len(expressão_lista)):
            if type(expressão_lista[i]) == float:
                número = expressão_lista[i]
                if sinal == "+":
                   resultado += número
                if sinal == "-":
                   resultado -= número
            else:
                sinal = expressão_lista[i]
        print("O resultado é: ",resultado)
#notação polonesa reversa

#de forma mais simples (linha 156)

import os
número = 0
número = float(número)
sinal = "+"
resultado = 0
while True:
    print("Escolha a operação que deseja realizar pelo número")
    print()
    print("""0 - sair
1 - adição
2 - subtração
3 - multiplicação
4 - divisão
5 - expressão""")
    operação = input()
    os.system("cls")
    if operação == "0":
        break
    elif operação == "1":
        print("Escolha os números que deseja somar")
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print("O resultado é:", a + b)
    elif operação == "2":
        print("Escolha os números que deseja subtrair")
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print("O resultado é:", a - b)
    elif operação == "3":
        print("Escolha os números que deseja multiplicar")
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print("O resultado é:", a * b)
    elif operação == "4":
        print("Escolha os números que deseja dividir")
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print("O resultado é:", a / b)
    elif operação == "5":
        print("escreva a expressão (separe sinais e números por espaço)")
        expressão_lista = []
        a = input()
        expressão_lista = a.split(" ")
        for i in range(len(expressão_lista)):
            if expressão_lista[i].isnumeric():
                expressão_lista[i] = float(expressão_lista[i])
        for i in range(len(expressão_lista)):
            if type(expressão_lista[i]) == str:
                if "*" in expressão_lista[i]:
                    multiplicação = expressão_lista[i-1] * expressão_lista[i+1]
                    expressão_lista[i] = " "
                    expressão_lista[i+1] = " "
                    expressão_lista[i-1] = multiplicação
        contagem = len(expressão_lista)
        while True:
            contagem -= 1
            if type(expressão_lista[contagem]) == str:
                if " " in expressão_lista[contagem]:
                    expressão_lista.remove(" ")
            if contagem <= 0:
                break
        for i in range(len(expressão_lista)):
            if type(expressão_lista[i]) == str:
                if "/" in expressão_lista[i]:
                    divisao = expressão_lista[i-1] / expressão_lista[i+1]
                    expressão_lista[i] = " "
                    expressão_lista[i+1] = " "
                    expressão_lista[i-1] = divisao
        contagem = len(expressão_lista)
        while True:
            contagem -= 1
            if type(expressão_lista[contagem]) == str:
               if " " in expressão_lista[contagem]:
                    expressão_lista.remove(" ")
            if contagem <= 0:
                break
        for i in range (len(expressão_lista)):
            if type(expressão_lista[i]) == float:
                número = expressão_lista[i]
                if sinal == "+":
                   resultado += número
                if sinal == "-":
                   resultado -= número
            else:
                sinal = expressão_lista[i]
        print("O resultado é: ",resultado)

#utilizando o comando eval (executa uma string) (linha241)
#o comando eval é perigoso pelo alto risco do usuario quebrar o código

import os
número = 0
número = float(número)
sinal = "+"
resultado = 0
while True:
    print("Escolha a operação que deseja realizar pelo número")
    print()
    print("""0 - sair
1 - adição
2 - subtração
3 - multiplicação
4 - divisão
5 - expressão""")
    operação = input()
    os.system("cls")
    if operação == "0":
        break
    elif operação == "1":
        print("Escolha os números que deseja somar")
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print("O resultado é:", a + b)
    elif operação == "2":
        print("Escolha os números que deseja subtrair")
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print("O resultado é:", a - b)
    elif operação == "3":
        print("Escolha os números que deseja multiplicar")
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print("O resultado é:", a * b)
    elif operação == "4":
        print("Escolha os números que deseja dividir")
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print("O resultado é:", a / b)
    elif operação == "5":
        print("escreva a expressão (separe sinais e números por espaço)")
        expressao = input()
        print(eval(expressao))
        print("O resultado é: ",resultado)