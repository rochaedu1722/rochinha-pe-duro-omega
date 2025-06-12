from datetime import datetime
def gerar_sinais_laboratorio():
    return [{
        "modo": "Laboratório v2",
        "data": datetime.now().strftime("%Y-%m-%d"),
        "competicao": "Libertadores",
        "jogo": "Flamengo x River Plate",
        "mercado": "Finalizações Gabigol +3.5",
        "confiança": 87.0,
        "odd": 2.15,
        "fair_odd": 1.95,
        "stake": 2.5,
        "resultado": "AGUARDANDO"
    }]
