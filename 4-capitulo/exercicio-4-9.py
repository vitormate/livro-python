valor_casa = float(input('Valor da Casa: R$ '))
salario = float(input('Salário: R$ '))
anos = int(input('Anos para pagar: '))

prestacao = valor_casa / (anos * 12)

if prestacao < salario*0.3:
    print(f'Emprestimo aprovado! Valor da prestação: R$ {prestacao:.2f}')
else:
    print('Emprestimo negado!')