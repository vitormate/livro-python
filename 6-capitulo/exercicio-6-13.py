T = [-10,-8,0,1,2,5,-2,-4]
menor = T[0]
maior = T[0]
soma = 0

for item in T:
    if item < menor:
        menor = item
    if item > maior:
        maior = item
    soma += item

media = soma / len(T)
print(f'Temperatura mínima: {menor}')
print(f'Temperatura máxima: {maior}')
print(f'Temperatura média: {media}')