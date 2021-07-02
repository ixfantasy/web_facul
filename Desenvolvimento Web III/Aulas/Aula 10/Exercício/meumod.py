def teste(n):
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont = cont + 1
    if cont == 2:
        print('O número é primo!')
    else:
        print('O número não é primo!')


def primo(n):
    cont = 0
    x = 0

    for i in range(1, n+1):
        x = x + 1
        cont = 0

        for j in range(1, x+1):
            if x % j == 0:
                cont = cont + 1

        if cont == 2:
            print(x, end=',')


def res(n, i, f, x):
    if(i > n):
        return f
    x = f - x
    return res(n, i + 1, f + x, x)


def fib(n):
    i = 0
    f = 1
    x = 1
    return res(n - 2, i, f, x)

