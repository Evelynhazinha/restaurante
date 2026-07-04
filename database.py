import psycopg2
from psycopg2 import Error
from config import DATABASE_URL

class Database:
    """Classe responsável por gerenciar a conexão com o banco de dados"""
    
    @staticmethod
    def get_connection():
        """Retorna uma nova conexão"""
        try:
            conn = psycopg2.connect(DATABASE_URL)
            return conn
        except Error as e:
            print(f"❌ Erro de conexão: {e}")
            return None

    @staticmethod
    def close_connection(conn, cursor=None):
        """Fecha conexão e cursor"""
        if cursor:
            cursor.close()
        if conn and not conn.closed:
            conn.close()

    @staticmethod
    def inicializar_banco():
        """Cria todas as tabelas necessárias automaticamente caso não existam"""
        conn = Database.get_connection()
        if not conn:
            print("❌ Não foi possível conectar ao banco para inicialização.")
            return

        try:
            cursor = conn.cursor()
            
            # Script SQL com a ordem correta de criação (tabelas independentes primeiro)
            sql = """
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                senha VARCHAR(255) NOT NULL,
                tipo VARCHAR(20) NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS cliente (
                idcliente SERIAL PRIMARY KEY,
                nomecliente VARCHAR(100),
                telefone VARCHAR(20),
                email VARCHAR(100)
            );

            CREATE TABLE IF NOT EXISTS funcionario (
                idfuncionario SERIAL PRIMARY KEY,
                nomefuncionario VARCHAR(100),
                cpf VARCHAR(14),
                telefone VARCHAR(20),
                email VARCHAR(100)
            );

            CREATE TABLE IF NOT EXISTS login (
                idlogin SERIAL PRIMARY KEY,
                email VARCHAR(100),
                senha VARCHAR(255),
                idcliente INT REFERENCES cliente(idcliente),
                idfuncionario INT REFERENCES funcionario(idfuncionario)
            );

            CREATE TABLE IF NOT EXISTS reserva (
                idreserva SERIAL PRIMARY KEY,
                datahora TIMESTAMP,
                qtdpessoas INT,
                idCliente INT REFERENCES cliente(idcliente)
            );

            CREATE TABLE IF NOT EXISTS pedido (
                idpedido SERIAL PRIMARY KEY,
                total REAL,
                idcliente INT REFERENCES cliente(idcliente),
                mesa INT,
                status BOOLEAN
            );

            CREATE TABLE IF NOT EXISTS cardapio (
                idcardapio SERIAL PRIMARY KEY,
                nomeprato VARCHAR(100),
                preco REAL,
                idpedido INT REFERENCES pedido(idpedido)
            );

            CREATE TABLE IF NOT EXISTS pagamento (
                idpagamento SERIAL PRIMARY KEY,
                idpedido INT REFERENCES pedido(idpedido),
                valor REAL
            );

            CREATE TABLE IF NOT EXISTS formapagamento (
                idformapagamento SERIAL PRIMARY KEY,
                metodo VARCHAR(50),
                idpagamento INT REFERENCES pagamento(idpagamento)
            );
            """
            cursor.execute(sql)
            conn.commit()
            print("✅ Estrutura do banco de dados verificada/inicializada com sucesso!")
            
        except Error as e:
            print(f"❌ Erro ao inicializar o banco de dados: {e}")
            conn.rollback()
        finally:
            Database.close_connection(conn, cursor)