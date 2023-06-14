primeira = list(input('1ª string: '))
segunda = list(input('2ª string: '))

new_string = []

for i in primeira:
    if i not in segunda:
        new_string.append(i)

new = ''.join(new_string)

print(f'3ª string: {new}')