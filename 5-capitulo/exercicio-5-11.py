deposito_inicial = float(input('Depósito Inicial: R$ '))
taxa_juros = float(input('Taxa de Juros: '))
x = 1
total_conta = deposito_inicial
while x <= 24:
    total_conta += total_conta*(taxa_juros/100)
    print(f'Saldo da conta ao final do mês {x}: R$ {total_conta:.2f}')
    x += 1
total_ganho = total_conta - deposito_inicial
print(f'Total ganho: R$ {total_ganho:.2f}')