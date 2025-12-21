#=== PRIMERA ENTREGA ====#

CREATE DATABASE IF NOT EXISTS ecommerce_daud;
USE ecommerce_daud;

------------------------------
-- 1) Tabla Clientes
------------------------------
CREATE TABLE  clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    fecha_registro DATETIME
);

------------------------------
-- 2) Tabla Productos
------------------------------
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(120) NOT NULL,
    categoria VARCHAR(80),
    precio INT NOT NULL,
    stock INT NOT NULL,
    created_at DATETIME
);

------------------------------
-- 3) Tabla Ordenes
------------------------------
CREATE TABLE  ordenes (
    id_orden INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha_orden DATETIME,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

------------------------------
-- 4) Tabla Detalle Orden
------------------------------
CREATE TABLE IF NOT EXISTS detalle_orden (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_orden INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario INT NOT NULL,

    FOREIGN KEY (id_orden) REFERENCES ordenes(id_orden),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

------------------------------
-- 5) Tabla Pagos
------------------------------
CREATE TABLE IF NOT EXISTS pagos (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_orden INT NOT NULL,
    metodo_pago VARCHAR(50),
    monto INT NOT NULL,
    fecha_pago DATETIME,

    FOREIGN KEY (id_orden) REFERENCES ordenes(id_orden)
);

#==== SEGUNDA ENTREGA ====#


#== CORRECIONES ==#



ALTER TABLE clientes
ADD UNIQUE (email),
ADD COLUMN ciudad VARCHAR (100),
ADD COLUMN pais VARCHAR (100);


ALTER TABLE ordenes
ADD COLUMN total DECIMAL(10,2);


ALTER TABLE productos
MODIFY precio DECIMAL (10, 2); 

ALTER TABLE detalle_orden
MODIFY precio_unitario DECIMAL (10, 2); 

# === DATOS === #

USE ecommerce_daud;

#=== CLIENTES ===#

USE clientes;


DESCRIBE clientes;

INSERT INTO clientes (nombre, email, fecha_registro, ciudad, pais) 
VALUES 
('Raul Salvatierra', 'raul.salvatierra.35@gmail.com', NOW(), 'Brooklyn', 'USA'),
		('Maria Perez', 'maria@hotmail.com', NOW(), 'Buenos Aires', 'Argentina'),
		('Carlos Lopez', 'carlos@gmail.com', NOW(), 'Madrid', 'España'),
		('Gian Tenorio', 'gian.tenorio6@gmail.com', NOW(), 'Cali', 'Colombia'),
		('Brian Scheller', 'bscheller@gmail.com', NOW(), 'Brooklyn', 'USA'),
		('Juan Perez', 'juan.perez@gmail.com', NOW(), 'Buenos Aires', 'Argentina'),
		('Maria Gonzalez', 'maria.gonzalez@yahoo.com', NOW(), 'Santiago', 'Chile'),
		('Carlos Ramirez', 'carlos.ramirez@hotmail.com', NOW(), 'Lima', 'Peru'),
		('Ana Fernandez', 'ana.fernandez@gmail.com', NOW(), 'Bogotá', 'Colombia'),
		('Luis Martinez', 'luis.martinez@yahoo.com', NOW(), 'Quito', 'Ecuador'),
		('Sofia Lopez', 'sofia.lopez@hotmail.com', NOW(), 'Montevideo', 'Uruguay'),
		('Diego Sanchez', 'diego.sanchez@gmail.com', NOW(), 'Asunción', 'Paraguay'),
	('Camila Torres', 'camila.torres@yahoo.com', NOW(), 'La Paz', 'Bolivia'),
		('Jose Castillo', 'jose.castillo@hotmail.com', NOW(), 'Caracas', 'Venezuela'),
		('Valentina Herrera', 'valentina.herrera@gmail.com', NOW(), 'Ciudad de Mexico', 'Mexico'),
		('Ricardo Morales', 'ricardo.morales@yahoo.com', NOW(), 'Guadalajara', 'Mexico'),
		('Fernanda Diaz', 'fernanda.diaz@hotmail.com', NOW(), 'Medellín', 'Colombia'),
		('Gabriel Ortiz', 'gabriel.ortiz@gmail.com', NOW(), 'Santo Domingo', 'Republica Dominicana'),
		('Isabella Reyes', 'isabella.reyes@yahoo.com', NOW(), 'San Juan', 'Puerto Rico'),
		('Matias Rojas', 'matias.rojas@hotmail.com', NOW(), 'Montevideo', 'Uruguay')
