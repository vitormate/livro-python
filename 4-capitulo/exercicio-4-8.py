a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
operacao = input('''Qual operação você deseja?
+ para soma
- para subtração
* para multiplicação
/ para divisão
-> ''')

if operacao == '+':
    resultado = a+b
elif operacao == '-':
    resultado = a-b
elif operacao == '*':
    resultado = a*b
elif operacao == '/':
    resultado = a/b
else:
    print('Operação inválida! Digite uma das operações do menu!')
    resultado = 0

print(f'Resultado: {resultado}')