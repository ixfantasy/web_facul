# -*- coding: utf-8 -*-

# Dicionário - Representado por chaves { }. São listas de associações compostas por uma chave e um valor correspondente
# nome_dicionario = {'chave: valor'}

frutas = {'A': 'abacaxi', 'B': 'banana'}
print(frutas)
print(frutas['A'])

# dicionário vazio
dados = dict()

dados = {'nome': 'Larissa', 'idade': 19}
print(dados['nome'])
print(dados['idade'])
print(f'A {dados["nome"]} tem {dados["idade"]} anos.')

dados['sexo'] = 'F'
print(dados)

# apagar elementos do dicionário - del
del dados['idade']
print(dados)

# keys - retornam as chaves
# values - retornam os valores
# items - retornam as chaves e os valores

filme = {'título': 'Star Wars', 'ano': 1997, 'diretor': 'George Lucas'}
print(filme)
print(filme.keys())
print(filme.values())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}.')

# dicionário + lista

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])

for n in range(0, len(brasil)):
    print(brasil[n]['sigla'])


# brasil.append(estado.copy())
