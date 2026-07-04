-- Tabela complementar exigida pelo arquivo auth.py
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela: cliente
CREATE TABLE IF NOT EXISTS cliente (
    idcliente SERIAL PRIMARY KEY,
    nomecliente VARCHAR(100),
    telefone VARCHAR(20),
    email VARCHAR(100)
);

-- Tabela: funcionario
CREATE TABLE IF NOT EXISTS funcionario (
    idfuncionario SERIAL PRIMARY KEY,
    nomefuncionario VARCHAR(100),
    cpf VARCHAR(14),
    telefone VARCHAR(20),
    email VARCHAR(100)
);

-- Tabela: login
CREATE TABLE IF NOT EXISTS login (
    idlogin SERIAL PRIMARY KEY,
    email VARCHAR(100),
    senha VARCHAR(255),
    idcliente INT REFERENCES cliente(idcliente),
    idfuncionario INT REFERENCES funcionario(idfuncionario)
);

-- Tabela: reserva
CREATE TABLE IF NOT EXISTS reserva (
    idreserva SERIAL PRIMARY KEY,
    datahora TIMESTAMP,
    qtdpessoas INT,
    idCliente INT REFERENCES cliente(idcliente)
);

-- Tabela: pedido
CREATE TABLE IF NOT EXISTS pedido (
    idpedido SERIAL PRIMARY KEY,
    total REAL,
    idcliente INT REFERENCES cliente(idcliente),
    mesa INT,
    status BOOLEAN
);

-- Tabela: cardapio
CREATE TABLE IF NOT EXISTS cardapio (
    idcardapio SERIAL PRIMARY KEY,
    nomeprato VARCHAR(100),
    preco REAL,
    idpedido INT REFERENCES pedido(idpedido)
);

-- Tabela: pagamento
CREATE TABLE IF NOT EXISTS pagamento (
    idpagamento SERIAL PRIMARY KEY,
    idpedido INT REFERENCES pedido(idpedido),
    valor REAL
);

-- Tabela: formapagamento
CREATE TABLE IF NOT EXISTS formapagamento (
    idformapagamento SERIAL PRIMARY KEY,
    metodo VARCHAR(50),
    idpagamento INT REFERENCES pagamento(idpagamento)
);

-- Carga inicial de Funcionários
INSERT INTO funcionario (nomefuncionario, cpf, telefone, email) VALUES
('João Silva', '569.249.267-11', '(27) 99569-7456', 'joao@restaurante.com'),
('Maria Souza', '268.225.156-67', '(27) 99235-6598', 'maria@restaurante.com'),
('Carlos Oliveira', '198.135.983-66', '(27) 99357-1259', 'carlos@restaurante.com'),
('Ana Pereira', '234.852.987-22', '(27) 98569-7534', 'ana@restaurante.com'),
('Jorge Silva dos Santos', '159.753.853-69', '(27) 99733-1289', 'jorge@restaurante.com');

-- Logins dos funcionários
INSERT INTO login (email, senha, idfuncionario) VALUES
('joao@restaurante.com', 'joaozinho123', 1),
('maria@restaurante.com', 'Xfo-i136', 2),
('carlos@restaurante.com', '123456', 3),
('ana@restaurante.com', 'jjko9086', 4),
('jorge@restaurante.com', 'jorge134@', 5);

-- Formas de pagamento
INSERT INTO formapagamento (metodo) VALUES
('Dinheiro'),
('Cartão de Débito'),
('Cartão de Crédito'),
('PIX'),
('Vale Alimentação');

-- Itens do Cardápio (Excluído o valor de ID fixado como NULL para acionar o SERIAL automaticamente)
INSERT INTO cardapio (nomeprato, preco, idpedido) VALUES 
('Risotto', 34.90, NULL),
('Lasanha à Bolonhesa', 29.90, NULL),
('Espaguete à Carbonara', 32.90, NULL),
('Bife Wellington', 35.90, NULL),
('Feijoada', 34.90, NULL),
('Batatas Fritas', 19.90, NULL),
('Mandiocas Fritas', 21.90, NULL),
('Petit Gateau com Sorvete', 22.90, NULL),
('Gelato', 23.90, NULL),
('Sucos Naturais', 7.90, NULL);