import sqlite3

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda')
resultado = cursor.fetchall()
for registro in resultado:
    print(f'Nome: {registro[0]} | Telefone: {registro[1]}')

cursor.close()
conexao.close()