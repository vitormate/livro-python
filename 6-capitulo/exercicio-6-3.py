first = []
second = []
while True:
    x = int(input('Digite um elemento da lista (0 para sair): '))
    if x == 0:
        break
    first.append(x)

while True:
    x = int(input('Digite um elemento da lista (0 para sair): '))
    if x == 0:
        break
    second.append(x)

thirth = []

index = 0

while index < len(first):
    if first[index] not in second:
        thirth.append(first[index])
    index += 1

thirth.extend(second)

print(f'First list: {first}')
print(f'Second list: {second}')
print(f'Thirth list: {thirth}')