;

# == PRODUCTOS == #

INSERT INTO productos (nombre_producto, categoria, precio, stock, created_at) VALUES
('Vinilo "Midnight Echoes" - The Lunar Tides','Vinilo',28.00,40,'2025-01-05 10:00:00'),
('CD "Midnight Echoes" - The Lunar Tides','CD',18.00,50,'2025-01-10 11:00:00'),
('Camiseta "Midnight Echoes" - The Lunar Tides','Merchandising',22.00,80,'2025-01-15 12:00:00'),
('Pin "The Lunar Tides Logo"','Merchandising',6.00,150,'2025-01-20 13:00:00'),
('Poster "Midnight Echoes Album Art"','Poster',12.00,60,'2025-01-25 14:00:00'),

('Vinilo "Neon Shadows" - Desert Wolves','Vinilo',30.00,35,'2025-02-05 10:00:00'),
('CD "Neon Shadows" - Desert Wolves','CD',20.00,45,'2025-02-10 11:00:00'),
('Camiseta "Neon Shadows" - Desert Wolves','Merchandising',24.00,70,'2025-02-15 12:00:00'),
('Pin "Desert Wolves Logo"','Merchandising',6.50,140,'2025-02-20 13:00:00'),
('Poster "Neon Shadows Album Art"','Poster',13.00,55,'2025-02-25 14:00:00'),

('Vinilo "Crimson Horizon" - The Velvet Roads','Vinilo',32.00,30,'2025-03-05 10:00:00'),
('CD "Crimson Horizon" - The Velvet Roads','CD',21.00,40,'2025-03-10 11:00:00'),
('Camiseta "Crimson Horizon" - The Velvet Roads','Merchandising',25.00,60,'2025-03-15 12:00:00'),
('Pin "Velvet Roads Logo"','Merchandising',7.00,120,'2025-03-20 13:00:00'),
('Poster "Crimson Horizon Album Art"','Poster',14.00,50,'2025-03-25 14:00:00'),

('Vinilo "Echoes in Silence" - Midnight Signals','Vinilo',29.00,38,'2025-04-05 10:00:00'),
('CD "Echoes in Silence" - Midnight Signals','CD',19.00,48,'2025-04-10 11:00:00'),
('Camiseta "Echoes in Silence" - Midnight Signals','Merchandising',23.00,75,'2025-04-15 12:00:00'),
('Pin "Midnight Signals Logo"','Merchandising',6.50,130,'2025-04-20 13:00:00'),
('Poster "Echoes in Silence Album Art"','Poster',12.50,55,'2025-04-25 14:00:00'),

('Vinilo "Solar Flare" - Electric Alley','Vinilo',31.00,33,'2025-05-05 10:00:00'),
('CD "Solar Flare" - Electric Alley','CD',20.50,42,'2025-05-10 11:00:00'),
('Camiseta "Solar Flare" - Electric Alley','Merchandising',24.50,70,'2025-05-15 12:00:00'),
('Pin "Electric Alley Logo"','Merchandising',6.00,120,'2025-05-20 13:00:00'),
('Poster "Solar Flare Album Art"','Poster',13.00,50,'2025-05-25 14:00:00'),

('Vinilo "Obsidian Dreams" - The Hidden Frequencies','Vinilo',33.00,28,'2025-06-05 10:00:00'),
('CD "Obsidian Dreams" - The Hidden Frequencies','CD',22.00,38,'2025-06-10 11:00:00'),
('Camiseta "Obsidian Dreams" - The Hidden Frequencies','Merchandising',26.00,65,'2025-06-15 12:00:00'),
('Pin "Hidden Frequencies Logo"','Merchandising',7.50,110,'2025-06-20 13:00:00'),
('Poster "Obsidian Dreams Album Art"','Poster',14.50,45,'2025-06-25 14:00:00'),

