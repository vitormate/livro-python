expressao = input('Digite os parênteses para verificar: ')
x = 0
pilha = []

while x < len(expressao):
    if expressao[x] == '(':
        pilha.append('(')
    if expressao[x] == ')':
        if (len(pilha)) > 0:
            pilha.pop(-1)
        else:
            pilha.append(')')
            break
    x += 1

if (len(pilha)) == 0:
    print('OK')
else:
    print('Erro')