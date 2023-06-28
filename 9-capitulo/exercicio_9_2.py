import sys

argvs = sys.argv
nome_arquivo = argvs[1]
inicio = int(argvs[2])
fim = int(argvs[3])

arquivo = open(nome_arquivo, 'r')
for linha in arquivo.readlines()[inicio-1:fim]:
    print(linha)
arquivo.close
