pares = open('pares.txt', 'r')
inverso = open('inverso.txt', 'w')

lista = pares.readlines()
lista.reverse()
for item in lista:
    inverso.write(item)

pares.close()
inverso.close()