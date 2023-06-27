def imprimir(lista, nivel=0):
    espaco = '  '
    for item in lista:
        if type(item)==list:
            imprimir(item, nivel + 1)
        else:
            if nivel == 0:
                print(f'{item}')
            else:
                print(f'{espaco*nivel}{item}')

L = [1, [2,3,4,[5,6,7]]]

imprimir(L)