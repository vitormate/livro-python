primeira = []
segunda = []
while True:
    x = int(input('Elementos da primeira lista (0 para sair): '))
    
    if x == 0:
        break
    
    primeira.append(x)
while True:
    y = int(input('Elemento da segunda lista (0 para sair): '))
    
    if y == 0:
        break

    segunda.append(y)

terceira = primeira[:] + segunda[:]
print(terceira)
