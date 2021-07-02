from tkinter import *

# criar uma classe
i = Tk()


# título
i.title('Primeiro Aplicativo')


# ícone da janela
i.wm_iconbitmap('abc.ico')


# cor background
i['bg'] = '#a00'


# tamanho da janela inicial
i.geometry('1000x1000')


# bloquear redimensionamento da janela. False(0), True(1)
i.resizable(True, True)


# tamanho mínimo da tela
"""i.minsize(200, 200)"""


# tamanho máximo da tela
"""i.maxsize(700, 500)"""


# janela abre em tela cheia
"""i.state('zoomed')"""


# janela abre minimizada
"""i.state('iconic')"""



# dimensões iniciais da janela
"""largura = 400
altura = 300

# resolução do nosso sistema
largura_screen = i.winfo_screenwidth()
altura_screen = i.winfo_screenheight()

print(largura_screen, altura_screen)

# calculando para centralizar
posx = largura_screen / 2 - largura / 2
posy = altura_screen / 2 - altura / 2

i.geometry('%dx%d+%d+%d' %(largura, altura, posx, posy))"""


# inserir label na janela
# Método 1
"""texto = Label(i,
              text = 'Bom dia! \n Belezinha?',
              bg = 'blue', # cor do background
              fg = 'yellow', # cor da fonte
              font = 'Arial 20 bold italic', # fonte
              bd = 10, # tamanho da borda
              relief = 'flat', # tipo da borda
              padx = 60, # padding largura
              pady = 60, # padding altura
              justify = RIGHT # alinhamento
              )"""

# Método 2
"""texto1 = Label(i)
texto1['text'] = 'Bom dia!'
texto1['bg'] = 'blue'
texto1['fg'] = 'yellow'
"""

# tipos de borda: solid, raised, sunken, ridge, groove, flat (none)

# empacotar o label
"""texto.pack()"""



# inserir botão
"""def b_Click(mensagem):
    print(mensagem)

b = Button(i, text='Clique',command=lambda: b_Click('Funcionou'))
b.pack()"""


# criar caixa de entradas
"""ent = Entry(i)
ent.pack()"""



"""def Calcular():
    print('Calculando')
    resultado['text'] = 'Calculando!'
    resultado['text'] = form.get()

form = Entry(i)
form.pack()

calc = Button(i, text='Calcule', command = Calcular)
calc.pack()

resultado = Label(i, text='Resultado', fg = 'green')
resultado.pack()"""


# Sistema de Grid
label1 = Label(i, text='Testando', font='Arial 20', bg='red')
label2 = Label(i, text='Testando', font='Arial 20', bg='yellow')
label3 = Label(i, text='Testando', font='Arial 20', bg='blue')


label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

btn1 = Button(i, text="Click1")
btn2 = Button(i, text="Click2")
btn3 = Button(i, text="Click3")

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)





i.mainloop() # obrigatório para rodar o programa. Última linha
