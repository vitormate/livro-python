cigarros_dia = int(input('Cigarros por dia: '))
anos = int(input('Informe a quanto anos é fumante: '))

perda_min = anos * 365 * cigarros_dia * 10
perda_dias = perda_min / 60 / 24

print(f'Você perdeu um total de {perda_dias:.0f} dias de vida')