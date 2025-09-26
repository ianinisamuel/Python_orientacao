create database db_lanchonete;

CREATE TABLE IF NOT EXISTS clientes (
  id serial primary key,
  name varchar(200) not null,
  phone varchar(20) not null,
  adress varchar(255) not null,
  created_at DATE NOT NULL DEFAULT CURRENT_DATE
);

create TABLE IF NOT exists fornecedores (
  id serial primary key,
  name varchar(255) not null,
  phone varchar(20) not null,
  email varchar(100) not null,
  create_at date not null default current_date,
  note text
);

create table if not exists lanches (
  id serial primary key,
  name varchar(255) not null,
  description varchar(255) not null,
  price decimal (10,2) not null
);

create table if not exists pedidos (
  id serial primary key,
  mesa int not null,
  data_pedido TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  status varchar(50) not null
);

create table if not exists ingrediente_est (
  id serial primary key,
  name varchar(255) not null,
  categoria varchar(50) not null,
  quantidade int
  );



