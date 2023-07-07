import sqlite3

conexao = sqlite3.connect('precos.db')
cursor = conexao.cursor()
cursor.execute('select * from precos')

while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print(f'Produto: {resultado[0]} | Preço: {resultado[1]:.2f}')

cursor.close()
conexao.close()