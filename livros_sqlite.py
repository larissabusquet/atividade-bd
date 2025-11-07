import sqlite3

# Criando a tabela de livros.

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL UNIQUE,
        autor TEXT,
        ano INTEGER,
        genero TEXT,
        disponivel INTEGER DEFAULT 1
    )
''')
conn.commit()
conn.close()

# Inserir livros fictícios na tabela.

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

livros = [
    ("A hora da estrela", "Clarice Lispector", 1977, "Romance", 1),
    ("Dom Casmurro", "Machado de Assis", 1899, "Romance", 0),
    ("Mudar: Método", "Édouard Louis", 2024, "Ficção doméstica", 1),
    ("A Fúria dos Reis", "George R. R. Martin", 1998, "Fantasia", 0),
    ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia", 1)
]

for livro in livros:
    cursor.execute('''
        INSERT OR IGNORE INTO Livros (titulo, autor, ano, genero, disponivel)
        VALUES (?, ?, ?, ?, ?)
    ''', livro)
    print(f" Inserido: {livro[0]} - {livro[1]} ({livro[2]})")
conn.commit()
conn.close()
print("Livros inseridos com sucesso na tabela 'Livros'.")

# Consultar os livros na tabela.

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM Livros WHERE disponivel = 1')
livros_disponiveis = cursor.fetchall()
print("Livros disponíveis para empréstimo:")
for livro in livros_disponiveis:
    print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Gênero: {livro[4]}")
conn.close()

# Atualizar disponibilidade de um livro.

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()
cursor.execute('''
    UPDATE Livros
    SET disponivel = 0
    WHERE titulo = ?
''', ("A hora da estrela",))
conn.commit()
print("Disponibilidade atualizada em 'A hora da estrela'.")
conn.close()

# Ordenar por ano

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Livros ORDER BY ano DESC')
livros_ordenados = cursor.fetchall()
print("Livros ordenados por ano de publicação (do mais recente ao mais antigo):")
for livro in livros_ordenados:
    print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Gênero: {livro[4]}, Disponível: {livro[5]}")
conn.close()

# Deletar um livro antigo da tabela. (Não vi que era por data, então to adicionando como outra feature)

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()
cursor.execute('''
    DELETE FROM Livros
    WHERE ano < 1940
''')
conn.commit()
print("Livro 'Dom Casmurro' deletado da tabela.")
conn.close()

# Criar tabela usuário.

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
    )
''')
conn.commit()
conn.close()
print("Tabela 'Usuario' criada com sucesso.")

# Alterar tabela usuário para adicionar idade.

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()
cursor.execute('''
    ALTER TABLE Usuario
    ADD COLUMN idade INTEGER
''')
conn.commit()
conn.close()
print("Coluna 'idade' adicionada à tabela 'Usuario' com sucesso.")

# Inserir 5 usuários na tabela

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()
usuarios = [
    ("Gabriel Vieira", 28),
    ("Luiz Fernando", 35),
    ("Evelyn Silva", 22),
    ("Lincoln Barbosa", 30),
    ("Lucas Nogueira", 23)
]

for usuario in usuarios:
    cursor.execute('''
        INSERT INTO Usuario (nome, idade)
        VALUES (?, ?) 
    ''', usuario)
    print(f" Inserido: {usuario[0]} - {usuario[1]} anos")
conn.commit()
conn.close()
