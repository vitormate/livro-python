lista = ['vitor', 'preguiça', 'coruja', 'tartaruga']

num = int(input("Digite um número:"))

indice = (num * 776) % len(lista)

for x in range(100):
    print() 

digitadas = []
acertos = []
erros = 0

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
    
    print("X==:==\nX : ")
    print("X O " if erros >= 1 else "X")
    linha2=""

    if erros == 2:
        linha2 = " | "

    elif erros == 3:
        linha2 = " \| "

    elif erros >= 4:
        linha2 = " \|/ "

    print(f"X{linha2}")
    linha3=""

    if erros == 5:
        linha3+=" /   "

    elif erros>=6:
        linha3+=" / \ "

    print(f"X{linha3}")
    print("X\n===========")

    if erros == 6:
        print("Enforcado!")
        print(f'A palavra era: {lista[indice]}!')
        break