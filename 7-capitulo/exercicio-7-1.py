first_string = input('First string: ')
sec_string = input('Second string: ')

if sec_string.lower() in first_string.lower():
    index = first_string.find(sec_string) + 1
    print(f'Result: {sec_string} find in {index} position of {first_string}')

# Resposta do site
# primeira = input("Digite a primeira string: ")
# segunda = input("Digite a segunda string: ")

# posição = primeira.find(segunda)

# if posição == -1:
#     print(f"'{segunda}' não encontrada em '{primeira}'")
# else:
#     print(f"{segunda} encontrada na posição {posição} de {primeira}")
