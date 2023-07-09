import sqlite3

nome = input('Digite um nome: ')
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
# Essa forma de fazer o select é ruim, pq da brecha para SQL Injection
# cursor.execute(f'select * from agenda where nome = "{nome}"')
# Forma melher de fazer um select
cursor.execute(f'select * from agenda where nome = ?', (nome,))
resultado = cursor.fetchall()
for registro in resultado:
    print(f'Nome: {registro[0]} | Telefone: {registro[1]}')

cursor.close()
conexao.close()