salario = float(input('Informe o salário: '))

if salario > 1250:
    aumento = salario * (10/100)
if salario <= 1250:
    aumento = salario * (15/100)

print(f'O aumento foi: R$ {aumento:.2f} para o salario: R$ {salario:.2f}')

# Resolução do site de exercícios resolvidos
# salário = float(input("Digite seu salário: "))
# pc_aumento = 0.15
# if salário > 1250:
#     pc_aumento = 0.10
# aumento = salário * pc_aumento
# print(f"Seu aumento será de: R$ {aumento:7.2f}")