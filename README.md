# To-Do List API

Une API RESTful de gestion de liste de tâches (To-Do List) avec Flask, MySQL, et JWT pour l'authentification.

## Prérequis

Avant de commencer, vous devez avoir installé les éléments suivants :

- Python 3.6 ou supérieur
- MariaDB (ou MySQL)
- Virtualenv (optionnel mais recommandé)
- Pip (gestionnaire de paquets Python)

## Installation

### 1. Clonez le dépôt

Clonez ce projet sur votre machine locale :

```bash
git clone https://github.com/CodesVibes229/To-do_list.git
cd To-Do_list
```

### 2. Créez et activez un environnement virtuel

Si vous n'avez pas encore configuré un environnement virtuel, voici comment faire :

```bash
python3 -m venv venv
source venv/bin/activate  # Sur Linux/MacOS
venv\Scripts\activate     # Sur Windows
```

### 3. Installez les dépendances

Installez les bibliothèques nécessaires via `pip` :

```bash
pip install -r requirements.txt
```

Le fichier `requirements.txt` inclut les dépendances suivantes :

```
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
Flask-Migrate==3.1.0
Flask-Bcrypt==0.7.1
Flask-JWT-Extended==4.2.1
PyMySQL==1.0.2
pytest==6.2.4
```

### 4. Configuration de la base de données

#### Créez la base de données

Ouvrez MariaDB/MySQL et créez une base de données :

```sql
CREATE DATABASE todo_list;
```

#### Configurez votre connexion à la base de données

Dans le fichier `config.py`, configurez la connexion à votre base de données MySQL (ou MariaDB) :

```python
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/todo_list'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

Remplacez `user` et `password` par vos informations de connexion MySQL.

#### Créez les tables

Après avoir configuré la base de données, lancez les migrations pour créer les tables :

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5. Exécution de l'API

Lancez l'API avec la commande suivante :

```bash
flask run
```

Cela démarre l'API sur `http://127.0.0.1:5000/`.

## Endpoints

### POST `/tasks`

Création d'une nouvelle tâche.

#### Exemple de requête :

```bash
POST /tasks
Content-Type: application/json
Authorization: Bearer <JWT>

{
  "title": "Nouvelle tâche",
  "description": "Détails de la tâche"
}
```

### GET `/tasks`

Récupération de la liste des tâches.

#### Exemple de requête :

```bash
GET /tasks
Authorization: Bearer <JWT>
```

### PUT `/tasks/<task_id>`

Mise à jour d'une tâche existante.

#### Exemple de requête :

```bash
PUT /tasks/1
Content-Type: application/json
Authorization: Bearer <JWT>

{
  "title": "Tâche mise à jour",
  "description": "Nouveaux détails"
}
```

### DELETE `/tasks/<task_id>`

Suppression d'une tâche.

#### Exemple de requête :

```bash
DELETE /tasks/1
Authorization: Bearer <JWT>
```

## Tests

Pour exécuter les tests de l'API, vous pouvez utiliser `pytest` :

```bash
pytest test_api.py
```

Cela exécute tous les tests définis dans le fichier `test_api.py`.

## Résolution des erreurs courantes

- **Erreur d'accès à la base de données** : Si vous obtenez l'erreur `Access denied for user 'user'@'localhost'`, cela signifie que les informations de connexion à la base de données sont incorrectes ou que l'utilisateur n'a pas les droits appropriés. Vérifiez vos identifiants MySQL/MariaDB et assurez-vous que l'utilisateur dispose des autorisations nécessaires pour accéder à la base de données.
  
- **Migrations non appliquées** : Si vous obtenez une erreur liée aux migrations, assurez-vous d'avoir exécuté les commandes `flask db init`, `flask db migrate`, et `flask db upgrade` correctement.

- **Tests échoués** : Si les tests échouent, vérifiez vos configurations et assurez-vous que les dépendances sont installées et correctement configurées.

## Contribution

Si vous souhaitez contribuer à ce projet, veuillez créer une branche, apporter vos modifications et ouvrir une pull request.

