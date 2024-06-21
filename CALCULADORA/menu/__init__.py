def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[32mDigite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

def linha(tam=50):
    return '=' * tam


def titulo(txt):
    print(linha())
    print(txt.center(50))



def menuDeOpções(lista):
    titulo('\033[40mMENU DE OPÇÕES\033[m')
    c = 1
    for item in lista:
        print(f'\033[32m{c}\033[m-\033[35m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Escolha sua opção: ')
    return opc
