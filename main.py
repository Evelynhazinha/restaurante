from auth import AuthService
from pedido import Pedido
from reserva import Reserva
from pagamento import Pagamento


class SistemaRestaurante:

    def __init__(self):
        self.usuario = None

    def iniciar(self):

        while True:

            print("\n" + "=" * 50)
            print("        RESTAURANTE")
            print("=" * 50)
            print("1 - Login")
            print("2 - Cadastro")
            print("3 - Listar usuários")
            print("4 - Deletar usuários")
            print("5 - Atualizar E-mail")
            print("6 - Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                self.login()

            elif opcao == "2":
                AuthService.cadastrar_usuario()

            elif opcao == "3":
                AuthService.listar_usuarios()

            elif opcao == "4":
                AuthService.delete_usuario()

            elif opcao == "5":
                AuthService.atualizar_email()

            elif opcao == "6":
                print("\nObrigado por utilizar nosso sistema!")
                break

            else:
                print("\nOpção inválida!")

    def login(self):

        usuario = AuthService.fazer_login()

        if usuario:
            self.usuario = usuario
            self.menu_cliente()

    def menu_cliente(self):

        while True:

            print("\n" + "=" * 50)
            print(f"Bem-vindo(a), {self.usuario.nome}")
            print("=" * 50)
            print("1 - Fazer pedido")
            print("2 - Fazer reserva")
            print("3 - Logout")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                self.realizar_pedido()

            elif opcao == "2":
                self.realizar_reserva()

            elif opcao == "3":
                print("\nLogout realizado!")
                self.usuario = None
                break

            else:
                print("\nOpção inválida!")

    def realizar_pedido(self):

        pedido = Pedido(self.usuario.id)

        pedido.fazer_pedido()

        if pedido.total == 0:
            print("\nNenhum item foi escolhido.")
            return

        pedido.salvar_pedido()

        pagamento = Pagamento(
            pedido.idpedido,
            pedido.total
        )

        formas = {
            "1": "Dinheiro",
            "2": "Cartão de Débito",
            "3": "Cartão de Crédito",
            "4": "PIX",
            "5": "Vale Alimentação"
        }

        print("\nFormas de pagamento:")

        for codigo, metodo in formas.items():
            print(f"{codigo} - {metodo}")

        escolha = input("\nEscolha a forma de pagamento: ")

        pagamento.escolher_forma(
            formas.get(escolha, "Não identificado")
        )

        pagamento.finalizar()

    def realizar_reserva(self):

        pessoas = int(input("Quantidade de pessoas: "))
        datahora = input("Data e hora (AAAA-MM-DD HH:MM): ")

        reserva = Reserva(
            self.usuario.id,
            pessoas,
            datahora
        )

        reserva.confirmar()


if __name__ == "__main__":

    sistema = SistemaRestaurante()
    sistema.iniciar()