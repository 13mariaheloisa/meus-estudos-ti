-- ==========================================
-- Projeto: Modelo de Banco de Dados - Livraria
-- Descrição: Criação de tabelas relacionais básicas para prática de SQL.
-- Desenvolvido por: Maria Heloisa
-- ==========================================

-- 1. Criação do Banco de Dados
CREATE DATABASE db_livraria;

-- Selecionando o banco para uso
USE db_livraria;

-- 2. Tabela de Clientes
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    data_cadastro DATE
);

-- 3. Tabela de Livros
CREATE TABLE livros (
    id_livro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    estoque INT NOT NULL
);

-- 4. Inserindo alguns dados de exemplo (DML)
INSERT INTO clientes (nome, email, data_cadastro) 
VALUES ('Ana Souza', 'ana@email.com', '2026-10-01');

INSERT INTO livros (titulo, autor, preco, estoque) 
VALUES ('O Hobbit', 'J.R.R. Tolkien', 45.90, 12);

-- 5. Consulta básica para verificar os dados cadastrados
SELECT * FROM livros;
