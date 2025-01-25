# To-Do List API avec Flask

## Description
Une API RESTful permettant de gérer une liste de tâches avec des fonctionnalités d'authentification pour que chaque utilisateur puisse gérer ses propres tâches.

## Technologies utilisées
- Python (Flask)
- MySQL
- Flask SQLAlchemy
- Flask Bcrypt
- Flask JWT Extended

## Structure du projet
```
project_root/
│-- app/
│   │-- __init__.py
│   │-- models.py
│   │-- routes.py
│-- config.py
│-- run.py
│-- requirements.txt
│-- README.md
```

## Installation

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/votre-repo/todo-list-api.git
   cd todo-list-api
   ```

2. Créer un environnement virtuel et l'activer :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Configurer la base de données :
   - Créer une base de données MySQL nommée `todo_db`.
   - Mettre à jour `config.py` avec vos informations de connexion.

5. Initialiser la base de données :
   ```python
   from app import db
   db.create_all()
   ```

6. Lancer le serveur :
   ```bash
   python run.py
   ```

## Endpoints de l'API

### Authentification
- `POST /register` : Inscription d'un utilisateur
- `POST /login` : Connexion et obtention d'un token JWT

### Gestion des tâches
- `POST /tasks` : Ajouter une tâche (JWT requis)
- `GET /tasks` : Obtenir toutes les tâches de l'utilisateur (JWT requis)
- `PUT /tasks/<int:task_id>` : Modifier une tâche (JWT requis)
- `DELETE /tasks/<int:task_id>` : Supprimer une tâche (JWT requis)

## Exemple de requête avec cURL

```bash
# Inscription d'un utilisateur
curl -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "password"}' http://localhost:5000/register

# Connexion et obtention du token JWT
curl -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "password"}' http://localhost:5000/login
```

## Contribution
Les contributions sont les bienvenues ! Créez une issue ou soumettez une pull request.

## Licence
MIT Licence