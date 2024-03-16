-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.36 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando datos para la tabla db.posts: ~0 rows (aproximadamente)

-- Volcando datos para la tabla db.user: ~1 rows (aproximadamente)
INSERT IGNORE INTO `user` (`id`, `username`, `apellido`, `apellido2`, `residencia`, `email`, `telefono`, `telefonoE`, `celular`, `password`, `confirmpassword`, `alergias`, `cronico`, `medicamentos`, `nacimiento`, `imagen_perfil`, `date_added`) VALUES
	(1, 'Kenneth', 'Ruiz', 'Matamoros', 'cartagop', 'kenth11977@gmail.com', '86227500', NULL, '86227500', '$2b$12$OjG75mfV5qQ/JikI8Tf78Odx46p05kxZ85krowYd5Ai7B3puUZhNC', '$2b$12$OjG75mfV5qQ/JikI8Tf78Odx46p05kxZ85krowYd5Ai7B3puUZhNC', 'asma', 'asma', 'salbutamol', 'noviembre', 'default.jpg', '2024-03-15 21:21:02');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
