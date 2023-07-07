import sqlite3

dados = [('Street Fighter 6', 249.00),
         ('Dark Souls: Remasthered', 119.90),
         ('Sekiro', 180.50)]

conexao = sqlite3.connect('precos.db')
cursor = conexao.cursor()
cursor.execute('''
    create table precos(
        produto text,
        preco real)
''')

cursor.executemany('''
    insert into precos (produto, preco)
        values (?, ?)
        ''', dados)

conexao.commit()
cursor.close()
conexao.close()