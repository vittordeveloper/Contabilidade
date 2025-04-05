# Criamos aqui o projeto em si, precisa ter o nome, produto, quantidade, data da compra

from tkinter import *

def salvando():
    # Pegar todos as fichas e apagar
    nome.delete(0, END)
    produto.delete(0, END)
    quantidade.delete(0, END)
    data.delete(0, END)
    
    # Abrindo nova JANELA
    salvar = Tk()
    # Configs
    salvar.config(background='#3ef5ff')
    salvar.geometry('150x100+200+200')
    salvar.resizable(False, False)

    # Mensagem (salvo)
    mensagem_salvo = Label(salvar, text='Foi salvo com sucesso!',bg='#3ef5ff')
    mensagem_salvo.place(x=75, y=50, anchor='center')
    # Botão que encerra o loop
    encerrar_loop = Button(salvar, text='OK', width=8, command=lambda: salvar.destroy())
    encerrar_loop.place(x=75, y=75, anchor='center')
    salvar.mainloop()

# Exibição
Janela = Tk()

# Configurações
Janela.geometry('200x200+400+400')
Janela.resizable(False, False)
# Todas as cores
todos_os_bg = '#e7c669'

Janela.config(background=todos_os_bg)

# Cadastro (Nome)
nome_cadastro = Label(Janela, text='Nome: ', background=todos_os_bg)
nome_cadastro.grid(column=0)
nome = Entry(Janela)
nome.grid(column=1, row=0)

# Cadastro (Produto)
produto_cadastro = Label(Janela, text='Produto: ', background=todos_os_bg)
produto_cadastro.grid(column=0, row=1)
produto = Entry(Janela)
produto.grid(column=1, row=1)

# Cadastro (Quantidade)
quantidade_cadastro = Label(Janela, text='Quantidade: ', background=todos_os_bg)
quantidade_cadastro.grid(column=0)
quantidade = Entry(Janela)
quantidade.grid(column=1, row=2)

# Cadastro (Data De Compra)
data_cadastro = Label(Janela, text='Data de Compra: ', background=todos_os_bg)
data_cadastro.grid(column=0)
data = Entry(Janela)
data.grid(column=1, row=3)

# Botão de salvar
salvar_cadastro = Button(Janela, text='Salvar', command=salvando)
salvar_cadastro.grid(column=1, row=5)

# Loop (para se manter aberto)
Janela = mainloop()