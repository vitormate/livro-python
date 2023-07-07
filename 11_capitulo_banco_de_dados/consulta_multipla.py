import sqlite3

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda where nome = "Nilo"')
resultado = cursor.fetchall()
for registro in resultado:
    print(f'Nome: {registro[0]} | Telefone: {registro[1]}')

cursor.close()
conexao.close()