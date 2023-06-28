impares = open('impares.txt', 'w')
pares = open('pares.txt', 'w')

for n in range(0, 1000):
    if n % 2 == 0:
        pares.write(f'{n}\n')
    else:
        impares.write(f'{n}\n')

impares.close()
pares.close()