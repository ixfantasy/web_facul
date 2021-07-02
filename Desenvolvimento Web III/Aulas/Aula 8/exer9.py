#Questão 1

def area(x, y):
    print(x * y)

largura = int(input('Digite a largura:'))
comprimento = int(input('Digite o comprimento:'))
area(largura, comprimento)



#Questão 2

def escreva(txt):
    tam = len(txt)
    print('-' * tam)
    print(txt)
    print('-' * tam)

frase = input('Digite um texto:')
escreva(frase)



#Questão 3

def contador(inicio, fim, passo):
    n = 0
    while n <= 10:
        print(f'{n}', end='-')
        n = n + 1
    print('Final 1')
    print('.' * 30)

    n = 10
    while n >= 0:
        print(f'{n}', end='-')
        n = n - 1
    print('Final 2')
    print('.' * 30)

    n = inicio
    while n <= fim:
        print(f'{n}', end='-')
        n = n + passo
    print('Final 3')
    print('.' * 30)

ini = int(input('Digite o número inicial:'))
fim = int(input('Digite o número final:'))
passo = int(input('Número de casas:'))

contador(ini, fim, passo)
