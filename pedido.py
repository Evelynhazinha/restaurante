from database import Database

class Pedido:

    def __init__(self, idcliente):
        self.idcliente = idcliente
        self.idpedido = None
        self.total = 0

    def mostrar_cardapio(self):

        conn = Database.get_connection()

        if not conn:
            return []

        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT idcardapio, nomeprato, preco
            FROM cardapio
        """)

        cardapio = cursor.fetchall()

        print("\n" + "=" * 40)
        print("           CARDÁPIO")
        print("=" * 40)

        for prato in cardapio:
            print(f"{prato['idcardapio']} - {prato['nomeprato']} - R$ {prato['preco']:.2f}")

        Database.close_connection(conn, cursor)

        return cardapio


    def fazer_pedido(self):

        cardapio = self.mostrar_cardapio()

        while True:

            codigo = input("\nCódigo do prato (0 para finalizar): ")

            if codigo == "0":
                break

            encontrou = False

            for prato in cardapio:

                if str(prato["idcardapio"]) == codigo:

                    quantidade = int(input("Quantidade: "))

                    subtotal = prato["preco"] * quantidade

                    self.total += subtotal

                    print(f"{quantidade}x {prato['nomeprato']} adicionados!")
                    print(f"Subtotal: R$ {subtotal:.2f}")

                    encontrou = True
                    break

            if not encontrou:
                print("Código inválido!")

        print("\nTotal do pedido: R$ {:.2f}".format(self.total))


    def salvar_pedido(self):

        conn = Database.get_connection()

        if not conn:
            return

        cursor = conn.cursor()

        mesa = int(input("Número da mesa: "))

        cursor.execute("""
            INSERT INTO pedido(total,idcliente,mesa,status)
            VALUES(%s,%s,%s,%s)
        """, (
            self.total,
            self.idcliente,
            mesa,
            False
        ))

        conn.commit()

        self.idpedido = cursor.lastrowid

        Database.close_connection(conn, cursor)

        print("\nPedido realizado com sucesso!")
        print(f"Número do pedido: {self.idpedido}")