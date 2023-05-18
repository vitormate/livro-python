num = int(input('Digite um número: '))

for i in range(3, num, 2):
    if num != 2 and num % 2 == 0:
        print(f'O número {num} não é primo')
        break
    
    if num % i == 0:
        print(f'O número {num} não é primo')
        break
else:
    if num < 2:
        print(f'O número {num} não é primo')
    else:
        print(f'O número {num} é primo')


# Resposta do livro
# n = int(input("Digite um número:"))
# if n < 0:
#     print("Número inválido. Digite apenas valores positivos")
# if n == 0 or n == 1:
#     print(f"{n} é um caso especial.")
# else:
#     if n == 2:
#         print("2 é primo")
#     elif n % 2 == 0:
#         print(f"{n} não é primo, pois 2 é o único número par primo.")
#     else:
#         x = 3
#         while(x < n):
#             if n % x == 0:
#                 break
#             x = x + 2
#         if x == n:
#             print(f"{n} é primo")
#         else:
#             print(f"{n} não é primo, pois é divisível por {x}")