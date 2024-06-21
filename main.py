from CALCULADORA.menu import *
from CALCULADORA import *

from time import sleep
while True:
    resposta = menuDeOpções(['Somar', 'Subtrair', 'Dividir', 'Multiplicar', 'Tabuada', 'Baskara', 'Fatorial', 'Sair do Sistema'])
    if resposta == 1:
        titulo('Você escolheu somar')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        print(f'A soma entre {n1} e {n2} é: {soma(n1, n2)}')

    elif resposta == 2:
        titulo('Você escolheu subtrair')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        print(f'A subtração entre {n1} e {n2} é: {subtração(n1, n2)}')

    elif resposta == 3:
        titulo('Você escolheu dividir')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        print(f'A divisão entre {n1} e {n2} é: {divisão(n1, n2)}')

    elif resposta == 4:
        titulo('Você escolheu Multiplicar')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        print(f'A multiplicação entre {n1} e {n2} é: {multiplicação(n1, n2)}')

    elif resposta == 5:
        titulo('Tabuada')
        print(tabuada(0))

    elif resposta == 6:
        titulo('Baskara')
        a1 = int(input('Digite o valor de "a": '))
        b2 = int(input('Digite o valor de "b": '))
        c3 = int(input('Digite o valor de "c": '))
        print(baskara(a1, b2, c3))

    elif resposta == 7:
        titulo('fatorial')
        n1 = int(input('Digite um número para fatorar: '))
        print(f'O fatorial de {n1} é: ', end='')
        print(fatorial(n1, show=True))


    elif resposta == 8:
        titulo('..........Saindo do Sistema..........')
        break
    else:
        print('\033[0;31;40mERRO: Digite uma opção válida.\033[m')
        sleep(2)
    sleep(2)
sleep(2)