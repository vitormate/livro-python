def soma(L):
    total=0
    for i in range(len(L)):
        total+=L[i]
    return total

L=[1,7,2,9,15]
print(soma(L))