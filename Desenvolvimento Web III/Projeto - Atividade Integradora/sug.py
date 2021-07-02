from function import *
from tkinter import *
import random


# Base Programa
master = Tk()
master.title('Sugestão dos Participantes') #Título

master.wm_iconbitmap('star.ico') #Ícone do Programa

master.geometry('1056x740') #Tamanho da Tela

master['bg'] = '#09697F' #Cor Background


# Logo LaSalle - Tela Principal
img = PhotoImage(file='logo.png')
logo = Label(master, image = img)
logo.place(x = 0, y = 0)


# Título da Tela Principal - "Sugestão"
tit_prin = Label(master,
                  text = 'SUGESTÃO DE TEMAS',
                  bg = '#09697F',
                  fg = 'white',
                  font = 'Arial 30 bold',
                  padx = 30,
                  pady = 30)
tit_prin.place(x = 300, y = 210)


# Rótulo - Tema
rot_tema = Label(master,
                  text = 'TEMA:',
                  bg = '#09697F',
                  fg = 'white',
                  font = 'Arial 18 bold',
                  padx = 20,
                  pady = 20)
rot_tema.place(x = 400, y = 290)


# Dropdown Menu - Selecionar tema
def Selecionar(x):
    global opt
    opt = x


result = [
    'Selecione...',
    '4ª Revolução Industrial',
    'Automatização das Coisas',
    'Inovação Tecnológica',
    'Comunicação para o meu negócio',
    'Inovação e Criatividade'
    ]

variable = StringVar(master)
variable.set(result[0])

w = OptionMenu(master, variable, *result, command = Selecionar)
w.config(width = 25, font=('Arial', 8), bg = '#92D1DF', relief = 'flat')
w.place(x = 500, y = 310)


# Botão Check - Novo Tema
valor_check = IntVar()
check = Checkbutton(master, 
                    command = new, 
                    text = 'Sugerir novo tema', 
                    bg = '#09697F', 
                    fg = '#9CE4FF', 
                    font = 'Arial 12 italic bold')
check.place(x = 460, y = 345)


# Título - Palestrante
rot_palest = Label(master,
                  text = 'PALESTRANTE:',
                  bg = '#09697F',
                  fg = 'white',
                  font = 'Arial 18 bold')
rot_palest.place(x = 450, y = 415)


# Rótulos e Caixas - Palestrante
rot_nome = Label(master, # Nome
                  text = '• Nome do Palestrante:',
                  bg = '#09697F',
                  fg = '#9CE4FF',
                  font = 'Arial 12 bold')
rot_nome.place(x = 340, y = 460)

box_nome = Entry(master, font = 'Arial 12')
box_nome.place(x = 530, y = 460)
#

rot_num = Label(master, # Telefone
                  text = '• Telefone do Palestrante:',
                  bg = '#09697F',
                  fg = '#9CE4FF',
                  font = 'Arial 12 bold')
rot_num.place(x = 330, y = 530)

box_num = Entry(master, font = 'Arial 12')
box_num.place(x = 540, y = 530)
#

rot_email = Label(master, # E-mail
                  text = '• E-mail do Palestrante:',
                  bg = '#09697F',
                  fg = '#9CE4FF',
                  font = 'Arial 12 bold')
rot_email.place(x = 340, y = 600)

box_email = Entry(master, font = 'Arial 12')
box_email.place(x = 530, y = 602)
#

# Botão Enviar
def Salvar():  
    no = box_nome.get()

    num = int(box_num.get())

    em = box_email.get()

    cpf = random.randint(11111111111, 99999999999)

    print(f'Salvando Dados...\n\n• Nome do Palestrante: {no}\n• Telefone do Palestrante: {num}\n• E-mail do Palestrante: {em}\n• CPF do Participante: {cpf}\n• Tema selecionado: {opt}')


b = Button(master, text='ENVIAR', font = 'Arial 15', bg ='#92D1DF', fg = '#004C5D', relief = 'flat', command = Salvar)
b.place(x = 500, y = 660)


mainloop()
