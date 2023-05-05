valor = 0

while True:
    codigo = int(input('Digite o código do produto ou 0 para sair: '))
    
    if codigo == 0:
        break
    elif codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco == 1
    elif codigo == 3:
        preco = 4
    elif codigo == 5:
        preco = 7
    elif codigo == 9:
        preco = 8
    else:
        print('Código inválido')
    
    qtde = int(input('Digite a quantidade do produto: '))

    valor = valor + (qtde * preco)

print(f'Valor a pagar: R$ {valor:.2f}')

