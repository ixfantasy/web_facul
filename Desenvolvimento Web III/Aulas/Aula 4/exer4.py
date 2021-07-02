# Número 14.

i = int(input('Digite 1, 2 ou 3:'))

a = float(input('Digite um valor:'))

b = float(input('Digite outro valor:'))

c = float(input('Digite outro valor:'))

if (a > b) and (a > c):
    maior = a
    if (b < c):
        menor = b
        inter = c
    else:
        menor = c
        inter = b
        
elif (b > a) and (b > c):
    maior = b
    if(a < c):
        menor = a
        inter = c
    else:
        menor = c
        inter = a
        
elif (c > a) and (c > b):
    maior = c
    if (a < b):
        menor = a
        inter = b
    else:
        menor = b
        inter = a

if i == 1:
    print(f'Crescente: {menor}, {inter}, {maior}')
elif i == 2:
    print(f'Decrescente: {maior}, {inter}, {menor}')
else:
    print(f'Outro modo: {inter}, {maior}, {menor}')




# Número 15.

preco = float(input('Preço da lata:'))

raio = float(input('Raio:'))

h = float(input('Altura:'))

metro = 3.14 * (raio**2) * h

litro = metro / 3

lata = litro / 5

print(f'{lata} necessárias, e custo: {lata * preco}')




# Número 16.

preco = float(input('Preço inicial do carro:'))

opcao = ''

while opcao != 'z':
    opcao = input('Digite (a) - ar-condicionado, (b) - pintura metálica, (c) - vidro elétrico, (d) - direção hidráulica, (z) - para sair:')

    if (opcao == 'a'):
        preco = preco + 1750
        
    elif (opcao == 'b'):
        preco = preco + 800

    elif (opcao == 'c'):
        preco = preco + 1200

    elif (opcao == 'd'):
        preco = preco + 2000
else:
    print(f'Preço final: R${preco}')




# Número 17.

num = int(input('Digite um número:'))

n1 = num // 10000
aux = num % 10000
print(n1)

n2 = aux // 1000
aux = aux % 1000
print(n2)

n3 = aux // 100
aux = aux % 100
print(n3)

n4 = aux // 10
print(n4)

n5 = aux % 10
print(n5)

if (n1 == n5) and (n2 == n4):
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')




# Número 18.

prest = float(input('Prestação:'))

taxa = float(input('Taxa:'))

print(f'O valor de atraso é: {prest + (prest * (taxa / 100))}')




# Número 19.

raio = float(input('Raio:'))

h = float(input('Altura:'))

print(f'O volume é igual a {3.1415 * (raio**2) * h}')




# Número 20.

n1 = float(input('Nota 1:'))

n2 = float(input('Nota 2:'))

n3 = float(input('Nota 3:'))

print(f'Sua nota final é: {n1 + n2 + n3}')







