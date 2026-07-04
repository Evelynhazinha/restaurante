from database import Database

class Reserva:
    def __init__(self, idcliente, qtdpessoas, datahora):
        self.idcliente = idcliente
        self.qtdpessoas = qtdpessoas
        self.datahora = datahora

    def confirmar(self):
        print("=" * 30)
        print("   RESERVA")
        print("=" * 30)
        print(f"Cliente: {self.idcliente}")
        print(f"Pessoas: {self.qtdpessoas}")
        print(f"Data/Hora: {self.datahora}")
        print("=" * 30)
        print("Reserva confirmada!")


# ---- teste isolado ----
if __name__ == "__main__":
    cliente = input("Nome do cliente: ")
    pessoas = int(input("Quantidade de pessoas: "))
    datahora = input("Data e hora (ex: 25/12 19:00): ")

    reserva = Reserva(idcliente=cliente, qtdpessoas=pessoas, datahora=datahora)
    reserva.confirmar()