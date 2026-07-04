from auth import AuthService
from database import Database

def menu():
    # Inicializa o banco de dados automaticamente ao abrir o sistema
    print("Iniciando sistema e configurando banco de dados...")
    Database.inicializar_banco()

    while True:

        print("\n" + "="*65)
        print("   SISTEMA DE CADASTRO E LOGIN - ORIENTADO A OBJETOS")
        print("="*65)
        print("1. Cadastrar novo usuário")
        print("2. Fazer Login")
        print("3. Listar todos os usuários")
        print("4. Sair")
        print("="*65)
        
        opcao = input("\nEscolha uma opção: ").strip()


        if opcao == "1":
            AuthService.cadastrar_usuario()
        elif opcao == "2":
            AuthService.fazer_login()
        elif opcao == "3":
            AuthService.listar_usuarios()
        elif opcao == "4":
            print("👋 Obrigado por usar o sistema! Até logo!")
            break
        else:
            print("❌ Opção inválida!")

        if opcao != "4":
            input("\nPressione Enter para continuar...")
        
if __name__ == "__main__":
    menu()