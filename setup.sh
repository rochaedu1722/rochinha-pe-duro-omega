#!/bin/bash
echo "🔧 Instalando dependências..."
pip install -r requirements.txt

echo "🔧 Ajustando banco de dados..."
python ajustar_banco.py

echo "🚀 Iniciando bot Rochinha Pé Duro com scheduler..."
python bot.py
