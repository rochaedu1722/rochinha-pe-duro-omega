#!/bin/bash
echo "🔧 Iniciando setup do bot Rochinha Pé Duro..."

# Instalar dependências do requirements.txt
if [ -f requirements.txt ]; then
  echo "📦 Instalando dependências via pip..."
  pip install -r requirements.txt
else
  echo "⚠️ Arquivo requirements.txt não encontrado!"
fi

# Criar diretório de banco de dados se não existir
mkdir -p db

# Mensagem final
echo "✅ Setup concluído com sucesso!"
