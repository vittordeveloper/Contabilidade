# Criamos aqui o projeto em si, precisa ter o nome, produto, quantidade, data da compra

from tkinter import *

def salvando():
    # Pegar todos as fichas e apagar
    nome_valor = nome.get()
    produto_valor = produto.get()
    quantidade_valor = quantidade.get()
    data_valor = data.get()
    
    if not nome_valor or not produto_valor or not quantidade_valor or not data_valor:
        salvando_limpeza['text'] = 'Preencha todos os dados, por favor!'
        salvando_limpeza.place(x=175, y=107, anchor='center')
        Janela.after(2500, salvando_limpeza.place_forget)
        return
    
    # Numerar as fichas
    try:
        with open('dados.txt', 'r', encoding='utf-8') as abrir:
            linhas = abrir.readlines()
            numeracao = len(linhas) + 1
    except FileNotFoundError:
        numeracao = 1
    
    # Enviar para um arquivo .txt (simular um banco de dados)
    with open('dados.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{numeracao}. Nome: {nome.get()}, Produto: {produto_valor}, Quantidade: {quantidade_valor}, Data de Compra: {data_valor}\n')

    # Apagando os textos
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
    encerrar_loop = Button(salvar, text='OK', width=8, command=lambda: salvar.destroy(), cursor='hand2')
    encerrar_loop.place(x=75, y=75, anchor='center')
    salvar.mainloop()

def limpar():
    
    # Mensagem para alertar
    
    # Função
    try: 
        with open('dados.txt', 'w', encoding='utf-8') as arquivo:
            pass
    except:
        salvando_limpeza['text'] = 'O arquivo não existe!'
       
    else:
        salvando_limpeza['text'] = 'Os dados foram apagados!'

    salvando_limpeza.place(x=175, y=107, anchor='center')
    Janela.after(2500, salvando_limpeza.place_forget)



# Exibição
Janela = Tk()

# Configurações
Janela.geometry('350x200+400+400')
Janela.resizable(False, False)

# Variáveis
todos_os_bg = 'white'
todas_as_fontes = ('Arial', 13)

Janela.config(background=todos_os_bg)

# Cadastro (Nome)
nome_cadastro = Label(Janela, text='Nome: ', background=todos_os_bg, font=todas_as_fontes)
nome_cadastro.grid(column=0)
nome = Entry(Janela, width=33)
nome.grid(column=1, row=0)

# Cadastro (Produto)
produto_cadastro = Label(Janela, text='Produto: ', background=todos_os_bg, font=todas_as_fontes)
produto_cadastro.grid(column=0, row=1)
produto = Entry(Janela, width=33)
produto.grid(column=1, row=1)

# Cadastro (Quantidade)
quantidade_cadastro = Label(Janela, text='Quantidade: ', background=todos_os_bg, font=todas_as_fontes)
quantidade_cadastro.grid(column=0)
quantidade = Entry(Janela, width=33)
quantidade.grid(column=1, row=2)

# Cadastro (Data De Compra)
data_cadastro = Label(Janela, text='Data de Compra: ', background=todos_os_bg, font=todas_as_fontes)
data_cadastro.grid(column=0)
data = Entry(Janela, width=33)
data.grid(column=1, row=3)

# Botão de salvar
salvar_cadastro = Button(Janela, text='Salvar', command=salvando, width=40, height=1, background='green', font=('Arial', 10), cursor='hand2')
salvar_cadastro.place(x=175, y=135, anchor='center')

# Botão para limpar
limpar_botao = Button(Janela, text='Limpar', width=40, height=1, background='red', font=('Arial', 10), cursor='hand2', command=limpar)
limpar_botao.place(x=175, y=165, anchor='center')

# Salvando/Limpeza
salvando_limpeza = Label(Janela, text='', background='white')

# Loop (para se manter aberto)
Janela = mainloop()