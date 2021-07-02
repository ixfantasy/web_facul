# -*- coding: utf-8 -*-

# Questão 1

fut = dict()

fut['Nome'] = input('Digite o nome do jogador:')

fut['partidasTotal'] = int(input('Digite o número de partidas jogadas:'))

soma = 0
for n in range(1, fut['partidasTotal']+1):
    x = int(input(f'Digite o número de gols da partida {n}:'))
    soma = soma + x
    fut[n] = x

fut['totalGols'] = soma

print(fut)




# Questão 2

x = 0
cont = 0

pes = dict()

total = list()

mulher = list()

while x != 1:
    cont = cont + 1
    pes['nome'] = input('Digite o nome:')
    pes['sexo'] = input('Digite o sexo:')
    pes['idade'] = int(input('Digite a idade:'))

    if pes['sexo'] == 'f':
        mulher.append(pes.copy())

    total.append(pes.copy())
    x = int(input('Digite 0 para continuar, 1 para parar:'))

print(f'Total de pessoas cadastradas: {cont}')

soma = 0
for n in range(0, cont):
    soma = soma + total[n]['idade']

media = soma / cont
print(f'Média de idade do grupo: {media}')

print(f'Lista de mulheres: {mulher}')

acima = list()
for n in range(0, cont):
    if total[n]['idade'] > media:
        acima.append(total[n]['nome'][:])

print(f'Pessoas com idade acima da média: {acima}')




# Questão 3
import math

x = int(input('Digite um valor:'))

if x > 0:
    print(f'Número positivo, raiz quadrada: {math.sqrt(x)}')
elif x < 0:
    print(f'Número negativo, quadrado do número: {x**2}')
else:
    print('Valor digitado foi 0.')




# Questão 4

anonasc = int(input('Digite o seu ano de nascimento:'))

anoat = int(input('Digite o ano atual:'))

print(f'Idade atual: {anoat - anonasc}, Idade em 2030: {2030 - anonasc}')

    
    
