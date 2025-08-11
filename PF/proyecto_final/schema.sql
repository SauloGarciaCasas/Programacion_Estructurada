CREATE DATABASE IF NOT EXISTS gestion_escolar
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE gestion_escolar;

CREATE TABLE IF NOT EXISTS usuarios (
  id            INT AUTO_INCREMENT PRIMARY KEY,
  nombre        VARCHAR(80)  NOT NULL,
  email         VARCHAR(150) NOT NULL UNIQUE,
  password_hash VARCHAR(60)  NOT NULL
);

CREATE TABLE IF NOT EXISTS grupos (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  nombre      VARCHAR(120) NOT NULL,
  usuario_id  INT NOT NULL,
  fecha       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT uq_grupo_usuario UNIQUE (nombre, usuario_id),
  CONSTRAINT fk_grupos_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS alumnos (
  id       INT AUTO_INCREMENT PRIMARY KEY,
  nombre   VARCHAR(120) NOT NULL,
  grupo_id INT NOT NULL,
  fecha    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_alumnos_grupo FOREIGN KEY (grupo_id) REFERENCES grupos(id) ON DELETE CASCADE
);

CREATE INDEX idx_alumnos_nombre ON alumnos (nombre);