('Vinilo "Twilight Reverie" - Scarlet Horizon','Vinilo',30.00,35,'2025-07-05 10:00:00'),
('CD "Twilight Reverie" - Scarlet Horizon','CD',20.00,45,'2025-07-10 11:00:00'),
('Camiseta "Twilight Reverie" - Scarlet Horizon','Merchandising',24.00,70,'2025-07-15 12:00:00'),
('Pin "Scarlet Horizon Logo"','Merchandising',6.50,140,'2025-07-20 13:00:00'),
('Poster "Twilight Reverie Album Art"','Poster',13.00,55,'2025-07-25 14:00:00'),

('Vinilo "Nocturnal Waves" - Phantom Roads','Vinilo',29.50,36,'2025-08-05 10:00:00'),
('CD "Nocturnal Waves" - Phantom Roads','CD',19.50,46,'2025-08-10 11:00:00'),
('Camiseta "Nocturnal Waves" - Phantom Roads','Merchandising',23.50,72,'2025-08-15 12:00:00'),
('Pin "Phantom Roads Logo"','Merchandising',6.00,130,'2025-08-20 13:00:00'),
('Poster "Nocturnal Waves Album Art"','Poster',12.50,50,'2025-08-25 14:00:00'),

('Vinilo "Crimson Echo" - Lunar Eclipse','Vinilo',32.00,30,'2025-09-05 10:00:00'),
('CD "Crimson Echo" - Lunar Eclipse','CD',21.00,40,'2025-09-10 11:00:00'),
('Camiseta "Crimson Echo" - Lunar Eclipse','Merchandising',25.00,65,'2025-09-15 12:00:00'),
('Pin "Lunar Eclipse Logo"','Merchandising',7.00,120,'2025-09-20 13:00:00'),
('Poster "Crimson Echo Album Art"','Poster',14.00,45,'2025-09-25 14:00:00'),

('Vinilo "Velvet Skies" - Aurora Fields','Vinilo',31.00,34,'2025-10-05 10:00:00'),
('CD "Velvet Skies" - Aurora Fields','CD',20.50,44,'2025-10-10 11:00:00'),
('Camiseta "Velvet Skies" - Aurora Fields','Merchandising',24.50,68,'2025-10-15 12:00:00'),
('Pin "Aurora Fields Logo"','Merchandising',6.50,125,'2025-10-20 13:00:00'),
('Poster "Velvet Skies Album Art"','Poster',13.50,52,'2025-10-25 14:00:00');


# === ORDENES === #


INSERT INTO ordenes (id_cliente, fecha_orden) VALUES
(1, '2025-01-15 10:20:00'),
(2, '2025-02-03 14:45:00'),
(3, '2025-03-10 09:30:00'),
(4, '2025-04-22 16:10:00'),
(5, '2025-05-05 11:50:00'),
(6, '2025-06-18 13:25:00'),
(7, '2025-07-07 17:40:00'),
(8, '2025-08-12 12:15:00'),
(9, '2025-09-25 15:30:00'),
(10, '2025-10-03 10:05:00'),
(11, '2025-11-11 14:20:00'),
(12, '2025-12-01 09:55:00'),
(13, '2025-01-28 16:45:00'),
(14, '2025-02-15 11:10:00'),
(15, '2025-03-30 13:50:00'),
(16, '2025-04-18 17:25:00'),
(17, '2025-05-27 10:40:00'),
(18, '2025-06-09 12:35:00'),
(19, '2025-07-21 15:15:00'),
(20, '2025-08-30 09:50:00'),
(21, '2025-09-14 14:05:00');


# == DETALLE ORDEN == #

