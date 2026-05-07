#importaçoes

#importa o sqlite(banco de dados)
import sqlite3

#criar banco de dados
conn = sqlite3.connect('estoque.db', check_same_thread=False)
cursor = conn.cursor()

#tabela de usuarios
cursor.execute('''
create table if not exists usuarios (
    id integer primary key autoincrement,
    nome TEXT,
    email TEXT,
    senha TEXT
)
''')

#tabela de produtos
cursor.execute('''
create table if not exists produtos (
    id integer primary key autoincrement,
    nome TEXT,
    quantidade INTEGER,
    usuario_id INTEGER
)
''')

#salva as tabelas no banco de dados
conn.commit()
