soma = 0
x = 0
while True:
    n = int(input('Digite um número ou 0 para sair: '))
    if n == 0:
        break
    soma += n
    x += 1

print(f'Foram digitados {x} números')
print(f'A soma dos números digitados: {soma}')
print(f'A média dos números digitados: {soma/x}')
