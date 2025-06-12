from datetime import datetime
def gerar_sinais_precision():
    return [{
        "modo": "Precision v4",
        "data": datetime.now().strftime("%Y-%m-%d"),
        "competicao": "Premier League",
        "jogo": "Arsenal x Chelsea",
        "mercado": "Mais de 2.5 gols",
        "confiança": 89.5,
        "odd": 2.00,
        "fair_odd": 1.85,
        "stake": 2.0,
        "resultado": "AGUARDANDO"
    }]