INSERT INTO detalle_orden (id_orden, id_producto, cantidad, precio_unitario) 
VALUES
(1, 1, 2, 28.00),
(1, 5, 1, 12.00),
(2, 2, 1, 18.00),
(2, 10, 2, 24.00),
(2, 15, 1, 13.00),
(3, 3, 1, 22.00),
(3, 7, 2, 25.00),
(4, 4, 1, 30.00),
(4, 12, 1, 14.00),
(4, 20, 2, 23.50),
(5, 8, 1, 26.00),
(5, 18, 2, 19.50),
(6, 6, 1, 31.00),
(6, 11, 2, 13.50),
(7, 9, 1, 21.00),
(7, 13, 1, 12.50),
(7, 17, 1, 24.50),
(8, 14, 2, 28.00),
(8, 19, 1, 14.00),
(9, 16, 1, 23.00),
(9, 21, 2, 25.00),
(10, 22, 1, 20.50),
(10, 25, 2, 13.00),
(11, 23, 1, 24.00),
(11, 27, 1, 12.50),
(12, 24, 2, 22.00),
(12, 29, 1, 14.50),
(13, 26, 1, 25.00),
(13, 30, 2, 12.00),
(14, 28, 1, 23.50),
(14, 31, 2, 13.50),
(15, 32, 1, 24.50),
(15, 35, 1, 26.00),
(16, 33, 2, 22.50),
(16, 37, 1, 19.50),
(17, 34, 1, 21.00),
(17, 40, 2, 25.00),
(18, 36, 1, 28.00),
(18, 39, 1, 12.50),
(19, 38, 2, 24.00),
(19, 41, 1, 13.50),
(20, 42, 1, 23.50),
(20, 45, 2, 14.00),
(21, 43, 1, 26.00),
(21, 47, 1, 25.00);

# === PAGOS === # 

INSERT INTO pagos (id_orden, metodo_pago, monto, fecha_pago) VALUES
(1, 'Tarjeta de crédito', 68.00, '2025-01-15 11:00:00'),
(2, 'Venmo', 79.00, '2025-02-03 15:00:00'),
(3, 'Zelle', 72.00, '2025-03-10 10:00:00'),
(4, 'Tarjeta de crédito', 87.50, '2025-04-22 17:00:00'),
(5, 'Venmo', 71.00, '2025-05-05 12:30:00'),
(6, 'Zelle', 57.50, '2025-06-18 14:00:00'),
(7, 'Tarjeta de crédito', 82.50, '2025-07-07 18:30:00'),
(8, 'Venmo', 70.00, '2025-08-12 13:30:00'),
(9, 'Zelle', 73.00, '2025-09-25 16:00:00'),
(10, 'Tarjeta de crédito', 54.00, '2025-10-03 11:00:00');


#=== VISTAS ===#

#=1=# 

CREATE VIEW vw_detalle_compra AS
SELECT 	p.categoria,
		pa.metodo_pago,
		d.precio_unitario
FROM detalle_orden AS d
INNER JOIN productos AS p ON d.id_producto = p.id_producto
INNER JOIN ordenes AS o ON d.id_orden = o.id_orden
INNER JOIN pagos AS pa ON o.id_orden = pa.id_orden;


#=2=# 
CREATE VIEW vw_total_por_clientes AS
SELECT 	c.nombre,
		p.categoria,
        o.fecha_orden,
		pa.monto
FROM clientes AS c
INNER JOIN ordenes AS o ON c.id_cliente = o.id_cliente
INNER JOIN detalle_orden AS do ON o.id_orden = do.id_orden
INNER JOIN productos AS p ON do.id_producto = p.id_producto
INNER JOIN pagos AS pa ON o.id_orden = pa.id_orden; 

#=3=#
 
CREATE VIEW vw_ordenes_por_ubicacion AS 
SELECT 	c.ciudad,
		c.pais,
        COUNT(o.id_orden) AS cantidad_ordenes
FROM clientes AS c 
LEFT JOIN ordenes AS o ON c.id_cliente = o.id_cliente 
GROUP BY c.ciudad, c.pais; 

#=4=# 

