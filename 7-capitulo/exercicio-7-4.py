text = input('String: ')

lista = []

for i in text:
    if i not in lista:
        lista.append(i)

print('Resultado: ')
for i in lista:
    print(f'{i}: {text.count(i)}x')

# Resposta do site
# sequencia = input("Digite a string: ")

# contador = {}

# for letra in sequencia:
#     contador[letra] = contador.get(letra, 0) + 1

# for chave, valor in contador.items():
#     print(f"{chave}: {valor}x")