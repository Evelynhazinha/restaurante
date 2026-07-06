from database import Database

class Reserva:
    def __init__(self, idcliente, qtdpessoas, datahora):
        self.idcliente = idcliente
        self.qtdpessoas = qtdpessoas
        self.datahora = datahora

    def confirmar(self):
        conn = Database.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO reserva (datahora, qtdpessoas, idCliente) VALUES (%s, %s, %s)",
            (self.datahora, self.qtdpessoas, self.idcliente)
        )

        conn.commit()
        Database.close_connection(conn, cursor)

        print("=" * 30)
        print("   RESERVA")
        print("=" * 30)
        print(f"Cliente: {self.idcliente}")
        print(f"Pessoas: {self.qtdpessoas}")
        print(f"Data/Hora: {self.datahora}")
        print("=" * 30)
        print("Reserva confirmada!")

if __name__ == "__main__":
    cliente = int(input("ID do cliente: "))
    pessoas = int(input("Quantidade de pessoas: "))
    datahora = input("Data e hora (ex: 2026-07-10 19:00:00): ")

    reserva = Reserva(idcliente=cliente, qtdpessoas=pessoas, datahora=datahora)
    reserva.confirmar()