from core.modo_precision import gerar_sinais_precision
from core.modo_laboratorio import gerar_sinais_laboratorio
from envio import enviar_para_telegram
from core.aprendizado import registrar_sinal

print("🤖 Iniciando Rochinha Pé Duro Omega...")

sinais = gerar_sinais_precision() + gerar_sinais_laboratorio()

for sinal in sinais:
    enviar_para_telegram(sinal)
    registrar_sinal(sinal)

print("✅ Sinais enviados e registrados para aprendizado.")
