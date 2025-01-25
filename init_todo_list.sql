-- Créer la base de données si elle n'existe pas
CREATE DATABASE IF NOT EXISTS todo_list;

-- Utiliser la base de données
USE todo_list;

-- Création de la table des utilisateurs
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Création de la table des tâches
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('pending', 'in-progress', 'completed') DEFAULT 'pending',
    user_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);


-- Insérer des utilisateurs de test
INSERT INTO users (username, password, email)
VALUES
('john_doe', 'hashed_password_here', 'john@example.com'),
('jane_doe', 'hashed_password_here', 'jane@example.com');

-- Insérer des tâches de test
INSERT INTO tasks (title, description, status, user_id)
VALUES
('Acheter du lait', 'Aller au supermarché pour acheter du lait', 'pending', 1),
('Réviser le projet', 'Finaliser le projet pour la réunion', 'in-progress', 2),
('Faire du sport', 'Aller courir pendant 30 minutes', 'completed', 1);

-- Vérifier que les données ont été insérées correctement
SELECT * FROM users;
SELECT * FROM tasks;