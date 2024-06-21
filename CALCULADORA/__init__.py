def soma(a, b):
    s = a + b
    return s


def subtração(a, b):
    sub = a - b
    return sub

def divisão(a, b):
    div = a / b
    return div

def multiplicação(a, b):
    mult = a * b
    return mult

def fatorial(n=1, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:

            if c > 1:
                print(f'{c} x ', end='')
            if c == 1:
                print(f'{c} = ', end='')
        f = f * c
    return f

def baskara(a, b, c):
    delta = (b ** 2) - 4 * a * c

    if delta < 0:
        print('esta equação não possui raízes reais')
    if delta == 0:
        raiz1 = (- b + (delta ** 0.5)) / (2 * a)
        raiz2 = (- b - (delta ** 0.5)) / (2 * a)
        print(f'a raiz dupla desta equação é {raiz1}')
    if delta > 0:
        raiz1 = (- b + (delta ** 0.5)) / (2 * a)
        raiz2 = (- b - (delta ** 0.5)) / (2 * a)
        if raiz1 < raiz2:
            print(f'as raízes da equação são x¹:{raiz1} e x²:{raiz2}')
        else:
            print(f'as raízes da equação são x¹:{raiz2} e x²:{raiz1}')
    return f'O delta é {delta}'



def tabuada(n):
    while True:
        print('=' * 40)
        n = int(input('Quer ver a tabuada de qual valor? '))
        print('=' * 40)
        for c in range(1, 11):
            t = n * c
            print(f'{c} x {n} = {t}')
        return f'Esta é a tabuada de {n} '
