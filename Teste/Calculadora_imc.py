from tkinter import *
root = Tk()

#defina o nome da janela
root.title("calculadora de imc")

#defino e posiciono a altura
altura = Entry(root, width=10, borderwidth=3, font=("System", 20), justify="right")
altura.grid(row=0, column=0)

#defino e posiciono o visor
visor = Entry(root, width=10, borderwidth=3, font=("System", 20), justify="right", state="readonly")
visor.grid(row=0, column=1)

#defino e posiciono o peso
peso = Entry(root, width=10, borderwidth=3, font=("System", 20), justify="right")
peso.grid(row=0, column=2)

#defino e posiciono as instrução
ins_altura = Label(root,text="Digite sua altura(m)")
ins_peso = Label(root,text="Digite seu peso(kg)")

ins_altura.grid(row=1, column=0)
ins_peso.grid(row=1, column=2)

#defino e posiciono o diagnótico
magro = Label(root,text="abaixo do peso - abaixo de 25", bg="blue")
saúdavel = Label(root,text="normal - 18 a 25", bg="green")
gordo = Label(root,text="acima do peso - acima de 25", bg="red")

magro.grid(row=2, column=0)
saúdavel.grid(row=2, column=1)
gordo.grid(row=2, column=2)

#defino função do botão
def click():
   visor.configure(state="normal")
   visor.delete(0, END)
   pes= peso.get()
   altur = altura.get()
   pes = float(pes)
   altur = float(altur)
   resutado = pes/(altur * altur)
   resutado = int(resutado)
   visor.insert(0, str(resutado))
   visor.configure(state="readonly")

#defino e posiciono o botão
btn_1 = Button(root, text="Calcular", command=lambda : click(), font=("System", 20))
btn_1.grid(row=1, column=1)

root.mainloop()