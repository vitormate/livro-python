# n1 = int(input('First number: '))
# n2 = int(input('Second number: '))

# aux = 0 
# div = 0

# while aux < n1:
#     aux += n2
#     div += 1

# if aux > n1:
#     aux -= n2
#     div -=1

# print(f'Resul: {div}') 
# print(f'Rest: {n1 - aux}')

# Resposta do site(melhor)
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print(f"{dividendo} / {divisor} = {quociente} (quociente) {resto} (resto)")