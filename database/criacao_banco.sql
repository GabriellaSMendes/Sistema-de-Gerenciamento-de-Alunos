CREATE DATABASE sistema_gerenciamento;

USE sistema_gerenciamento;

CREATE TABLE IF NOT EXISTS usuario(
	id INT auto_increment PRIMARY KEY,
    nome VARCHAR(70) NOT NULL,
    matricula VARCHAR(6) NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    tipo ENUM('ALUNO', 'PROFESSOR', 'ADMIN') NOT NULL
);

CREATE TABLE IF NOT EXISTS disciplina(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cod_disciplina VARCHAR(6) NOT NULL,
    id_professor INT,
    FOREIGN KEY (id_professor) REFERENCES usuario(id)    
);

CREATE TABLE IF NOT EXISTS turma(
	id INT AUTO_INCREMENT PRIMARY KEY,
    cod_turma VARCHAR(15) NOT NULL,
    id_disciplina INT NOT NULL,
    id_professor INT NOT NULL,
    ano INT NOT NULL,
    semestre INT NOT NULL,
    FOREIGN KEY (id_disciplina) REFERENCES disciplina(id),
    FOREIGN KEY (id_professor) REFERENCES usuario(id)
);

CREATE TABLE IF NOT EXISTS notas(
	id INT AUTO_INCREMENT PRIMARY KEY,
    id_disciplina INT NOT NULL,
    id_aluno INT NOT NULL,
    id_turma INT NOT NULL,
    avaliacao VARCHAR(50),
    nota DECIMAL(5,2),
    data_lancamento DATE
);

CREATE TABLE IF NOT EXISTS relatorio(
	id INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT NOT NULL,
    media DECIMAL(5,2),
    situacao ENUM('Aprovado', 'Reprovado', 'Em andamento')  NOT NULL,
    FOREIGN KEY (id_aluno) REFERENCES usuario(id)
);
