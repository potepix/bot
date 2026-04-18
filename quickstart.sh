#!/bin/bash
# 🚀 Quick Start - Bot de Vendas PIX

echo "╔════════════════════════════════════════╗"
echo "║  💰 BOT DE VENDAS COM PIX 💰          ║"
echo "║  Quick Start Setup                      ║"
echo "╚════════════════════════════════════════╝"
echo ""

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 1. Verificar Python
echo -n "🔍 Verificando Python... "
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}OK${NC} ($PYTHON_VERSION)"
else
    echo -e "${RED}ERRO${NC}: Python não encontrado"
    exit 1
fi

# 2. Verificar pip
echo -n "🔍 Verificando pip... "
if command -v pip &> /dev/null; then
    echo -e "${GREEN}OK${NC}"
else
    echo -e "${RED}ERRO${NC}: pip não encontrado"
    exit 1
fi

# 3. Instalar dependências
echo ""
echo "📦 Instalando dependências..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Erro ao instalar dependências${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Dependências instaladas${NC}"

# 4. Testar
echo ""
echo "🧪 Testando configuração..."
python3 test.py

if [ $? -ne 0 ]; then
    echo ""
    echo -e "${YELLOW}⚠️  Configuração incompleta${NC}"
    echo ""
    echo "📝 Próximos passos:"
    echo "1. Abra Discord Developer Portal: https://discord.com/developers/applications"
    echo "2. Regenere o token do seu bot"
    echo "3. Cole o token em .env → DISCORD_TOKEN="
    echo "4. Execute: python3 main.py"
    exit 1
fi

# 5. Bot pronto
echo ""
echo -e "${GREEN}✅ Tudo configurado!${NC}"
echo ""
echo "🚀 Para iniciar o bot:"
echo "   python3 main.py"
echo ""
echo "📊 Dashboard web:"
echo "   http://localhost:5000"
echo ""
