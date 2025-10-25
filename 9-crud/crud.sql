CREATE DATABASE uala;

CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    data_nascimento DATE,
    saldo DECIMAL(10,2),
    ativo BOOLEAN DEFAULT TRUE,
    cadastro_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO cliente(nome, email, telefone, data_nascimento, saldo, ativo)
VALUES("Daniel Lopes", "dniel150@proton.me", "11 97544-5123", "2008-03-20", 0.00, TRUE)