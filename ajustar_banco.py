import sqlite3
import os

db_path = os.path.join("db", "rochinha_aprendizado.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute("PRAGMA table_info(sinais);")
colunas = [col[1] for col in c.fetchall()]

novas_colunas = {
    "data": "TEXT",
    "modo": "TEXT",
    "competicao": "TEXT",
    "jogo": "TEXT"
}

for coluna, tipo in novas_colunas.items():
    if coluna not in colunas:
        print(f"Adicionando coluna '{coluna}'...")
        c.execute(f"ALTER TABLE sinais ADD COLUMN {coluna} {tipo};")
        conn.commit()

conn.close()
