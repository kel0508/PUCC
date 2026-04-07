CREATE TABLE produto (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100),
preco DECIMAL(10,2),
categoria VARCHAR(50)
);
CREATE TABLE cliente (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100),
cidade VARCHAR(100),
idade INT
);
CREATE TABLE pedido (
id INT AUTO_INCREMENT PRIMARY KEY,
cliente_id INT,
valor_total DECIMAL(10,2),
data_pedido DATE
);

insert into produto (id, nome, preco, categoria)
values (1, "livro", 50.99, "entretenimento"),
(2, "celular", 5000.00, "eletronico"),
(3, "creme de cabelo", 50.99, "cosméticos"),
(4, "pizza", 70.99, "alimento");

insert into cliente (id, nome, cidade, idade)
values (1, "Gustavo", "Sumaré", 20),
(2, "Raquel", "Paulínia", 18),
(3, "Paulo", "Porto Ferreira", 54),
(4, "Lucas", "Campinas", 22),
(5, "Mayara", "Campinas", 25);

insert into pedido (id, cliente_id, valor_total, data_pedido)
values (1, 1, 500, "2023-05-12"),
(2, 2, 9200, "2024-07-07"),
(3, 3, 2000, "2025-08-09"),
(4, 3, 14000, "2026-02-14");

select nome from cliente where idade >= (select avg(idade) from cliente);

select nome, preco from produto where preco >= (select avg(preco) from produto);

select nome from cliente where cidade in (select cidade from cliente group by cidade having count(*) = 1);

select nome from produto where preco in (select preco from produto group by preco having count(preco) > 1);

select * from pedido where valor_total > (select max(valor_total) from pedido where data_pedido >= "2023-01-01" and data_pedido <= "2023-12-31"); 

select nome from cliente where id not in (select cliente_id from pedido);