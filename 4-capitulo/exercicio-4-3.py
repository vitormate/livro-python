a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))

if a > b > c:
    print(f'{a} é o maior e {c} é o menor')
if a > c > b:
    print(f'{a} é o maior e {b} é o menor')
if b > a > c:
    print(f'{b} é o maior e {c} é o menor')
if b > c > a:
    print(f'{b} é o maior e {a} é o menor')
if c > a > b:
    print(f'{c} é o maior e {b} é o menor')
if c > b > a:
    print(f'{c} é o maior e {a} é o menor')


# Resolução do site de exercícios resolvidos
# a = int(input("Digite o primeiro valor:"))
# b = int(input("Digite o segundo valor:"))
# c = int(input("Digite o terceiro valor:"))
# maior = a
# if b > a and b > c:
#     maior = b
# if c > a and c > b:
#     maior = c
# menor = a
# if b < c and b < a:
#     menor = b
# if c < b and c < a:
#     menor = c
# print(f"O menor número digitado foi {menor}")
# print(f"O maior número digitado foi {maior}")