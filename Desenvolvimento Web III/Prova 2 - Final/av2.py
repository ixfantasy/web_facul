from tkinter import *
import mysql.connector

# QUESTÃO 2
# Banco de Dados
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'cadastro'
    )
cursor = conexao.cursor()

# Criar a base de dados
"""cursor.execute('create database cadastro')"""


# Criar a tabela livro
"""cursor.execute('create table livro(titulo varchar(50) not null, autor varchar(80) not null, editora varchar(70) not null, preço int(3) not null, id_livro int(5) primary key auto_increment)')"""


# Inserir elementos
"""sql = 'insert into livro(titulo, autor, editora, preço) values (%s, %s, %s, %s)'

val = [
    ('Título 1', 'Fulano', 'Editora1', 20),
    ('Título 2', 'Cicrano', 'Saraiva', 40),
    ('Título 3', 'Maria', 'Editora3', 15),
    ('Título 4', 'Ana', 'Saraiva', 35),
    ('Título 5', 'Fulana', 'Editora5', 25)
    ]
cursor.executemany(sql, val)
conexao.commit()"""


# Atualizar tabela
"""cursor.execute('update livro set preço = 60 where id_livro = 2')
conexao.commit()"""


# Deletar um elemento
"""cursor.execute('delete from livro where id_livro = 1')
conexao.commit()"""


# Selecionar todos os livros da Editora Saraiva
"""cursor.execute('select * from livro where editora like "%Saraiva%"')
result = cursor.fetchall()
print(result)"""



# QUESTÃO 1
# Base do Programa - Interface
master = Tk()

master.title('Prova AV2') #Título

master.wm_iconbitmap('Arquivo.ico') #Ícone

master.geometry('500x400') #Tamanho Tela


# Conteúdo do Programa
# Título Principal Cadastro
texto = Label(master,
              text = 'Cadastro de Livros',
              fg = 'gray',
              font = '10')
texto.grid(row = 0, column = 1)


#Título
tit = Label(master,
            text = 'Título:')
tit.grid(row = 1, column = 0)

tit_box = Entry(master)
tit_box.grid(row = 1, column = 1)


#Autor
aut = Label(master,
            text = 'Autor:')
aut.grid(row = 2, column = 0)

aut_box = Entry(master)
aut_box.grid(row = 2, column = 1)


#Editora
edi = Label(master,
            text = 'Editora:')
edi.grid(row = 3, column = 0)

edi_box = Entry(master)
edi_box.grid(row = 3, column = 1)


#Preço
pre = Label(master,
            text = 'Preço:')
pre.grid(row = 4, column = 0)

pre_box = Entry(master)
pre_box.grid(row = 4, column = 1)


# Botão
bt = Button(master,
            text = 'Cadastrar')
bt.grid(row = 5, column = 1)


# Imagem
foto = PhotoImage(file = 'Livro.png')
label_imagem = Label(master,
                     image = foto)
label_imagem.grid(row = 6, column = 1)


master.mainloop()
