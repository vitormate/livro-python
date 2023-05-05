x = 1
soma = 0
while x <= 5:
    n = int(input(f'Digite o {x}° número: '))
    soma += n
    x += 1
print(f'Média: {soma/5}')