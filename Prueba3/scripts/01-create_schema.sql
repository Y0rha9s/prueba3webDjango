use carniceria;

create table region(
    CODIGO int primary key,
    NOMBRE varchar(80) not null,
    DESCRIPCION varchar(300)
)

create table region(
	id int auto_increment primary key,
    nombre varchar(120) not null,
    descripcion varchar(400)
);

create table Contact(
	id int auto_increment primary key,
	nombres varchar(120) not null,
    apellidos varchar(120) not null,
    telefono int
);