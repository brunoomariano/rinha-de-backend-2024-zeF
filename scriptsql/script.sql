CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(22) UNIQUE,
    limite INTEGER,
    saldo INTEGER
);

CREATE TABLE transacoes (
    id SERIAL PRIMARY KEY,
    valor INTEGER,
    tipo CHAR(1),
    descricao VARCHAR(10),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    client_id INTEGER REFERENCES clientes(id)
);


DO $$
BEGIN
  INSERT INTO clientes (id, nome, limite, saldo)
  VALUES
    (1,'ranger red', 1000 * 100, 0),
    (2,'ranger blue', 800 * 100, 0),
    (3,'ranger yellow', 10000 * 100, 0),
    (4,'ranger pink', 100000 * 100, 0),
    (5,'ranger green', 5000 * 100, 0);
END; $$