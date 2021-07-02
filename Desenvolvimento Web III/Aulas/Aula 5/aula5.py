# Variáveis compostas: tuplas, listas e dicionários

# Tuplas são imutáveis, ou seja, não podem ser alteradas e são declaradas através de ()
lanche = ('Pizza', 'Suco', 'Pudim', 'Bolo')

print(lanche) #mostra a tupla inteira

print(lanche[1]) # mostra o elemento que se encontra na posição 1 (crescente)

print(lanche[-2]) # mostra de trás para frente

print(lanche[1:3]) # mostra os elementos entre a posição 1 e 3, sendo que a 3 não entra

print(lanche[1:]) # definindo somente a posição inicial

print(lanche[:3]) # definindo somente a posição final


for comida in lanche:
    print(f'Eu vou comer: {comida}')


# usando o range, com o mesmo resultado
for count in range(0, len(lanche)):
    print(f'Eu vou comer: {lanche[count]}')

# mostrando posição de cada elemento
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer: {comida} na posição {pos}')

# Em tuplas, o sinal + concatena
a = (2, 4, 6, 8)

b = (1, 3, 5, 7)

c = a + b
print(c)

# len - mostra a quantidade de elementos de uma string
print(len(c))

teste = 'Oi!'
print(len(teste))

for pos, letra in enumerate(teste):
    print(f'{letra} - posição: {pos}')

# count - conta quantas vezes um valor se repete
num = (1, 2, 3, 3, 4, 5, 6, 6, 6, 6, 7)

print(num.count(6))

# index - para saber a posição que o elemento se encontra, mostrando a primeira ocorrência
print(num.index(3))

# del - para deletar uma tupla inteira
del(c)



