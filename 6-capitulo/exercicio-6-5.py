ultimo = 10
fila = list(range(1, ultimo+1))
print(f'\nExistem {len(fila)} clientes na fila')
print(f'Fila atual: {fila}')
print('Digite F para adicionar um cliente ao fim da fila,')
print('ou A para realizar o atendimento. S para sair.')
operacao = list(input('Operação (F, A ou S): '))

for item in operacao:
    if item == 'A':
        if (len(fila)) > 0:
            atendido = fila.pop(0)
            print(f'Cliente {atendido} atendido')
        else:
            print('Fila vazia! Ninguém para atender.')
    elif item == 'F':
        ultimo += 1
        fila.append(ultimo)
        print(f'Cliente {ultimo} foi adicionado a fila')
    elif item == 'S':
        break
    else:
        print('Operação inválida! Digite apenas F, A ou S!')

# Resposta do livro
# último = 10
# fila = list(range(1, último+1))
# while True:
#     print(f"\nExistem {len(fila)} clientes na fila")
#     print("Fila atual:", fila)
#     print("Digite F para adicionar um cliente ao fim da fila,")
#     print("ou A para realizar o atendimento. S para sair.")
#     operação = input("Operação (F, A ou S):")
#     x = 0
#     sair = False
#     while x < len(operação):
#         if operação[x] == "A":
#             if len(fila) > 0:
#                 atendido = fila.pop(0)
#                 print(f"Cliente {atendido} atendido")
#             else:
#                 print("Fila vazia! Ninguém para atender.")
#         elif operação[x] == "F":
#             último += 1  # Incrementa o ticket do novo cliente
#             fila.append(último)
#         elif operação[x] == "S":
#             sair = True
#             break
#         else:
#             print(f"Operação inválida: {operação[x]} na posição {x}! Digite apenas F, A ou S!")
#         x = x + 1
#     if sair:
#         break