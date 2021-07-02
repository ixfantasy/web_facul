import meumod
import moeda

#Questão 1
n = int(input('Digite um número:'))
print('Verificando se o número é primo:')
meumod.teste(n)

print('Agora, mostrando todos os números primos:')
meumod.primo(n)




#Questão 2
n = float(input('\nDigite um valor:'))
met = int(input('1. Aumentar // 2. Diminuir // 3. Dobro // 4. Metade:'))

if met == 1:
    aum = float(input('Digite o valor para aumentar:'))
    x = moeda.aumentar(n, aum)
    print(f'Novo total: {x}')
elif met == 2:
    dim = float(input('Digite o valor para diminuir:'))
    x = moeda.diminuir(n, dim)
    print(f'Novo total: {x}')
elif met == 3:
    x = moeda.dobro(n)
    print(f'O dobro é: {x}')
elif met == 4:
    x = moeda.metade(n)
    print(f'A metade é: {x}')
else:
    print('Entrada inválida!')




#Questão 3
print('[Valor antigo:]')
moeda.moeda(n)

print('[Valor atual:]')
moeda.moeda(x)




# Questão 4
n = int(input('Digite um número:'))
print(f'O valor Fibonacci é: {meumod.fib(n)}')

