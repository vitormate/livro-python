tabuada = 1
numero = 1
while tabuada <= 10:
    print(f'{tabuada} x {numero} = {tabuada*numero:>2}')
    numero += 1
    if numero == 11:
        numero = 1
        tabuada += 1