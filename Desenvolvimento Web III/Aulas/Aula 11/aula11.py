import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost", # definir host
    user = "root", # definir o usuário (root é o padrão)
    password = "", # definir uma senha (opcional)
    database = "aula10manhã"
    )

cursor = conexao.cursor() # verificar se a conexão foi feita
print(conexao)

"""cursor.execute("show databases")
for n in cursor:
    print(n)""" # mostrando todas as databases

"""cursor.execute("create database aula10manhã")""" # criar uma database


"""cursor.execute("create table aluno(matricula int(10) primary key auto_increment,nome varchar(40) not null,idade int(3), email varchar(50))")""" #criar uma tabela


"""cursor.execute("insert into aluno(nome, idade, email) values ('Thereza', 40, 'prof.thereza.gondim@soulasalle.com.br')")
conexao.commit()
print(cursor.rowcount, "registro(s) inserido(s)") """ # adicionando uma linha



"""sql = "insert into aluno(nome, idade, email) values (%s, %s, %s)"
val = [
    ('Banana', 10, 'banana@gmail.com'),
    ('Uva', 20, 'uva@gmail.com'),
    ('Maçã', 30, 'maça@gmail.com'),
    ('Laranja', 15, 'laranja@gmail.com')
    ]
cursor.executemany(sql, val)
conexao.commit()
print(cursor.rowcount, 'registro(s) inserido(s)')""" # para executar e adicionar várias linhas


