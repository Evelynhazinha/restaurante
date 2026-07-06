# restaurante

Sistema de Restaurante - POO II

Projeto desenvolvido para a disciplina de Programação Orientada a Objetos II com o objetivo de simular um sistema de gerenciamento de restaurante utilizando Python orientado a objetos e MySQL para armazenar os dados.

O sistema permite que clientes realizem cadastro e login, façam pedidos, escolham a forma de pagamento e efetuem reservas em um restaurante.

O projeto foi desenvolvido aplicando conceitos fundamentais de POO, como:

* Classes e Objetos;
* Modularização;
* Separação de responsabilidades;
* Integração com banco de dados MySQL.

Funcionalidades:

* Cadastro de clientes;
* Login de usuários;
* Listagem de clientes cadastrados;
* Visualização do cardápio;
* Realização de pedidos;
* Cálculo automático do valor total;
* Escolha da forma de pagamento;
* Reserva de mesas;
* Integração com banco de dados MySQL.

Estrutura do Projeto:

auth.py          # Cadastro, login e gerenciamento de usuários;
database.py      # Conexão com o banco de dados;
pedido.py        # Processo de realização de pedidos;
pagamento.py     # Gerenciamento de pagamentos;
reserva.py       # Sistema de reservas;
main.py          # Programa principal.

Tecnologias Utilizadas

* Python 3;
* MySQL;
* mysql-connector-python;
* Programação Orientada a Objetos.

Conceitos de POO Aplicados:

* Organização em classes independentes;
* Métodos responsáveis por regras específicas;
* Separação entre interface e acesso ao banco;
* Reutilização de código;
* Modularização do sistema.
