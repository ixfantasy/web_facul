# Modularização: a ideia é reutilizar códigos; facilita a manutenção.
import meumod

a = int(input('Digite um número:'))
b = int(input('Digite outro número:'))

c = meumod.soma(a, b)
print(c)

print(f'A multiplicação é: {meumod.mult(a, b)}')

print('O fatorial é: {}'.format(meumod.fatorial(a)))

print('O dobro é: {}'.format(meumod.dobro(a)))

print(f'O triplo é: {meumod.triplo(a)}')

meumod.mensagem()

import random

n = random.randint(1, 10)
print(f'Número aleatório: {n} // Fatorial: {meumod.fatorial(n)}')

# Importar com "from"
from meumod import dobro, triplo

n = random.randint(1, 5)

print(f'Número aleatório: {n} // Dobro: {dobro(n)} // Triplo: {triplo(n)}')

# Trazer todas as funções do módulo com "from"
from meumod import *
