#!/usr/bin/env python3
"""
Bot de Vendas com PIX - Main Launcher
Inicia o bot Discord e a API Flask simultaneamente
"""

import threading
import sys
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def run_bot():
    """Executa o bot Discord em uma thread separada"""
    print("🤖 Iniciando Bot Discord...")
    try:
        from src.bot.discord_bot import run_bot
        run_bot()
    except Exception as e:
        print(f"❌ Erro ao iniciar bot: {e}")
        sys.exit(1)

def run_api():
    """Executa a API Flask em uma thread separada"""
    print("🌐 Iniciando API Web...")
    try:
        from src.api.app import app
        from config import FLASK_HOST, FLASK_PORT
        # Desativar debug em thread (Flask não funciona com debug em thread)
        app.run(host=FLASK_HOST, port=FLASK_PORT, debug=False, threaded=True)
    except Exception as e:
        print(f"❌ Erro ao iniciar API: {e}")
        sys.exit(1)

if __name__ == '__main__':
    print("""
    ╔════════════════════════════════════════╗
    ║  💰 BOT DE VENDAS COM PIX 💰          ║
    ║  Discord Bot + Web Dashboard           ║
    ╚════════════════════════════════════════╝
    """)
    
    # Thread para o Bot Discord
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    
    # Thread para a API Flask
    api_thread = threading.Thread(target=run_api, daemon=True)
    
    # Iniciar ambas as threads
    print("🚀 Iniciando aplicação...\n")
    
    bot_thread.start()
    api_thread.start()
    
    print("\n✅ Sistema iniciado!")
    print("📊 Dashboard: http://localhost:5000")
    print("🤖 Bot Discord: Conectado ao Discord")
    print("\nPressione Ctrl+C para parar\n")
    
    try:
        # Manter o programa rodando
        bot_thread.join()
    except KeyboardInterrupt:
        print("\n\n⛔ Encerrando aplicação...")
        sys.exit(0)
