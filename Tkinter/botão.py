from tkinter import *
m = 0
def contagem():
    m = int(m)
    n = Label(janela,text=m)
    n.pack()
    m = m + 1
janela = Tk()
janela.title("programinha")
intrução = Label(janela,text="clique no botão!",bg="#000000",fg="#56e3dc")
intrução.pack()
botao = Button(janela,text="clique aqui!",command=contagem,bg="#000000",fg="#56e3dc")
botao.pack()
janela.mainloop()