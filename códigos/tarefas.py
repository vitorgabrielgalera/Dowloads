tarefas = []
import os
while True:
    print("Escolha o que deseja realizar pelo número")
    print("""0 - sair
1 - adicionar tarefa
2 - ver as tarefas
3 - marcar uma tarefa como feita""")
    opção = input()
    os.system("cls")
    if opção == "0":
        break
    elif opção == "1":
        tarefa = input("Digitea tarefa que deseja adicionar: ")
        tarefas.append(tarefa)
        print()
    elif opção == "2":
        print(tarefas)
        print()
    elif opção == "3":
        tarefa_removida = input("Digitea tarefa que deseja remover: ")
        tarefas.remove(tarefa_removida)
        print()