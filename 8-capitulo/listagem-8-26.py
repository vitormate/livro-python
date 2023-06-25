def soma(a,b):
    return a+b

def subtração(a,b):
    return a-b

def imprime(a,b, foper):
    print(foper(a,b)) 

imprime(5,4, soma) 
imprime(10,1, subtração) 