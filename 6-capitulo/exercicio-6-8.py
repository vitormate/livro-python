L = [15,7,27,39]
p = int(input('Digite o valor a procurar na lista: '))
x = 0

while x < len(L) and L[x] != p:
    x += 1

if x < len(L):
    print(f'{p} achado na posição {x}')
else:
    print(f'{p} não encontrado')
