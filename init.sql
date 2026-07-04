CREATE DATABASE IF NOT EXISTS sistema_login;
USE sistema_login;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    tipo ENUM('cliente', 'funcionario') NOT NULL DEFAULT 'cliente',
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Usuários de teste
INSERT INTO usuarios (nome, email, senha, tipo) 
VALUES 
('Administrador', 'admin@email.com', 'e6c83b282aeb2e022844e60c2e7c9f4a2c3b5d6e7f8a9b0c1d2e3f4a5b6c7d8e', 'funcionario'),
('João Cliente', 'cliente@email.com', 'e6c83b282aeb2e022844e60c2e7c9f4a2c3b5d6e7f8a9b0c1d2e3f4a5b6c7d8e', 'cliente')
ON DUPLICATE KEY UPDATE nome = nome;