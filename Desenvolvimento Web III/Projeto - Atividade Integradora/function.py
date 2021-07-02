from tkinter import *
import random

def new():
    
    #Base Programa
    i = Tk()
    i.title('Sugestão dos Participantes') #Título

    i.wm_iconbitmap('star.ico') #Ícone

    i.geometry('1056x740') #Tela

    i['bg'] = '#09697F' #Cor background



    #Título principal - "Sugestão"
    tit_prin = Label(i,
                      text = 'SUGESTÃO DE TEMAS',
                      bg = '#09697F',
                      fg = 'white',
                      font = 'Arial 30 bold',
                      padx = 30,
                      pady = 30)
    tit_prin.place(x = 300, y = 0)


    # Rótulo "Novo Tema"
    text_novo = Label(i,
                          text = 'NOVO TEMA:',
                          bg = '#09697F',
                          fg = 'white',
                          font = 'Arial 18 bold',
                          padx = 20,
                          pady = 20)
    text_novo.place(x = 360, y = 100)
        
    global caixa
    caixa = Entry(i, font = 'Arial 12')
    caixa.place(x = 545, y = 125)
        


    #Título Opcional
    rot_palest = Label(i,
                      text = '(Opcional)',
                      bg = '#09697F',
                      fg = '#FF7F7F',
                      font = 'Arial 12 bold italic',
                      pady = 20)
    rot_palest.place(x = 410, y = 180)

    
    #Título Palestrante
    rot_palest = Label(i,
                      text = 'PALESTRANTE:',
                      bg = '#09697F',
                      fg = 'white',
                      font = 'Arial 18 bold',
                      pady = 20)
    rot_palest.place(x = 500, y = 175)



    global box_palest
    global box_email
    global box_nome
    global box_num

    #Rótulos e Caixas - Palestrante
    rot_nome = Label(i, # Nome
                      text = '• Nome do Palestrante:',
                      bg = '#09697F',
                      fg = '#9CE4FF',
                      font = 'Arial 12 bold')
    rot_nome.place(x = 340, y = 250)

    box_nome = Entry(i, font = 'Arial 12')
    box_nome.place(x = 530, y = 250)
    #



    rot_num = Label(i, # Telefone
                      text = '• Telefone do Palestrante:',
                      bg = '#09697F',
                      fg = '#9CE4FF',
                      font = 'Arial 12 bold')
    rot_num.place(x = 330, y = 300)

    box_num = Entry(i, font = 'Arial 12')
    box_num.place(x = 540, y = 300)
    #



    rot_email = Label(i, # E-mail
                      text = '• E-mail do Palestrante:',
                      bg = '#09697F',
                      fg = '#9CE4FF',
                      font = 'Arial 12 bold')
    rot_email.place(x = 340, y = 350)

    box_email = Entry(i, font = 'Arial 12')
    box_email.place(x = 530, y = 350)
    #

    b = Button(i, text='ENVIAR', font = 'Arial 15', bg ='#92D1DF', fg = '#004C5D', relief = 'flat', command = Salvar)
    b.place(x = 380, y = 400)

    b2 = Button(i, text="CANCELAR E FECHAR", command = i.destroy, font = 'Arial 15', bg ='#BFCACD', fg = '#004C5D', relief = 'flat')
    b2.place(x = 500, y = 400)

def quit():
    global i
    i.quit()


def Salvar():
    tema = caixa.get()

    no = box_nome.get()

    num = box_num.get()

    em = box_email.get()

    cpf = random.randint(11111111111, 99999999999)

    if tema == '':
        print('ERRO!!! TEMA NÃO CADASTRADO!!!')
        
    else:
        print(f'Salvando Dados...\n\n• Novo Tema Cadastrado: {tema}\n• CPF do Participante: {cpf}')
        
        if no != '':
            print(f'• Nome do Palestrante: {no}\n• Telefone do Palestrante: {num}\n• E-mail do Palestrante: {em}')

        

