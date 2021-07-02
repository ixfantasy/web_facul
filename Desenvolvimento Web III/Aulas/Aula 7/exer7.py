# Número 90
aluno = dict()

aluno['nome'] = input('Digite o nome do aluno:')

aluno['média'] = input('Digite a média do aluno:')

print(aluno)




# Número 91
import random

from operator import itemgetter

dados = {'Jogador1': random.randint(1, 6), 'Jogador2': random.randint(1, 6), 'Jogador3': random.randint(1, 6), 'Jogador4': random.randint(1, 6)}
print(dados)

print(sorted(dados.items(), key=itemgetter(1), reverse=True))




# Número 92

cadastro = dict()

cadastro['nome'] = input('Digite o seu nome:')
cadastro['nascimento'] = int(input('Digite o ano de nascimento:'))
cadastro['idade'] = 2020 - cadastro['nascimento']
cadastro['carteira'] = int(input('Digite o número da carteira de trabalho:'))

if cadastro['carteira'] != 0:
    cadastro['contratação'] = int(input('Digite o ano de contratação:'))
    cadastro['salário'] = int(input('Digite o seu salário:'))

    sexo = input('Digite o seu sexo, M ou F:')

    if sexo == 'M':
        x = 2020 - cadastro['contratação']
        cadastro['IdadeAposentadoria'] = (35 - x) + cadastro['idade']
    else:
        x = 2020 - cadastro['contratação']
        cadastro['IdadeAposentadoria'] = (30 - x) + cadastro['idade']
print(cadastro)
