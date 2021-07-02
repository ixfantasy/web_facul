# Laço de Repetição: FOR

nome = ['Pedro', 'Jorbe', 'Larissa', 'Carol'] # vetor / lista
for n in nome :
    print(n) # n é o contador

# printa a frase com cada item separadamente
comida = ['Arroz', 'Feijão', 'Bife', 'Batata frita']
for x in comida :
    print('Estou cozinhando:', x)

# mostrar de 0 a 9
for c in range(0, 10) : #range define a posição inicial e final
    print(c)

# printa a frase 6 vezes
for b in range(0, 6):
    print('Olá, boa tarde!')

# mostrar se o número é par ou ímpar
for i in range(10):
    if (i % 2 == 0):
        print('{}: O número é par!'.format(i))
    else:
        print('{}: O número é ímpar!'.format(i))

for i in comida:
    print(i)
else:
    print('Que gostoso!')

# Laço de Repetição: WHILE

cont = 0
while cont < 5:
    print(cont)
    cont = cont + 1


cont = 0
while cont <= 3:
    print('Estamos dentro de um loop!')
    cont = cont + 1
else: # um retorno ao finalizar o loop
    print('Entramos em um else!')

senha = 0
while (senha != 123):
    senha = int(input('Digite a senha:'))
    if (senha != 123):
        print('Acesso negado!')
else:
    print('Acesso liberado!')


# Outro método de escrever print: FSTRING

nome = 'Banana'
idade = 25

print('A {} tem {} anos!'.format(nome, idade))

print(f'A {nome} tem {idade} anos!')

print(f'A {nome:20} tem {idade} anos!') # adiciona um espaço de 20 caracteres após o nome

print(f'A {nome:-^20} tem {idade} anos!') # para inserir traços antes e depois do nome

print(f'A {nome:>30} tem {idade} anos!') # centralizar em X caracteres

print(f'A {nome.upper()} tem {25 + 3} anos!')




