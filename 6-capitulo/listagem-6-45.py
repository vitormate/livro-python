tabela = {'Alface': 0.45,
        'Batata': 1.20,
        'Tomate': 2.30,
        'Feijão': 1.50}

print(tabela['Alface'])
tabela['Alface'] = 0.50
print(tabela['Alface'])
print()

print(tabela)
del tabela['Batata']
tabela['Cebola'] = 1.00
print(tabela)

print(list(tabela.keys()))
print(list(tabela.values()))
print(tabela.items())
