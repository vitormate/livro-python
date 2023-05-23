L = [15,7,27,39]
p = int(input('Digite o valor a procurar na lista: '))
v = int(input('Digite outro valor para procurar na lista: '))
x = 0
achadoP = False
achadoV = False

while x < len(L):
    if L[x] == p:
        achadoP = True
        posP = x
    if L[x] == v:
        achadoV = True
        posV = x
    x += 1

if achadoP:
    print(f'{p} achado na posição {posP}')
else:
    print(f'{p} não encontrado')
if achadoV:
    print(f'{v} achado na posição {posV}')
else:
    print(f'{v} não encontrado')
if achadoP and achadoV:
    if posP < posV:
        print('p foi encontrado antes de v')
    else:
        print('v foi encontrado antes de p')