CREATE VIEW vw_fecha_producto AS
SELECT 	o.id_orden,
		o.fecha_orden,
		p.categoria,
		p.created_at
FROM ordenes o
INNER JOIN detalle_orden d ON o.id_orden = d.id_orden
INNER JOIN productos p ON d.id_producto = p.id_producto;

#=5=# 

CREATE VIEW vw_stock_productos AS
SELECT 	p.nombre_producto,
		p.stock,
        d.precio_unitario
FROM productos p
JOIN detalle_orden d ON p.id_producto = d.id_producto; 


# EJECUSIONES #

SELECT * FROM vw_detalle_compra
WHERE metodo_pago IN ('Venmo'); 

SELECT * FROM vw_total_por_clientes
WHERE categoria IN ('Vinilo');

SELECT * FROM vw_ordenes_por_ubicacion
WHERE pais IN ('Argentina');

SELECT * FROM vw_fecha_producto 
WHERE MONTH  (fecha_orden)  =3;  

SELECT * FROM vw_stock_productos
WHERE precio_unitario < 25;


# === FUNCIONES === # 

# = 1 = #

USE ecommerce_daud;
DELIMITER //

CREATE FUNCTION monto_total_ordenes (param_idOrden INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN 
    DECLARE total DECIMAL(10,2);
    
    SELECT IFNULL(SUM(precio_unitario * cantidad), 0)
    INTO total
    FROM detalle_orden
    WHERE id_orden = param_idOrden; 
    
    RETURN total;
END//

DELIMITER ;

SELECT monto_total_ordenes (2,3,8);

# = 2 = #

DELIMITER //

CREATE FUNCTION ubicacion_clientes(param_idCliente INT)
RETURNS VARCHAR(250)
DETERMINISTIC
BEGIN
    DECLARE info VARCHAR(250);
    SELECT CONCAT(nombre, ', ', ciudad, ', ', pais) INTO info
    FROM clientes
    WHERE id_cliente = param_idCliente;

    RETURN info;
END//

DELIMITER ;

SELECT ubicacion_clientes (2); 


#=== SP ===#

# = 1 = #

DELIMITER //

CREATE PROCEDURE sp_listar_ordenes_cliente (IN p_id_cliente INT)
BEGIN
    SELECT 
        o.id_orden,
        o.fecha_orden,
        monto_total_ordenes(o.id_orden) AS total
    FROM ordenes AS o
    WHERE o.id_cliente = p_id_cliente;
END//

DELIMITER //

USE ecommerce_daud;  
CALL sp_listar_ordenes_cliente(2);

# = 2 = # 


DELIMITER //

CREATE PROCEDURE sp_ordenar_clientes(IN p_tabla VARCHAR(225),IN p_columna VARCHAR(225),IN p_orden VARCHAR(225))
BEGIN
    SET @sql_text = CONCAT('SELECT * FROM `', p_tabla, '` ORDER BY `', p_columna, '` ', p_orden, ';');
    PREPARE stmt FROM @sql_text;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END//

DELIMITER ;

CALL sp_ordenar_clientes('clientes', 'fecha_registro', 'ASC');

#=== TRIGGERS ===#

DELIMITER //

CREATE TRIGGER trg_actualizar_stock
AFTER INSERT ON detalle_orden
FOR EACH ROW
BEGIN
    UPDATE productos
    SET stock = stock - NEW.cantidad
    WHERE id_producto = NEW.id_producto;
END//

DELIMITER ;

SELECT stock FROM productos WHERE id_producto = 15;


DELIMITER //

CREATE TRIGGER tr_agregar_cliente
AFTER INSERT ON clientes
FOR EACH ROW
BEGIN
    INSERT INTO nuevo_cliente(id_cliente, nombre, ciudad, pais)
    VALUES (NEW.id_cliente, NEW.nombre, NEW.ciudad, NEW.pais);
END//

DELIMITER ;


INSERT INTO clientes (nombre, email, fecha_registro)
VALUES ('Sebastian Cendoya', 'sebastian@example.com', NOW());



