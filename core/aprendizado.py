import sqlite3
from datetime import datetime

def registrar_sinal(sinal):
    conn = sqlite3.connect("db/rochinha_aprendizado.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS sinais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT, modo TEXT, competicao TEXT, jogo TEXT,
            mercado TEXT, confiança REAL, odd REAL, fair_odd REAL,
            stake REAL, resultado TEXT, data_registro TEXT
        )
    """)
    c.execute("""
        INSERT INTO sinais (data, modo, competicao, jogo, mercado, confiança, odd, fair_odd, stake, resultado, data_registro)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        sinal["data"], sinal["modo"], sinal["competicao"], sinal["jogo"], sinal["mercado"],
        sinal["confiança"], sinal["odd"], sinal["fair_odd"], sinal["stake"],
        sinal.get("resultado", "AGUARDANDO"),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    conn.commit()
    conn.close()
