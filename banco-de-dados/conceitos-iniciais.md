# 🗄️ Fundamentos de Banco de Dados

Resumo dos principais conceitos e comandos iniciais estudados em Análise e Desenvolvimento de Sistemas.

---

## 1. O que é um Banco de Dados?
É um sistema organizado para armazenar, gerenciar e recuperar grandes volumes de dados de forma segura e rápida.

- **SGBD (Sistema de Gerenciamento de Banco de Dados):** O software que faz a interface entre o banco de dados e os usuários/aplicações (ex: MySQL, PostgreSQL, MongoDB).

---

## 2. Tipos Principais de Bancos de Dados
* **Relacionais (SQL):** Os dados são organizados em **tabelas** (linhas e colunas), com relações bem definidas entre si. 
  * *Exemplos:* MySQL, PostgreSQL, SQL Server.
* **Não Relacionais (NoSQL):** Os dados são armazenados de forma mais flexível (geralmente em formato de documentos JSON ou pares de chave-valor).
  * *Exemplos:* MongoDB, Redis.

---

## 3. Comandos Básicos em SQL (Linguagem de Consulta Estruturada)

O SQL é dividido em subconjuntos. Os comandos mais comuns que utilizamos no dia a dia são:

### 🔹 DDL (Data Definition Language) - Estrutura
Comandos para criar e modificar a estrutura do banco:
* `CREATE DATABASE nome_do_banco;` -> Cria um novo banco de dados.
* `CREATE TABLE nome_tabela (...);` -> Cria uma nova tabela.

### 🔹 DML (Data Manipulation Language) - Dados
Comandos para manipular os dados de dentro das tabelas:
* **SELECT:** Consulta dados.
  ```sql
  SELECT * FROM clientes;
* **INSERT:** Insere novos registros.
  INSERT INTO clientes (nome, email) VALUES ('Ana', 'ana@email.com');
* **UPDATE:** Atualiza registros existentes.
  UPDATE clientes SET email = 'novo_email@email.com' WHERE id = 1;
* **DELETE:** Apaga registros.
  DELETE FROM clientes WHERE id = 1;
