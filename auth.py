import getpass
import hashlib
import mysql.connector
from database import Database


class User:
    """Representa um usuário do sistema"""

    def __init__(self, id=None, nome=None, email=None, tipo=None, data_cadastro=None, email_deletar=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.tipo = tipo
        self.data_cadastro = data_cadastro
        self.email_deletar = email_deletar

    def __str__(self):
        return f"{self.nome} ({self.tipo.upper()})"


class AuthService:
    """Serviço de autenticação"""

    @staticmethod
    def hash_senha(senha: str) -> str:
        return hashlib.sha256(senha.encode("utf-8")).hexdigest()

    @staticmethod
    def cadastrar_usuario():

        print("\n" + "=" * 60)
        print("              CADASTRO DE CLIENTE")
        print("=" * 60)

        nome = input("Nome completo: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("Email: ").strip().lower()

        if not nome or not email:
            print("❌ Nome e email são obrigatórios!")
            return None

        senha = input("Senha: ")

        confirmar = input("Confirmar senha: ")

        if senha != confirmar:
            print("❌ As senhas não coincidem!")
            return None

        conn = Database.get_connection()

        if not conn:
            return None

        try:

            cursor = conn.cursor()

            sql_cliente = """
            INSERT INTO cliente(nomecliente, telefone, email)
            VALUES(%s,%s,%s)
            """

            cursor.execute(sql_cliente, (nome, telefone, email))

            idcliente = cursor.lastrowid

            sql_login = """
            INSERT INTO login(email, senha, idcliente)
            VALUES(%s,%s,%s)
            """

            cursor.execute(
                sql_login,
                (
                    email,
                    senha,
                    idcliente
                )
            )

            conn.commit()

            print("\n✅ Cliente cadastrado com sucesso!")

            return True

        except mysql.connector.Error as e:

            print(f"❌ Erro ao cadastrar: {e}")
            return False

        finally:

            Database.close_connection(conn, cursor)

    @staticmethod
    def fazer_login():

        print("\n" + "=" * 60)
        print("                    LOGIN")
        print("=" * 60)

        email = input("Email: ").strip().lower()
        senha = getpass.getpass("Senha: ")

        conn = Database.get_connection()

        if not conn:
            return None

        try:

            cursor = conn.cursor(dictionary=True)

            sql = """
            SELECT
                c.idcliente AS id,
                c.nomecliente AS nome,
                c.email,
                'cliente' AS tipo
            FROM login l
            INNER JOIN cliente c
            ON l.idcliente = c.idcliente
            WHERE l.email=%s
            AND l.senha=%s
            """

            cursor.execute(sql, (email, senha))

            resultado = cursor.fetchone()

            if resultado:

                usuario = User(**resultado)

                print("\n✅ Login realizado com sucesso!")
                print(f"👋 Bem-vindo(a), {usuario.nome}!")

                return usuario

            print("❌ Email ou senha incorretos!")

            return None

        except Exception as e:

            print(f"❌ Erro durante login: {e}")

            return None

        finally:

            Database.close_connection(conn, cursor)

    @staticmethod
    def listar_usuarios():

        conn = Database.get_connection()

        if not conn:
            return

        try:

            cursor = conn.cursor(dictionary=True)

            cursor.execute("""
                SELECT
                    idcliente AS id,
                    nomecliente AS nome,
                    email,
                    'cliente' AS tipo
                FROM cliente
                ORDER BY nomecliente
            """)

            usuarios = cursor.fetchall()

            print("\n" + "=" * 85)
            print("                 CLIENTES CADASTRADOS")
            print("=" * 85)

            if not usuarios:

                print("Nenhum cliente cadastrado.")
                return

            for u in usuarios:

                user = User(**u)

                print(
                    f"ID: {user.id:>3} | "
                    f"Nome: {user.nome:<25} | "
                    f"Email: {user.email:<30}"
                )

        except Exception as e:

            print(f"❌ Erro ao listar clientes: {e}")

        finally:

            Database.close_connection(conn, cursor)

    @staticmethod
    def delete_usuario():
        print("\n" + "="*60)
        print("                  DELETAR USUÁRIO (LOGIN)")
        print("="*60)
        
        email_deletar = input("Digite o e-mail do usuário que deseja deletar: ").strip().lower()
        
        if not email_deletar:
            print("❌ E-mail não pode ser vazio!")
            return False

        conn = Database.get_connection()
        if not conn:
            return False
            
        try:
            cursor = conn.cursor()
            
            cursor.execute("SELECT idcliente FROM cliente WHERE email = %s", (email_deletar,))
            resultado = cursor.fetchone()
            
            if not resultado:
                print("❌ Nenhum usuário encontrado com esse e-mail na lista de clientes.")
                return False
                
            id_cliente = resultado[0] 

            cursor.execute("DELETE FROM login WHERE idcliente = %s", (id_cliente,))
            cursor.execute("DELETE FROM reserva WHERE idCliente = %s", (id_cliente,))
            cursor.execute("DELETE FROM pedido WHERE idcliente = %s", (id_cliente,))
            cursor.execute("DELETE FROM cliente WHERE idcliente = %s", (id_cliente,))
            
            conn.commit()
            
            if cursor.rowcount > 0:
                print(f"✅ Usuário com e-mail '{email_deletar}' deletado com sucesso!")
                return True
            else:
                print("❌ Nenhum usuário encontrado com esse e-mail.")
                return False
                
        except Exception as e:
            print(f"❌ Erro ao deletar usuário: {e}")
            return False
        finally:
            Database.close_connection(conn, cursor)

    @staticmethod
    def atualizar_email():
        print("\n" + "="*60)
        print("                  ATUALIZAR E-MAIL DO USUÁRIO")
        print("="*60)
        
        email_atual = input("Digite o e-mail ATUAL do usuário que deseja alterar: ").strip().lower()
        
        if not email_atual:
            print("❌ O e-mail atual não pode ser vazio!")
            return False

        conn = Database.get_connection()
        if not conn:
            return False
            
        try:
            cursor = conn.cursor()
            
            cursor.execute("SELECT idcliente, nomecliente FROM cliente WHERE email = %s", (email_atual,))
            resultado = cursor.fetchone()
            
            if not resultado:
                print("❌ Nenhum usuário encontrado com esse e-mail.")
                return False
                
            id_cliente = resultado[0]
            nome_cliente = resultado[1]
            
            print(f"Usuário: {nome_cliente}")
            
            novo_email = input("Digite o novo e-mail: ").strip().lower()
            
            if not novo_email:
                print("❌ O novo e-mail não pode ser vazio!")
                return False
                
            if novo_email == email_atual:
                print("⚠️ O novo e-mail é igual ao atual. Nenhuma alteração necessária.")
                return True

            sql_cliente = "UPDATE cliente SET email = %s WHERE idcliente = %s"
            cursor.execute(sql_cliente, (novo_email, id_cliente))
            
            sql_login = "UPDATE login SET email = %s WHERE idcliente = %s"
            cursor.execute(sql_login, (novo_email, id_cliente))
            
            conn.commit()
            
            print(f"✅ E-mail de '{nome_cliente}' atualizado para '{novo_email}' com sucesso!")
            return True
                
        except Exception as e:
            print(f"❌ Erro ao atualizar o e-mail: {e}")
            return False
        finally:
            Database.close_connection(conn, cursor)