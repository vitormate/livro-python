divida = float(input('Valor da Dívida: R$ '))
juros = float(input('Taxa de Juros: '))
prestacao = float(input('Valor a ser pago mensalmente: R$ '))

total_divida = divida
total_pago = 0
meses = 0

if (divida * (juros/100)) > prestacao:
    print('Sua dívida nunca será paga com esse pagamento')
else:
        
    while total_divida > total_pago:
        total_divida += total_divida*(juros/100)
        total_pago += prestacao
        meses += 1

total_juros = total_divida - divida

print(f'Levará {meses} meses para a dívida ser paga')
print(f'O valor total que será pago: R$ {total_divida:.2f}')
print(f'O valor total de juros será: R$ {total_divida-divida:.2f}')
