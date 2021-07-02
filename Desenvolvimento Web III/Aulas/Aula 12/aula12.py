# importar o banco de dados - import
import mysql.connector

# fazer a conexão com o banco de dados
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'aula11'
    )

cursor = conexao.cursor()
"""print(conexao)"""

# criando a database - create database
"""cursor.execute('create database aula11')"""

# mostrando as databases criadas - show databases
"""cursor.execute('show databases') 
for x in cursor:
    print(x)"""


# criando uma tabela - create table
"""cursor.execute('create table usuario(cod_usuario int(10) primary key auto_increment, nome varchar(50), email varchar(70))')
"""

# mostrando as tabelas criadas - show tables
"""cursor.execute('show tables')
for x in cursor:
    print(x)"""

# descrevendo a tabela 'usuario' - desc ou describe
"""cursor.execute('describe usuario')
for x in cursor:
    print(x)"""


# inserindo uma linha na tabela - insert into + execute
"""sql = 'insert into usuario(nome, email) values ("Larissa", "larissa@gmail.com")'
cursor.execute(sql)"""

# para confirmar as alterações
"""conexao.commit()"""

# contagem de registros adicionados
"""print(cursor.rowcount, 'Registro(s) inserido(s).')
"""


# inserindo várias linhas de uma vez - insert into + executemany
"""sql = 'insert into usuario(nome, email) values (%s, %s)'
values = [
    ("Ana", "ana@gmail.com"),
    ("Bob", "bob@gmail.com"),
    ("Cat", "cat@gmail.com"),
    ("Angel", "angel@gmail.com"),
    ("Patrick", "patrick@gmail.com"),
    ("Cascudo", "cascudo@gmail.com"),
    ("Pérola", "perola@gmail.com"),
    ("Luna", "luna@gmail.com"),
    ("Lily", "lily@gmail.com"),
    ("Pikachu", "pikachu@gmail.com")
    ]

cursor.executemany(sql, values)
conexao.commit()
print(cursor.rowcount, 'Registro(s) inserido(s).')
"""

"""
sql = 'insert into usuario(nome, email) values ("Ash", "ash@gmail.com")'
cursor.execute(sql)
conexao.commit()"""

# para mostrar o id da última linha adicionada - lastrowid
"""print('O último registro inserido, ID:', cursor.lastrowid)"""


# para selecionar os registros da tabela - select
"""cursor.execute("select * from usuario")"""

# método que busca todas as linhas da última instrução executada
"""result = cursor.fetchall()

for x in result:
    print(x)"""


# para retornar a 1ª linha do resultado
"""cursor.execute('select * from usuario')
result = cursor.fetchone()
print(result)"""


# selecionar com condição - select ... where
"""cursor.execute('select * from usuario where cod_usuario = 3')
result = cursor.fetchall()
for x in result:
    print(x)"""

"""cursor.execute('select * from usuario where nome like "%a"')
result = cursor.fetchall()
for x in result:
    print(x)"""

"""cursor.execute('select email from usuario where nome like "_a%"')
result = cursor.fetchall()
for x in result:
    print(x)"""


# para classificar em ordem crescente (asc) ou decrescente (desc)
"""cursor.execute('select * from usuario order by nome asc')
result = cursor.fetchall()
for x in result:
    print(x)"""

"""cursor.execute('select * from usuario order by nome desc')
result = cursor.fetchall()
for x in result:
    print(x)"""


# para deletar registros/linhas - delete
"""cursor.execute('delete from usuario where cod_usuario between 2 and 4')
conexao.commit()
print(cursor.rowcount, 'Registro(s) apagado(s).')"""

sql = 'delete from usuario where cod_usuario in (%s, %s)'
cursor.execute(sql, (5, 12))
conexao.commit()
print(cursor.rowcount, 'Registro(s) deletado(s).')



