
import requests

API_KEY = 'b7e22280e22193b6902175136b55bd61'

def obter_odds_reais(jogos):
    url = f'https://api.the-odds-api.com/v4/sports/soccer_epl/odds'
    params = {
        'apiKey': API_KEY,
        'regions': 'eu',
        'markets': 'h2h,totals',
        'oddsFormat': 'decimal'
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        odds_por_time = {}
        for partida in data:
            if 'home_team' in partida and 'bookmakers' in partida:
                home = partida['home_team']
                away = partida['away_team']
                jogo = f"{home} x {away}"
                odds = {}

                for bookmaker in partida['bookmakers']:
                    for mercado in bookmaker['markets']:
                        if mercado['key'] == 'totals':
                            for outcome in mercado['outcomes']:
                                if outcome['point'] == 2.5:
                                    odds['mais_2.5'] = outcome['price']
                        elif mercado['key'] == 'h2h':
                            if len(mercado['outcomes']) == 3:
                                odds['dupla_chance'] = max([o['price'] for o in mercado['outcomes'][:2]])

                odds_por_time[jogo] = odds

        for jogo in jogos:
            jogo_nome = f"{jogo['home_team']} x {jogo['away_team']}"
            if jogo_nome in odds_por_time:
                jogo['odds'] = odds_por_time[jogo_nome]
            else:
                jogo['odds'] = {}

        return jogos

    except Exception as e:
        print(f"Erro ao obter odds reais: {e}")
        for jogo in jogos:
            jogo['odds'] = {}
        return jogos
