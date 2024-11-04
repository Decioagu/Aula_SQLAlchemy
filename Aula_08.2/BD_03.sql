CREATE DATABASE IF NOT EXISTS cinema_03;

USE cinema_03;

CREATE TABLE IF NOT EXISTS filmes (
    titulo VARCHAR(50) NOT NULL,
    genero VARCHAR(30) NOT NULL,
    ano YEAR NOT NULL,
    PRIMARY KEY(titulo)
);

INSERT INTO filmes (titulo, genero, ano)
VALUE ("Forest Gump", "Drama", 1994);

INSERT INTO filmes (titulo, genero, ano)
VALUE ("O predador", "Ação", 1987);