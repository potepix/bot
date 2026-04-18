#!/usr/bin/env python3
"""
Script de teste para validar a instalação do bot
"""

import os
import sys
from pathlib import Path

def test_environment():
    """Testa as variáveis de ambiente"""
    print("🔍 Verificando variáveis de ambiente...")
    
    required = ['DISCORD_TOKEN']
    missing = []
    
    for var in required:
        if not os.getenv(var):
            missing.append(var)
    
    if missing:
        print(f"⚠️  Variáveis faltando: {', '.join(missing)}")
        print("   Preencha o arquivo .env com os valores")
        return False
    
    print("✅ Variáveis de ambiente OK")
    return True

def test_imports():
    """Testa as importações dos módulos"""
    print("\n🔍 Verificando importações...")
    
    try:
        import discord
        print("✅ discord.py OK")
    except ImportError:
        print("❌ discord.py não instalado")
        return False
    
    try:
        import flask
        print("✅ Flask OK")
    except ImportError:
        print("❌ Flask não instalado")
        return False
    
    try:
        import dotenv
        print("✅ python-dotenv OK")
    except ImportError:
        print("❌ python-dotenv não instalado")
        return False
    
    print("✅ Todas as importações OK")
    return True

def test_database():
    """Testa o banco de dados"""
    print("\n🔍 Verificando banco de dados...")
    
    try:
        from src.database.models import db
        
        # Tentar criar uma conexão
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        conn.close()
        
        if tables:
            print(f"✅ Banco de dados OK ({len(tables)} tabelas encontradas)")
        else:
            print("✅ Banco de dados criado com sucesso")
        
        return True
    except Exception as e:
        print(f"❌ Erro no banco de dados: {e}")
        return False

def test_bot():
    """Testa a importação do bot Discord"""
    print("\n🔍 Verificando bot Discord...")
    
    try:
        from src.bot.discord_bot import bot
        print(f"✅ Bot Discord OK")
        return True
    except Exception as e:
        print(f"❌ Erro no bot: {e}")
        return False

def test_api():
    """Testa a importação da API Flask"""
    print("\n🔍 Verificando API Flask...")
    
    try:
        from src.api.app import app
        print(f"✅ API Flask OK")
        return True
    except Exception as e:
        print(f"❌ Erro na API: {e}")
        return False

def main():
    print("""
    ╔════════════════════════════════════════╗
    ║  💰 TESTE DO BOT DE VENDAS COM PIX    ║
    ╚════════════════════════════════════════╝
    """)
    
    all_ok = True
    
    if not test_environment():
        all_ok = False
    
    if not test_imports():
        all_ok = False
    
    if not test_database():
        all_ok = False
    
    if not test_bot():
        all_ok = False
    
    if not test_api():
        all_ok = False
    
    print("\n" + "="*40)
    
    if all_ok:
        print("✅ TUDO OK! Você pode executar: python main.py")
    else:
        print("❌ Alguma coisa não está certa. Verifique os erros acima.")
        sys.exit(1)

if __name__ == '__main__':
    main()
