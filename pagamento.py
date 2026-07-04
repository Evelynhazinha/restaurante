from database import Database
class Pagamento:
    def __init__(self, idpedido, valor):
        self.idpedido = idpedido
        self.valor = valor
        self.forma = None

    def escolher_forma(self, metodo):
        self.forma = metodo

    def finalizar(self):
        print("=" * 30)
        print("   PAGAMENTO")
        print("=" * 30)
        print(f"Pedido: {self.idpedido}")
        print(f"Valor: R$ {self.valor:.2f}")
        print(f"Forma: {self.forma}")
        print("=" * 30)
        print("Pagamento confirmado!")


# ---- teste isolado ----
if __name__ == "__main__":
    valor = float(input("Valor do pedido: R$ "))
    pagamento = Pagamento(idpedido=1, valor=valor)

    # formas que já estão cadastradas no banco (tabela formapagamento)
    formas = {
        "1": "Dinheiro",
        "2": "Cartão de Débito",
        "3": "Cartão de Crédito",
        "4": "PIX",
        "5": "Vale Alimentação",
    }

    print("Formas de pagamento:")
    for numero, nome in formas.items():
        print(f"{numero} - {nome}")

    opcao = input("Escolha a forma: ")
    pagamento.escolher_forma(formas.get(opcao, "Não identificado"))
    pagamento.finalizar()