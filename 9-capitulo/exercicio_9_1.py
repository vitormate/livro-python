import sys

argvs = sys.argv
nome_arquivo = argvs[1]

arquivo = open(nome_arquivo, 'r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close
