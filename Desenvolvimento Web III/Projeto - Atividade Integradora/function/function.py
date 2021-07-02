from tkinter import *
import mysql.connector

def new():
    #Conexão com o Banco de Dados
    """
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'eventos'
        )
    cursor = conexao.cursor()
    """



    #Base Programa
    master = Tk()
    master.title('Sugestão dos Participantes') #Título

    master.wm_iconbitmap('star.ico') #Ícone

    master.state('zoomed') #Tela

    master['bg'] = '#09697F' #Cor background



    #Logo LaSalle
    img = PhotoImage(file='logo.png')
    logo = Label(master, image = img)
    logo.place(x = 350, y = 0)



    #Título principal - "Sugestão"
    tit_prin = Label(master,
                      text = 'Sugestão de Temas',
                      bg = '#09697F',
                      fg = 'white',
                      font = 'Arial 20 bold',
                      padx = 30,
                      pady = 30)
    tit_prin.place(x = 700, y = 210)


    text_novo = Label(master,
                          text = 'Novo Tema:',
                          bg = '#09697F',
                          fg = 'white',
                          font = 'Arial 12 bold',
                          padx = 20,
                          pady = 20)
    text_novo.place(x = 410, y = 330)
        
    global caixa
    caixa = Entry(master, font = 'Arial 10')
    caixa.place(x = 530, y = 350)
        
    bt_tema = Button(master, command = botao, text = 'Salvar Novo Tema')
    bt_tema.place(x = 680, y = 348)

    def botao():
        txt = caixa.get()
        print(txt)    

