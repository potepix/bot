import os
from dotenv import load_dotenv

load_dotenv()

# Discord Token
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN', '')

# Flask
FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')
# Railway usa PORT, outros usam FLASK_PORT
FLASK_PORT = int(os.getenv('PORT', os.getenv('FLASK_PORT', 5000)))
FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'

# Database
DB_PATH = os.getenv('DB_PATH', 'payments.db')
