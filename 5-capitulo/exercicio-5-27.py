n = input('Digite um número: ')

lista = []

for i in range(len(n)-1, -1, -1):
    lista.append(n[i])

x = ''.join(lista)

if n == x:
    print(f'O número {n} é palíndromo')
else:
    print(f'O número {n} não é palíndromo')