texto = input('Digite uma frase: ')
dicio = {}
for elem in texto:
    if elem.isalpha():
        dicio[elem] = texto.count(elem)

print(dicio)