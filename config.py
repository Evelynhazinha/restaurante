import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env[cite: 2]
load_dotenv()

# Pegamos a string de conexão inteira
DATABASE_URL = os.getenv('DATABASE_URL')