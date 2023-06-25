def validacao(texto, lista):
    return texto in lista

l = ['Vitor', 'Mat', 'Aguiar', 'Silva']
t = 'Mat'

print(validacao(t, l))