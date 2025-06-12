import sqlite3
import os

# Caminho do banco de dados
db_path = os.path.join("db", "rochinha_aprendizado.db")

# Conectar ao banco
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Verificar se a coluna 'data' já existe
c.execute("PRAGMA table_info(sinais);")
colunas = [col[1] for col in c.fetchall()]

if "data" not in colunas:
    print("🔧 Adicionando coluna 'data' na tabela 'sinais'...")
    c.execute("ALTER TABLE sinais ADD COLUMN data TEXT;")
    conn.commit()
    print("✅ Coluna 'data' adicionada com sucesso!")
else:
    print("✅ A coluna 'data' já existe. Nenhuma alteração foi necessária.")

conn.close()
