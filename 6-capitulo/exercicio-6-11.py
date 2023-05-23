L = []
while True:
    n = int(input('Digite um número (0 sai): '))
    if n == 0:
        break
    L.append(n)

for item in L:
    print(item)

# O primeiro while não pode ser transformado em for
# Porque antes adicionando um número indeterminado de valores
# na nossa lista