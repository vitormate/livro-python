último = 10
fila1 = list(range(1, último+1))
fila2 = list(range(1, último+1))
while True:
    print("Digite F para adicionar um cliente ao fim da fila 1,")
    print("Digite G para adicionar um clinete ao fim da fila 2,")
    print("ou A para realizar o atendimento na fila 1 e B para fila 2. S para sair.")

    operação = input("Operação (F, G, A, B ou S):")
    x = 0
    sair = False
    while x < len(operação):
        if operação[x] == "A":
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação[x] == "B":
            if len(fila1) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação[x] == "F":
            último += 1  # Incrementa o ticket do novo cliente
            fila1.append(último)
        elif operação[x] == "G":
            último += 1  # Incrementa o ticket do novo cliente
            fila2.append(último)
        elif operação[x] == "S":
            sair = True
            break
        else:
            print(f"Operação inválida: {operação[x]} na posição {x}! Digite apenas F, G, A, B ou S!")
        x = x + 1
    if sair:
        break
    
print(fila1)
print(fila2)