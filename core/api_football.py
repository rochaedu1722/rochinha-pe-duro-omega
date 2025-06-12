import requests

API_KEY = '716f8d3daaf79e64a6efe3e0a5b76987'
BASE_URL = 'https://v3.football.api-sports.io'

headers = {
    'x-apisports-key': API_KEY
}

def buscar_jogos_hoje():
    from datetime import datetime
    hoje = datetime.now().strftime('%Y-%m-%d')
    url = f"{BASE_URL}/fixtures?date={hoje}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        jogos = data.get('response', [])
        return jogos
    return []
