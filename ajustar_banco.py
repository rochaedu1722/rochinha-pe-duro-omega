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

# Adicionar colunas se não existirem
novas_colunas = {
    "data": "TEXT",
    "modo": "TEXT",
    "competicao": "TEXT",
    "jogo": "TEXT"
}

for coluna, tipo in novas_colunas.items():
    if coluna not in colunas:
        print(f"🔧 Adicionando coluna '{coluna}' na tabela 'sinais'...")
        c.execute(f"ALTER TABLE sinais ADD COLUMN {coluna} {tipo};")
        conn.commit()
        print(f"✅ Coluna '{coluna}' adicionada com sucesso!")
    else:
        print(f"✅ A coluna '{coluna}' já existe.")

conn.close()
