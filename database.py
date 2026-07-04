import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

class Database:
    """Classe responsável por gerenciar a conexão com o banco de dados"""
    
    @staticmethod
    def get_connection():
        """Retorna uma nova conexão"""
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            return conn
        except Error as e:
            print(f"❌ Erro de conexão: {e}")
            return None

    @staticmethod
    def close_connection(conn, cursor=None):
        """Fecha conexão e cursor"""
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()