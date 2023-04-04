km_percorrido = int(input('Quilômetros percorridos: '))
dias = int(input('Dias de aluguel do carro: '))

valor_carro = dias * 60
valor_km = km_percorrido * 0.15

total = valor_carro + valor_km

print(f'R$ {total:.1f}')