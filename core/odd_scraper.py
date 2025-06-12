def obter_odds_reais(jogos):
    # Esta função simula odds reais para cada jogo e adiciona 'odds' ao dicionário
    for jogo in jogos:
        jogo['odds'] = {
            'mais_2.5': 1.75,
            'btts': 1.83,
            'dupla_chance': 1.60,
            'resultado_mais_1.5': 1.95,
            'gol_75': 2.10
        }
    return jogos
