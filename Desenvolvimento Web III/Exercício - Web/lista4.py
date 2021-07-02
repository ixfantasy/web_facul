#Número 1.

n = int(input('Digite o primeiro número:'))

n2 = int(input('Digite o segundo número:'))

n3 = int(input('Digite o terceiro número:'))

n4 = int(input('Digite o quarto número:'))

if n > n2 and n > n3 and n > n4:
    print('A soma dos menores números é {}'.format(n2 + n3 + n4))
elif n2 > n and n2 > n3 and n2 > n4:
    print('A soma dos menores números é {}'.format(n + n3 + n4))
elif n3 > n and n3 > n2 and n3 > n4:
    print('A soma dos menores números é {}'.format(n + n2 + n4))
elif n4 > n and n4 > n2 and n4 > n3:
    print('A soma dos menores números é {}'.format(n + n2 + n3))



#Número 2.

import math

a = float(input('Digite o valor de A:'))

b = float(input('Digite o valor de B:'))

c = float(input('Digite o valor de C:'))

delta = (b**2) - (4 * a * c)

if delta < 0:
    print('Não existe raiz.')
elif delta == 0:
    x = (-b + (math.sqrt(delta))) / (2 * a)
    print('Existe uma raiz, de valor {}'.format(x))
else:
    x1 = (-b + (math.sqrt(delta))) / (2 * a)
    x2 = (-b - (math.sqrt(delta))) / (2 * a)
    print('Existe duas raízes, onde x¹ = {} e x² ={}'.format(x1, x2))



#Número 3.

x = int(input('Digite o valor de x:'))

if x < 1:
    print('Y = X = {}'.format(x))
elif x == 1:
    print('Y = 0')
else:
    print('Y = X² = {}'.format(x**2))



#Número 4.

numsala = input('Digite o número da sala:')

numcap = int(input('Digite a capacidade da sala:'))

nummat = int(input('Digite o número de alunos matriculados nesta sala:'))

x = numcap - nummat

if x > 0:
    print('O número da sala é: {}, sua capacidade é de: {}, o número de cadeiras ocupadas é: {}, o número de cadeiras livres é: {}, e a sala não está lotada'.format(numsala, numcap, nummat, x))
else:
    print('O número da sala é: {}, sua capacidade é de: {}, o número de cadeiras ocupadas é: {}, o número de cadeiras livres é 0, e a sala está lotada.'.format(numsala, numcap, nummat)) 



#Número 5.

salm = float(input('Digite o valor do salário mínimo:'))

dep = int(input('Digite o número de dependentes:'))

salf = float(input('Digite o valor do salário do funcionário:'))

if salf > (salm * 12):
    imp = salf * 0.2

    tax = imp * 0.04

    print('Imposto: {}, Salário: {}'.format(imp + tax, salf - (imp + tax)))
          
elif salf > (salm * 5):
    imp = salf * 0.08

    tax = imp * 0.04

    print('Imposto: {}, Salário: {}'.format(imp + tax, salf - (imp + tax)))
          
else:
    print('Não paga imposto de renda.')


    
#Número 6.

conta = input('Digite o número da conta do cliente:')

consumo = float(input('Digite a quantidade de consumo de água:'))

tipo = int(input('Residencial, digite 1. Comercial, digite 2. Industrial, digite 3.'))

if tipo == 1:
    print('Nº conta: {}, Gasto: R${}'.format(conta, (consumo * 0.05) + 5))
    
elif tipo == 2:
    print('Nº conta: {}'.format(conta))
    if (consumo - 80) > 0:
        print('Gasto: R${}'.format(500 + (consumo - 80) * 0.25))
    else:
        print('Gasto: R$500,00')
        
else:
    print('Nº conta: {}'.format(conta))
    if (consumo - 100) > 0:
        print('Gasto: R${}'.format(800 + (consumo - 100) * 0.04))
    else:
        print('Gasto: R$800,00') 

        

#Número 7.

