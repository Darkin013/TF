-- Cria o banco de dados 'escola'
CREATE DATABASE escola;

-- Conecta ao banco de dados 'escola'
\c escola;

-- Cria a tabela 'alunos'
CREATE TABLE alunos (
    aluno_id VARCHAR(5) NOT NULL,
    nome VARCHAR(40) NOT NULL,
    endereco VARCHAR(60),
    cidade VARCHAR(15),
    estado VARCHAR(15),
    cep VARCHAR(10),
    pais VARCHAR(15),
    telefone VARCHAR(24),
    PRIMARY KEY (aluno_id)
);

-- Insere pelo menos 10 alunos na tabela 'alunos'
INSERT INTO alunos (aluno_id, nome, endereco, cidade, estado, cep, pais, telefone) VALUES
('A001', 'João Silva', 'Rua A, 123', 'São Paulo', 'SP', '01000-000', 'Brasil', '1111-1111'),
('A002', 'Maria Souza', 'Rua B, 456', 'Rio de Janeiro', 'RJ', '02000-000', 'Brasil', '2222-2222'),
('A003', 'Pedro Oliveira', 'Rua C, 789', 'Belo Horizonte', 'MG', '03000-000', 'Brasil', '3333-3333'),
('A004', 'Ana Pereira', 'Rua D, 101', 'Curitiba', 'PR', '04000-000', 'Brasil', '4444-4444'),
('A005', 'Carlos Lima', 'Rua E, 202', 'Porto Alegre', 'RS', '05000-000', 'Brasil', '5555-5555'),
('A006', 'Fernanda Costa', 'Rua F, 303', 'Salvador', 'BA', '06000-000', 'Brasil', '6666-6666'),
('A007', 'Lucas Almeida', 'Rua G, 404', 'Fortaleza', 'CE', '07000-000', 'Brasil', '7777-7777'),
('A008', 'Juliana Santos', 'Rua H, 505', 'Manaus', 'AM', '08000-000', 'Brasil', '8888-8888'),
('A009', 'Rafael Gomes', 'Rua I, 606', 'Recife', 'PE', '09000-000', 'Brasil', '9999-9999'),
('A010', 'Patrícia Rocha', 'Rua J, 707', 'Florianópolis', 'SC', '10000-000', 'Brasil', '1010-1010');