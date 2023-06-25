import random

lista = ['vitor', 'preguiça', 'coruja', 'tartaruga']

indice = random.randrange(0, len(lista))

for x in range(100):
    print() 

digitadas = []
acertos = []
erros = 0
linha = list('X------')
x = 6

while True:
    senha=""
    
    for letra in lista[indice]:
        senha +=letra if letra in acertos else "." 
    
    print(senha)
    
    if senha == lista[indice]:
        print("Você acertou!")
        break
    
    tentativa = input("\nDigite uma letra:").lower().strip()
    
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue 
    else:
        digitadas += tentativa
        if tentativa in lista[indice]:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
            linha[x] = '|'
            x -= 1

    print(''.join(linha))
    

    if erros == 6:
        print("Enforcado!")
        print(f'A palavra era: {lista[indice]}!')
        break