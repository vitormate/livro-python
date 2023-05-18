n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

apagar = n1

while apagar > n2:
    apagar -= n2

print(f'O resto da divsão entre {n1} / {n2} é {apagar}')