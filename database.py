import mysql.connector


class Database:

    @staticmethod
    def get_connection():
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",  # coloque sua senha do MySQL aqui
                database=""  # nome do seu banco
            )
            return conn

        except mysql.connector.Error as err:
            print(f"Erro ao conectar com o banco de dados: {err}")
            return None

    @staticmethod
    def close_connection(conn, cursor):
        try:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        except Exception as e:
            print(f"Erro ao fechar conexão: {e}")