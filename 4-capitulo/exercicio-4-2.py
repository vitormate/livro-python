vel_carro = int(input('Velocidade do carro: '))

if vel_carro > 80:
    multa = (vel_carro - 80) * 5
    print(f'Multado: R$ {multa:.2f}')
if vel_carro <= 80:
    print('Velocidade correta')