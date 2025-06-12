#!/bin/bash

echo "🔧 Instalando dependências..."
pip install -r requirements.txt

echo "🔧 Ajustando banco de dados (adicionando coluna 'data' se necessário)..."
python ajustar_banco.py

echo "🚀 Iniciando bot Rochinha Pé Duro Omega..."
python bot.py
