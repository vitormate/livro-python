salario = float(input('Salário: '))
aumento = float(input('Porcentagem de aumento: '))

porcentagem = aumento / 100

valor_aumento = salario * porcentagem
novo_salario = salario + valor_aumento

print(f'O valor de aumento é: R$ {valor_aumento:.2f}')
print(f'O novo salário é: R$ {novo_salario:.2f}')