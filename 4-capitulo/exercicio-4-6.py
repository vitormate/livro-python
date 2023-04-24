distancia = int(input('Informa a distância a percorrer: '))

if distancia <= 200:
    valor_km = 0.5
else:
    valor_km = 0.45

valor_viagem = distancia * valor_km

print(f'O valor da viagem é: R$ {valor_viagem:.2f}')
