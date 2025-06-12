import schedule
import time
from core.modo_precision import gerar_sinais_precision
from core.modo_laboratorio import gerar_sinais_laboratorio
from envio import enviar_para_telegram
from core.aprendizado import registrar_sinal
from core.api_football import buscar_jogos_hoje

def rotina_bot():
    print("🔄 Buscando jogos do dia via API-Football...")
    jogos = buscar_jogos_hoje()
    if not jogos:
        print("❌ Nenhum jogo encontrado para hoje.")
        return

    print("✅ Jogos recebidos. Rodando modos de IA...")
    sinais_precision = gerar_sinais_precision(jogos)
    sinais_laboratorio = gerar_sinais_laboratorio(jogos)

    sinais = sinais_precision + sinais_laboratorio
    print(f"📦 Total de sinais gerados: {len(sinais)}")

    for sinal in sinais:
        registrar_sinal(sinal)
        enviar_para_telegram(sinal)

print("🤖 Iniciando Rochinha Pé Duro com scheduler e API-Football...")
schedule.every().hour.do(rotina_bot)
rotina_bot()

while True:
    schedule.run_pending()
    time.sleep(60)
