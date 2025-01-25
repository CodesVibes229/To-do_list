from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import Config

# Initialisation des extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialiser les extensions avec l'application
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Importer et enregistrer les routes
    from app.routes import main

    app.register_blueprint(main)

    return app
