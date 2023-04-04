preco = float(input('Preço da mercadoria: '))
desconto = float(input('Valor de desconto: '))

novo_preco = preco - (preco * desconto / 100)

print(f'O novo preço é: R$ {novo_preco:.2f}')