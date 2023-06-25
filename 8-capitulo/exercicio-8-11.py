def validacao(texto, minimo, maximo):
    return len(texto) > minimo and len(texto) < maximo

print(validacao('Vitor', 1, 4))