num = int(input('Digite um número:'))

if num > 0:
    if (num % 3 == 0):
        print('O número é positivo e múltiplo de 3.')
    else:
        print('O número é positivo e não é múltiplo de 3.')
else:
    if (num % 3 == 0):
        print('O número é negativo e múltiplo de 3.')
    else:
        print('O número é negativo e não é múltiplo de 3.')



#Número 8.

a = int(input('Valor de A:'))

b = int(input('Valor de B:'))

c = int(input('Valor de C:'))

if ((b - c) < a and (b + c) > a) or ((a - c) < b and (a + c) > b) or ((a - b) < c and (a + b) > c):
    print('É possível formar um triângulo!')

    if (a == b) and (a == c):
        print('Triângulo equilátero!')
    elif ((a == b) and (a != c)) or ((b == c) and (b != a)) or ((a == c) and (a != b)):
        print('Triângulo isósceles!')
    else:
        print('Triângulo escaleno!')
else:
    print('Não é possível formar um triângulo!')



#Número 9.

nota1 = float(input('Nota 1:'))

nota2 = float(input('Nota 2:'))

nota3 = float(input('Nota 3:'))

med = (nota1 + nota2 + nota3) / 3

if med >= 6:
    print('Aprovado!')
else:
    print('Reprovado!')



#Número 10.

cod = input('Digite o código do aluno:')

a1 = float(input('AV1:'))

a2 = float(input('AV2:'))

a3 = float(input('AV3:'))

if (a1 > a2) and (a1 > a3):
    maximo = a1
    
    min1 = a2
    min2 = a3
elif (a2 > a1) and (a2 > a3):
    maximo = a2

    min1 = a1
    min2 = a3
elif (a3 > a1) and (a3 > a2):
    maximo = a3

    min1 = a1
    min2 = a2

med = ((maximo * 4) + (min1 * 3) + (min2 * 3)) / (4 + 3 + 3)

print('O código do aluno: {}\nAV1: {}, AV2: {}, AV3: {}\nMédia: {}'.format(cod, a1, a2, a3, med))

if med >= 5:
    print('Aprovado!')
else:
    print('Reprovado!')



#Número 11.

x = int(input('Digite um número:'))

if (x % 2 == 0):
    if x > 0:
        print('Este número é par e positivo.')
    else:
        print('Este número é par e negativo.')

else:
    if x > 0:
        print('Este número é ímpar e positivo.')
    else:
        print('Este número é ímpar e negativo.')



#Número 12.

sexo = input('Digite o seu sexo:')

h = float(input('Digite a sua altura:'))

if (sexo == 'm'):
    print('Seu peso ideal é: {}'.format((72.7 * h) - 58))
else:
    print('Seu peso ideal é: {}'.format((62.1 * h) - 44.7))



#Número 13.

a1 = float(input('Nota 1:'))

a2 = float(input('Nota 2:'))

a3 = float(input('Nota 3:'))

tipo = input('a para aritmética, b para ponderada:')

if tipo == 'a':
    print('A média aritmética é: {}'.format((a1 + a2 + a3) / 3))
else:
    print('A média ponderada é: {}'.format(((a1 * 3) + (a2 * 3) + (a3 * 4)) / (3 + 3 + 4)))




#Número 14.

peso1 = float(input('Digite o seu peso:'))

peso2 = float(input('Digite o peso de uma segunda pessoa:'))

peso3 = float(input('Digite o peso de uma terceira pessoa:'))

print('Seu peso: {}kg, Peso da pessoa 2: {}kg, Peso da pessoa 3: {}kg'.format(peso1, peso2, peso3))




#Número 15.

nota1 = float(input('AV1:'))

nota2 = float(input('AV2:'))

print('Média final: {}'.format((nota1 + nota2) / 2))



#Número 16.

dist = float(input('Digite a distância percorrida:'))

comb = float(input('Digite o combustível consumido:'))

print('A média de combustível consumido é: {}'.format(dist / comb))
