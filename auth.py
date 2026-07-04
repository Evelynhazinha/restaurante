import hashlib
import getpass
import psycopg2
from psycopg2.errors import UniqueViolation
from psycopg2.extras import RealDictCursor
from database import Database

class User:
    """Representa um usuário do sistema"""
    
    def __init__(self, id=None, nome=None, email=None, tipo=None, data_cadastro=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.tipo = tipo
        self.data_cadastro = data_cadastro

    def __str__(self):
        return f"{self.nome} ({self.tipo.upper()})"


class AuthService:
    """Serviço de autenticação (Cadastro, Login e Listagem)"""
    
    @staticmethod
    def hash_senha(senha: str) -> str:
        """Gera hash da senha"""
        return hashlib.sha256(senha.encode('utf-8')).hexdigest()

    @staticmethod
    def cadastrar_usuario():
        """Cadastro de novo usuário"""
        print("\n" + "="*60)
        print("               CADASTRO DE USUÁRIO")
        print("="*60)
        
        nome = input("Nome completo: ").strip()
        email = input("Email: ").strip().lower()
        
        if not nome or not email:
            print("❌ Nome e email são obrigatórios!")
            return None

        print("\nTipo de Usuário:")
        print("1. Cliente")
        print("2. Funcionário")
        tipo_opcao = input("Escolha (1 ou 2): ").strip()
        tipo = "cliente" if tipo_opcao == "1" else "funcionario"

        senha = getpass.getpass("Senha (mín. 6 caracteres): ")
        if senha != getpass.getpass("Confirmar senha: "):
            print("❌ As senhas não coincidem!")
            return None
        if len(senha) < 6:
            print("❌ Senha deve ter no mínimo 6 caracteres!")
            return None

        conn = Database.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            sql = """
                INSERT INTO usuarios (nome, email, senha, tipo) 
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (nome, email, AuthService.hash_senha(senha), tipo))
            conn.commit()
            
            print(f"\n✅ Usuário '{nome}' cadastrado como {tipo.upper()} com sucesso!")
            return True
            
        except UniqueViolation:
            # Captura erro de e-mail duplicado no PostgreSQL
            print("❌ Este email já está cadastrado!")
            return False
        except psycopg2.Error as e:
            print(f"❌ Erro ao cadastrar: {e}")
            return False
        finally:
            Database.close_connection(conn, cursor)

    @staticmethod
    def fazer_login():
        """Realiza login"""
        print("\n" + "="*60)
        print("                    LOGIN")
        print("="*60)
        
        email = input("Email: ").strip().lower()
        senha = getpass.getpass("Senha: ")

        conn = Database.get_connection()
        if not conn:
            return None

        try:
            # Substituído 'dictionary=True' por cursor_factory do psycopg2
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            sql = """
                SELECT id, nome, email, tipo, data_cadastro 
                FROM usuarios 
                WHERE email = %s AND senha = %s
            """
            cursor.execute(sql, (email, AuthService.hash_senha(senha)))
            resultado = cursor.fetchone()
            
            if resultado:
                usuario = User(**resultado)
                print(f"\n✅ Login realizado com sucesso!")
                print(f"👋 Bem-vindo(a), {usuario.nome}!")
                print(f"Tipo: {usuario.tipo.upper()}")
                return usuario
            else:
                print("❌ Email ou senha incorretos!")
                return None
                
        except Exception as e:
            print(f"❌ Erro durante login: {e}")
            return None
        finally:
            Database.close_connection(conn, cursor)

    @staticmethod
    def listar_usuarios():
        """Lista todos os usuários cadastrados"""
        conn = Database.get_connection()
        if not conn:
            return

        try:
            # Substituído 'dictionary=True' por cursor_factory do psycopg2
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("""
                SELECT id, nome, email, tipo, data_cadastro 
                FROM usuarios 
                ORDER BY data_cadastro DESC
            """)
            usuarios = cursor.fetchall()
            
            print("\n" + "="*85)
            print("                    USUÁRIOS CADASTRADOS")
            print("="*85)
            
            if not usuarios:
                print("Nenhum usuário cadastrado ainda.")
                return
            
            for u in usuarios:
                user = User(**u)
                print(f"ID: {user.id:>3} | Nome: {user.nome:<25} | "
                      f"Email: {user.email:<30} | Tipo: {user.tipo.upper():<12} | "
                      f"Data: {user.data_cadastro}")
                
        except Exception as e:
            print(f"❌ Erro ao listar usuários: {e}")
        finally:
            Database.close_connection(conn, cursor)