import sys

print(f'Número de parâmentros: {len(sys.argv)}')

for n,p in enumerate(sys.argv):
    print(f'Parâmetro {n} = {p}')