compras = []
while True:
    produto = input("Produto: ")
    if produto == "fim":
            break
    quantidade = int(input("Quantidade: "))
    preço = float(input("Preço: "))
    compras.append([produto, quantidade, preço])
    soma = 0.0
    for e in compras:
        print(f"{e[0]:20} {e[1]:5} {e[2]:5.2f} {e[1]*e[2]:6.2f}")
        soma += e[1] * e[2]
print(f"Total: {soma:7.2f}")
