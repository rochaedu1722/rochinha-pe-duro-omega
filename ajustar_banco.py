import sqlite3
import os

# Caminho do banco de dados
db_path = os.path.join("db", "rochinha_aprendizado.db")

# Conectar ao banco
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Verificar as colunas existentes na tabela 'sinais'
c.execute("PRAGMA table_info(sinais);")
colunas = [col[1] for col in c.fetchall()]

# Adicionar coluna 'data' se não existir
if "data" not in colunas:
    print("🔧 Adicionando coluna 'data' na tabela 'sinais'...")
    c.execute("ALTER TABLE sinais ADD COLUMN data TEXT;")
    conn.commit()
    print("✅ Coluna 'data' adicionada com sucesso!")
else:
    print("✅ A coluna 'data' já existe.")

# Adicionar coluna 'modo' se não existir
if "modo" not in colunas:
    print("🔧 Adicionando coluna 'modo' na tabela 'sinais'...")
    c.execute("ALTER TABLE sinais ADD COLUMN modo TEXT;")
    conn.commit()
    print("✅ Coluna 'modo' adicionada com sucesso!")
else:
    print("✅ A coluna 'modo' já existe.")

conn.close()
