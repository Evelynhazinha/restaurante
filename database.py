import site

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv() [site: 2]

class Database:
    @staticmethod
    def get_connection():
        try:
            
            return mysql.connector.connect(
                host=os.getenv("DB_HOST", "localhost"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", ""), 
                database=os.getenv("DB_NAME", "restaurante")
            )
        except mysql.connector.Error as e:
            print(f"❌ Erro de conexão com o banco: {e}")
            return None

    @staticmethod
    def close_connection(conn, cursor=None):
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()