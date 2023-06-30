LARGURA=79
entrada=open("entrada.txt")
for linha in entrada.readlines():
    if linha[0]==";":
        continue
    elif linha[0]==">":
        print(linha[1:].rjust(LARGURA))
    elif linha[0]=="*":
        print(linha[1:].center(LARGURA))
    elif linha[0]=="=":
        c = "="
        print(c*40)
    elif linha[0]==".":
        input('Digite algo: ')
        print()
    else:
        print(linha)
entrada.close()