import sys

argvs = sys.argv
arquivo1 = argvs[1]
arquivo2 = argvs[2]

multiplo = open(arquivo1, 'r')
impar = open(arquivo2, 'r')
novo_arquivo = open('multiplo_impar.txt', 'w')

for i in multiplo.readlines():
    novo_arquivo.write(i)
for j in impar.readlines():
    novo_arquivo.write(j)

multiplo.close()
impar.close()
novo_arquivo.close()

# Resposta do Site
# import sys

# # Verifica se os parâmetros foram passados
# if len(sys.argv) != 4:  # Lembre-se que o nome do programa é o primeiro da lista
#     print("\nUso: e09-04.py primeiro segundo saída\n\n")
# else:
#     primeiro = open(sys.argv[1], "r")
#     segundo = open(sys.argv[2], "r")
#     saída = open(sys.argv[3], "w")

#     # Funciona de forma similar ao readlines
#     for l1 in primeiro:
#         saída.write(l1)
#     for l2 in segundo:
#         saída.write(l2)

#     primeiro.close()
#     segundo.close()
#     saída.close()