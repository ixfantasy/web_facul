from tkinter import *

# classe
i = Tk()



# título
i.title('Login de Usuário')



# ícone
i.wm_iconbitmap('user.ico')



# background
i['bg'] = '#FFBED5'



# tamanho da tela
largura = 400
altura = 300

largura_s = i.winfo_screenwidth()
altura_s = i.winfo_screenheight()

posx = largura_s / 2 - largura / 2
posy = altura_s / 2 - altura / 2

i.geometry('%dx%d+%d+%d' %(largura, altura, posx, posy))



# título do programa
tit_pag = Label(i,
                text = 'Login de Usuário',
                font = 'Arial 20 italic',
                bg = "#DB4C7F",
                fg = '#fff',
                bd = 5,
                relief = 'ridge',
                padx = 30,
                pady = 30
                )
tit_pag.grid(row = 0, column = 1)



# texto usuário e senha
usuario = Label(i, text='Usuário:',
                font = 'Arial 15',
                bg = '#FFBED5',
                fg = '#AB2756'
                )
senha = Label(i, text='Senha:',
              font = 'Arial 15',
              bg = '#FFBED5',
              fg = '#AB2756')

usuario.grid(row = 1, column = 0, padx = 5, pady = 10)
senha.grid(row = 2, column = 0, padx = 5, pady = 10)



# caixa de entrada
c1 = Entry(i, font = 'Arial 15', bg = '#FFE4EE', fg = '#CF004D')
c2 = Entry(i, font = 'Arial 15', bg = '#FFE4EE', fg = '#CF004D', show='*')

c1.grid(row = 1, column = 1)
c2.grid(row = 2, column = 1)



# ação botão
def Logar():
    user = c1.get()
    senha = c2.get()

    if user == 'admin' and senha == '1234':
        resul['text'] = 'Status: Login efetuado!'
    else:
        resul['text'] = 'Status: Login incorreto!'



# botão
bt = Button(i, text='Fazer Login',
            bg = '#93FFF2',
            fg = '#00342E',
            font = 'Arial 10 bold',
            command = Logar
            )

bt.grid(row = 3, column = 1, pady = 10)



# resultado do login
resul = Label(i, text='Status: ...',
              bg = '#FE97BD',
              fg = '#910035',
              font = 'Arial 20 italic',
              )

resul.grid(row = 5, column = 1)
              


# execução
i.mainloop()
