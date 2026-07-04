import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do banco de dados
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'devuser'),
    'password': os.getenv('DB_PASSWORD', 'devpass123'),
    'database': os.getenv('DB_NAME', 'sistema_login'),
    'port': int(os.getenv('DB_PORT', 3306))
}