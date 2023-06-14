first_string = input('First string: ')
sec_string = input('Second string: ')

new_string = []

for letter in sec_string:
    if letter in first_string:
        new_string.append(letter)

print(''.join(new_string))

# Estou percebendo que não estou tratando 
# as exceções, começar a tratar.
# Resposta do site
# primeira = input("Digite a primeira string: ")
# segunda = input("Digite a segunda string: ")

# terceira = ""

# for letra in primeira:
#     if letra in segunda and letra not in terceira:
#         terceira += letra

# if terceira == "":
#     print("Caracteres comuns não encontrados.")
# else:
#     print(f"Caracteres em comum: {terceira}")