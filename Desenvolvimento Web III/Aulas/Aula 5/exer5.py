# Número 72.
ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número de 0 a 20:'))

print(f'Número por extenso: {ext[num]}')




# Número 73.
times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')

print(f'Primeiros colocados: {times[0:5]}')

print(f'Os 4 últimos colocados: {times[16:]}')

times_ord = ('América-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Ceará', 'Chapecoense', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Grêmio', 'Internacional', 'Palmeiras', 'Paraná', 'Santos', 'São Paulo',  'Sport', 'Vasco', 'Vitória')

print(f'Ordem alfabética: {times_ord}')

print(f'Posição do Vasco: {times.index("Vasco") + 1}º lugar')




# Número 74.
import random

num1 = random.randint(0, 10)
num2 = random.randint(0, 10)
num3 = random.randint(0, 10)
num4 = random.randint(0, 10)
num5 = random.randint(0, 10)

aleatorio = (num1, num2, num3, num4, num5)
print(aleatorio)

print(f'Maior elemento: {max(aleatorio)} // Menor elemento: {min(aleatorio)}')




# Número 75.
num1 = int(input('Digite valor 1:'))

num2 = int(input('Digite valor 2:'))

num3 = int(input('Digite valor 3:'))

num4 = int(input('Digite valor 4:'))

tupla_num = (num1, num2, num3, num4)

print(f'Quantidade de 9 na tupla: {tupla_num.count(9)}')

print(f'Posição do primeiro valor 3: {tupla_num.index(3)}')

for i in tupla_num:
    if (i % 2 == 0):
        print(f'{i} é par!')


    




