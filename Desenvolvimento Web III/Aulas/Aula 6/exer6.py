#Número 84
i = 0
nome_peso = list()

lista = list()


while(i == 0):
    del nome_peso[:]
    
    nome_peso.append(input('Digite o nome:'))
    nome_peso.append(int(input('Digite o peso:')))

    lista.append(nome_peso[:])
    
    i = int(input('Digite 0 para adicionar mais pessoas!'))

total = len(lista)
print(f'Total de pessoas cadastradas: {total}')

soma = 0
for n in range(0, len(lista)):
    soma = soma + lista[n][1]
media = soma / len(lista)
print(f'A média de peso é {media}, logo...')


pesada = list()

for n in range(0, len(lista)):
    if lista[n][1] > media:
        pesada.append(lista[n][0][:])
print(f'As pessoas mais pesadas são: {pesada}')

leve = list()

for n in range(0, len(lista)):
    if lista[n][1] < media:
        leve.append(lista[n][0][:])
print(f'As pessoas mais leves são: {leve}')




# Número 85
num = list()

for n in range(0, 7):
    x = int(input('Digite um valor:'))

    if x % 2 == 0:
        num.insert(0, x)
    else:
        num.insert(6, x)
print(f'Lista preenchida: {num}')

num.sort()
print(f'Lista ordenada: {num}')




# Número 86
matriz = list()

num = list()

for n in range (0,3):
    del num[:]

    num.append(int(input('Digite um valor [0]:')))
    num.append(int(input('Digite um valor [1]:')))
    num.append(int(input('Digite um valor [2]:')))

    matriz.append(num[:])

for n in range(0, 3):
    print(matriz[n][0], matriz[n][1], matriz[n][2])




# Número 87
# a) soma dos pares

soma = 0
for n in range(0, 3):
    if matriz[n][0] % 2 == 0:
        soma = soma + matriz[n][0]
    if matriz[n][1] % 2 == 0:
        soma = soma + matriz[n][1]
    if matriz[n][2] % 2 == 0:
        soma = soma + matriz[n][2]
print(f'Soma dos pares: {soma}')

# b) Soma de todos os valores da terceira coluna
soma = 0
for n in range(0, 3):
    soma = soma + matriz[n][2]
print(f'Soma dos valores da terceira coluna: {soma}')

# c) O maior valor da segunda linha
maior = 0
for n in range(0, 3):
    if matriz[1][n] > maior:
        maior = matriz[1][n]
print(f'O maior valor da segunda linha: {maior}')




# Número 88
import random

x = int(input('Deseja gerar quantos jogos?'))

jogo = list()

total = list()

for n in range(0, x):
    del jogo[:]

    for k in range(0, 6):
        y = random.randint(1, 60)
        jogo.insert(k, y)

    total.append(jogo[:])

print(f'Possibilidades: {total}')




# Número 89

flag = 0

nome_nota = list()

turma = list()

cont = 0

while(flag == 0):
    del nome_nota[:]
    
    nome_nota.append(input('Insira o nome do aluno:'))
    nome_nota.append(int(input('Insira a nota AV1:')))
    nome_nota.append(int(input('Insira a nota AV2:')))

    turma.append(nome_nota[:])
    cont = cont + 1

    flag = int(input('Digite 0 para inserir mais alunos.'))

boletim = list()

for n in range(0, cont):
    media = (turma[n][1] + turma[n][2]) / 2

    boletim.insert(n, media)

print(f'Média dos alunos: {boletim}')

n = int(input('Digite o número do aluno para exibir suas notas:'))
print(f'Aluno {turma[n][0]} -> AV1: {turma[n][1]}, AV2: {turma[n][2]}')



    
    




