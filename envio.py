import requests

def enviar_para_telegram(sinal):
    token = "7590925126:AAFiCWBAFfztEm_EqLoU2QibTfYkndPhv9M"
    chat_id = "1146864652"
    mensagem = f"""
📡 {sinal['modo']}
📅 {sinal['data']}
🏆 {sinal['competicao']}
⚽ {sinal['jogo']}
🎯 Mercado: {sinal['mercado']}
📈 Confiança: {sinal['confiança']}%
💰 Odd: {sinal['odd']} (Fair: {sinal['fair_odd']})
🎯 Stake: {sinal['stake']}%
📊 Resultado: {sinal.get('resultado', 'Aguardando')}
"""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        requests.post(url, data={"chat_id": chat_id, "text": mensagem})
    except Exception as e:
        print(f"Erro no envio: {e}")
