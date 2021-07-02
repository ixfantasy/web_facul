# -*- coding: utf-8 -*-
# Listas: parecida com tupla, com a diferença que é mutável e é criada com [].
nome = ['Thereza', 'Larissa', 'Jorbe', 'Carol', 'Pedro']
print(nome)
print(f'O nome que está na posição 3 é: {nome[3]}')

nome[0] = 'Maria'
print(nome)

num = [1, 2, 3, 4]
print(num)
num[2] = 5
print(num)

#min() - menor número // max() - maior número
num = [5, 7, 2, 4, 10, 3, 8]
print(min(num))
print(max(num))


#sum() - somar todos os elementos
num = [1, 2, 3]
print(sum(num))


#append() - para adicionar elementos no final da lista
num = [1, 2, 3]
num.append(5)
print(num)


#insert(posição, elemento) - insere elementos em qualquer posição da lista
num.insert(1, 10)
print(num)


#pop() - apaga o último elemento da lista // para escolher a posição, pop (posição)
num = [1, 2, 3]
num.pop()
print(num)

num = [1, 2, 3]
num.pop(0)
print(num)


#del() - apaga a lista inteira ou remove um elemento da lista
num = [1, 2, 3]
del num[0]
print(num)

"""del(num)
print(num)"""

num = [1, 2, 3, 4, 5, 6]
del num[2:5]
print(num)


#remove() - apaga pelo elemento
lista = ['Oi', 'Tchau']
lista.remove('Oi')
print(lista)


#list - criar listas usando range
num = list(range(4, 11))
print(num)


#len() - tamanho da string
print(len(num))


#sort() - ordenar em ordem crescente
num = [3, 2, 5, 1]
num.sort()
print(num)


num = [3, 2, 5, 1]
num = sorted(num)
print(num)


#reverse() - ordenar em ordem decrescente
num.reverse()
print(num)

num.sort(reverse=True)
print(num)


#criando listas vazias:
#Método 1: nome_variavel = list()
#Método 2: nome_variavel = []
lista1 = list()
lista2 = []

print(f'Lista inicial: {lista1}')
lista1.append(5)
lista1.append(2)
lista1.append(1)
print(f'Lista final: {lista1}')

for n in range (0, len(lista1)):
    print(lista1[n])

for pos, n in enumerate(lista1):
    print(f'Posição {pos}: {n}')

for n in range(0, 1):
    lista2.append(int(input('Digite o valor:')))
print(lista2)

#criar cópia da lista: [:], permitindo que b seja alterada sem alterar a
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(a)
print(b)

a = [2, 3, 4, 7]
b = a
print(a)
print(b)


#Lista composta: uma lista dentro da outra
pessoas = [['Thereza', 25], ['Larissa', 20], ['Carol', 18]]
print(pessoas)
print(pessoas[0][0])
print(pessoas[1][1])

teste = list() #criando lista vazia
teste.append('Pedro')
teste.append(20)

galera = list() #criando outra lista vazia
galera.append(teste[:]) #cria cópia onde uma lista não afeta/altera outra

teste[0] = 'Mario'
teste[1] = 12

galera.append(teste[:])

print(galera)

