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