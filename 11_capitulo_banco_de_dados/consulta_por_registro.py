import sqlite3

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda')
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print(f'Nome: {resultado[0]} | Telefone: {resultado[1]}')

cursor.close()
conexao.close()

# Outra forma de fazer mesma coisa, porém
# sem precisar do fechamento
# import sqlite3
# from contextlib import closing
# with sqlite3.connect("agenda.db") as conexão:
#     with closing(conexão.cursor()) as cursor:		
#         cursor.execute("select * from agenda")
#         while True:
#             resultado=cursor.fetchone()
#             if resultado == None:
#                 break
#             print(f"Nome: {resultado[0]} | Telefone: {resultado[1]}")