qtde_kwh = int(input('Quantidade de kWh consumida: '))
instalacao = input('''Tipo de instalação:
R para residências
I para indústrias
C para comércios
-> ''')

if instalacao == 'R':
    if qtde_kwh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif instalacao == 'C':
    if qtde_kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.6
elif instalacao == 'I':
    if qtde_kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.6
else:
    print('Instalação inválida! Escolha uma especificada no menu!')
    preco = 0

print(f'Preço da conta: R$ {qtde_kwh*preco}')