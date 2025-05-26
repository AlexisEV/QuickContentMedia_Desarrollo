-- 1. Usuarios
INSERT INTO USUARIO (username, nombre, apellido, contrasena) VALUES
  ('aaa', 'aaa', 'aaa', '123'),
  ('u2', 'María', 'Gamez', '456'),
  ('A3', 'bbb', 'bbb', '123');

-- 2. Administradores (referencian USUARIO)
INSERT INTO ADMINISTRADOR (id_usuario, acceso) VALUES
  (3, TRUE);

-- 3. Clientes (referencian USUARIO)
INSERT INTO CLIENTE (id_usuario, saldo, excliente) VALUES
  (1, 1000, FALSE),
  (2, 500, TRUE);

-- 4. Tipos de archivo
INSERT INTO TIPO_ARCHIVO (extension, tipo_contenido, mime_type) VALUES
  ('mp3', 'sonido', 'sonido/mp3'),
  ('jpg', 'imagen', 'image/jpeg');

-- 5. Promociones
INSERT INTO PROMOCION (descuento, fecha_inicio, fecha_fin) VALUES
  (10, '2025-05-01', '2025-05-31'),
  (20, '2025-06-01', '2025-06-30');

-- 6. Categorías (auto-relación)
INSERT INTO CATEGORIA (nombre, id_categoria_padre) VALUES
  ('A', NULL),
  ('SubcategoríaA', 1);

-- 7. Contenidos (referencian TIPO_ARCHIVO, PROMOCION, CATEGORIA)
INSERT INTO CONTENIDO (formato, autor, archivo, nombre, precio, tamano_archivo, descripcion, id_tipo_archivo, id_promocion, id_categoria) VALUES
  ('imagen', 'Autor1', 'mp3.pdf', 'Manual de Usuario', 150, 2.3, 'Guía completa', 1, 1, 1),
  ('sonido', 'Autor2', 'imagen1.jpg', 'Foto de Producto', 50, 0.8, 'Imagen de alta resolución', 2, 2, 2);

-- 8. Rankings
INSERT INTO RANKING (tipo, fecha_inicio_semanal) VALUES
  ('descarga', '2025-05-19'),
  ('calificacion', '2025-05-01');

-- 9. Calificaciones (referencian CLIENTE y RANKING)
INSERT INTO CALIFICACION (fecha, nota, id_usuario, id_ranking) VALUES
  ('2025-05-1', 4, 2, 2);

-- 10. Descargas (referencian CONTENIDO, CLIENTE, CALIFICACION y RANKING)
INSERT INTO DESCARGA (fecha, id_contenido, id_usuario, id_calificacion, id_ranking) VALUES
  ('2025-05-22', 1, 1, 1, 1);

-- 11. Historial (referencian CLIENTE)
INSERT INTO HISTORIAL (precio_total, id_usuario) VALUES
  (30, 1),
  (15, 2);

-- 12. Regalos (referencian CLIENTE y CONTENIDO)
INSERT INTO REGALO (fecha, abierto, id_usuario_emisor, id_usuario_receptor, id_contenido) VALUES
  ('2025-05-1', TRUE, 1, 2, 1),
  ('2025-05-2', FALSE, 2, 1, 2);
